from django.contrib.sessions.models import Session
from django.db.models import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from dresses.models import Basket


def count(request):
    amount = 0
    try:
        if request.user.is_authenticated:
            basket = Basket.objects.get(user=request.user)
        else:
            request.session.save()
            session = get_object_or_404(Session, pk=request.session.session_key)
            basket = Basket.objects.get(session=session)
        if basket:
            amount = basket.dress.all().count()
        return {'count': amount}
    except ObjectDoesNotExist:
        return {'count': amount}
