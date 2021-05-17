from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory

from .models import Dress, ImagesDress
from .forms import DressForm

ImageFormSet = modelformset_factory(ImagesDress, fields=('image',), extra=2)


def index(request):
    dresses = Dress.objects.all()
    return render(request, 'index.html', {'dresses': dresses})


def single_dress(request, dress_id):
    dress = get_object_or_404(Dress, id=dress_id)
    return render(request, 'dresses/dress_card.html', {'dress': dress})


def create_edit_dress(request):
    dress_form = DressForm(request.POST or None, request.FILES or None)
    image_formset = ImageFormSet(request.POST or None, request.FILES or None)
    if dress_form.is_valid() and image_formset.is_valid():
        dress = dress_form.save(commit=False)
        images = image_formset.save(commit=False)
        for image in images:
            image.dress = dress
            image.save()
        dress.save()
        return redirect('index')
    return render(
        request,
        'dresses/create_edit_dress.html',
        {
            'dress_form': dress_form,
            'image_formset': image_formset
        })
