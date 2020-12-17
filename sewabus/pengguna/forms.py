
from django.shortcuts import render, redirect 
from .forms import *
from django import forms
from .models import DataBus
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
  
class BusForm(forms.ModelForm): 
   
    class Meta: 
        model = DataBus 
        exclude = ['po_id']
        # fields = "__all__"
