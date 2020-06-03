from django import forms
from .models import Day

class DayCreateForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = '__all__' #('text','field','date)