from django.forms import ModelForm
from .models import Faculty
from django import forms

class CreatePollForm(ModelForm):
    class Meta:
        model=Faculty
        fields=['question','option_one','option_two','option_three','option_four','option_five','option_six','option_seven','option_eight','option_nine','option_ten']
