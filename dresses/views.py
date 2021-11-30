from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from .forms import BasketForm, DressForm
from .models import Basket, Dress, Order

User = get_user_model()


class DressListView(ListView):
    model = Dress
    template_name = 'dresses/dress_list.html'
    context_object_name = 'dresses'


class DressDetailView(DetailView):
    model = Dress
    template_name = 'dresses/dress_card.html'
    context_object_name = 'dress'


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


def basket_dress(request):
    if request.user.is_active:
        basket = get_object_or_404(Basket, user=request.user)
    else:
        basket = get_object_or_404(Basket, session=request.session.session_key)
    form_basket = BasketForm(request.POST or None)
    if form_basket.is_valid():
        basket.rent_date = form_basket.cleaned_data.get('rent_date')
        basket.save()
        return redirect('order', basket.id)
    if basket:
        return render(request, 'dresses/basket.html', {'basket': basket, 'form': form_basket})
    else:
        return render(request, 'dresses/basket.html', {'form': form_basket})


def add_dress_basket(request, id_dress):
    dress = get_object_or_404(Dress, id=id_dress)
    session = get_object_or_404(Session, pk=request.session.session_key)
    if request.user.is_active:
        basket, _ = Basket.objects.get_or_create(user=request.user)
    else:
        basket, _ = Basket.objects.get_or_create(session=session)
    basket.dress.add(dress)
    return redirect('index')


def basket_add(request, id_dress):
    if request.POST:
        dress = get_object_or_404(Dress, id=id_dress)
        session = get_object_or_404(Session, pk=request.session.session_key)
        if request.user.is_active:
            basket, _ = Basket.objects.get_or_create(user=request.user)
        else:
            basket, _ = Basket.objects.get_or_create(session=session)
        basket.dress.add(dress)
        return HttpResponse(data={'success': True})
    return HttpResponse(data={'success': False})


def delete_dress_basket(request, id_dress):
    dress = get_object_or_404(Dress, id=id_dress)
    session = get_object_or_404(Session, pk=request.session.session_key)
    if request.user.is_active:
        basket = Basket.objects.get(user=request.user)
    else:
        basket = Basket.objects.get(session=session)
    basket.dress.remove(dress)
    return redirect('index')


def basket_del(request, id_dress):
    if request.DELETE:
        dress = get_object_or_404(Dress, id=id_dress)
        session = get_object_or_404(Session, pk=request.session.session_key)
        if request.user.is_active:
            basket = Basket.objects.get(user=request.user)
        else:
            basket = Basket.objects.get(session=session)
        basket.dress.remove(dress)
        return HttpResponse(data={'success': True})
    return HttpResponse(data={'success': False})


def order(request, basket_id):
    basket = get_object_or_404(Basket, id=basket_id)
    dress = basket.dress.all()
    cost = basket.dress.aggregate(sum=Sum('price'))['sum']
    order = Order.objects.create(
        tenant=basket.user,
        rent_date=basket.rent_date,
        cost=cost
    )
    order.dress.add(*dress)
    basket.delete()
    return redirect('thanks')
