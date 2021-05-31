from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Dress
from .forms import DressForm


def index(request):
    dresses = Dress.objects.all()
    return render(request, 'index.html', {'dresses': dresses})


def single_dress(request, dress_id):
    dress = get_object_or_404(Dress, id=dress_id)
    return render(request, 'dresses/dress_card.html', {'dress': dress})


@login_required(login_url='login')
def create_dress(request):
    dress_form = DressForm(request.POST or None, files=request.FILES or None)
    if dress_form.is_valid():
        dress_form.save()
        return redirect('index')
    return render(
        request,
        'dresses/create_edit_dress.html',
        {
            'dress_form': dress_form,
        })


@login_required(login_url='login')
def edit_dress(request, id_dress):
    dress = get_object_or_404(Dress, id=id_dress)
    dress_form = DressForm(
        request.POST or None,
        files=request.FILES or None,
        instance=dress
    )
    if dress_form.is_valid():
        dress_form.save()
        return redirect('index')
    return render(
        request,
        'dresses/create_edit_dress.html',
        {
            'dress_form': dress_form,
        })


@login_required(login_url='login')
def delete_dress(request, id_dress):
    get_object_or_404(Dress, id=id_dress).delete()
    return redirect('index')
