from django.forms import ModelForm
from django import forms
from .models import NewUser,ActivityPeriod

class NewUserForm(forms.ModelForm):
 
    class Meta:
        model = NewUser
        fields = ("real_name","tz")
class ActivityPeriodForm(forms.ModelForm):
    start_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
                widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
        , required=False)
    end_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
                widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        })
        , required=False)
    class Meta:
        model = ActivityPeriod
        fields = ("user","start_time","end_time")
