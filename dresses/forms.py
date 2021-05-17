from django import forms

from .models import Dress, ImagesDress


class DressForm(forms.ModelForm):
    class Meta:
        model = Dress
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImagesDress
        fields = ('image',)
