from django import template
from django.db.models import ObjectDoesNotExist

from dresses.models import Basket

register = template.Library()


@register.filter
def tranc_name(name):
    new_name = name.lower()[:4]
    return new_name


@register.filter
def dress_in_basket(request, dress):
    try:
        if request.user.is_active:
            basket = Basket.objects.get(user=request.user)
        else:
            basket = Basket.objects.get(session=request.session.session_key)
        dresses = basket.dress.all()
        if dresses.filter(id=dress.id).exists():
            return True
    except ObjectDoesNotExist:
        return False
    return False
