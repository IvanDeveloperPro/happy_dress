from django import forms

from .models import Basket, Dress


class DressForm(forms.ModelForm):
    class Meta:
        model = Dress
        fields = '__all__'


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['rent_date']

    def clean_rent_date(self):
        date = self.cleaned_data['rent_date']
        if not date:
            raise forms.ValidationError('Не указана дата')
        return date
