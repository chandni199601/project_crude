from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from webApp import forms

# Create your views here.
def EmpView(request):
    #form=forms.EmpForm()
    if request.method=='POST':
        form=forms.EmpForm(request.POST)
        if form.is_valid():
            print("validation is success")
            print(form.cleaned_data['Name'])
            print(form.cleaned_data['Salary'])
            print(form.cleaned_data['Bot_field'])
            return  HttpResponseRedirect('/thanks')
    else:
        form=forms.EmpForm()
    return  render(request,'myApp/welcome.html',  {'form':form})
def ThankuView(request):
    return render(request,'myApp/thanks.html')





