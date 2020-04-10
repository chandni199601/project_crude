from django import forms
from django.core import validators

class EmpForm(forms.Form):
    Name=forms.CharField()
    Salary=forms.IntegerField()
    Bot_field=forms.CharField(required=False,widget=forms.HiddenInput)


    def clean(self):
        cdata=super().clean()
        bhandle=cdata['Bot_field']
        if len(bhandle)>0:
            raise forms.validationError("welcome your Bot,your data unable to process")



