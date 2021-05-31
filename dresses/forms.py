from django import forms

from .models import Dress


class DressForm(forms.ModelForm):
    class Meta:
        model = Dress
        fields = '__all__'
