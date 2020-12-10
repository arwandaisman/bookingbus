from django.shortcuts import render, redirect, get_object_or_404
from . import models
# from manga.form import FormManga
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BusForm
from .models import DataBus


# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def index (request):
    tampil = models.DataBus.objects.all()
    data = {
        'data':tampil,
    }   
    return render(request,'pengguna/index.html',data)  
    
def detail(request, id):
    tampil = models.DataBus.objects.filter(pk=id)
    data = {
        'data':tampil,
    }   
    return render(request,'pengguna/detail.html',data) 

def edit(request,id):
    context ={}
    obj = get_object_or_404(DataBus, id = id)
    form = BusForm(request.POST or None, instance = obj)
    if form.is_valid(): 
        form.save() 
        return redirect('index')
    context["form"] = form
    return render(request, "pengguna/edit.html", context)


def user(request): 
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            form = BusForm()
            
            konteks = {
                'form' : form,
            }
            return render(request, 'pengguna/user.html', konteks)
    else:
        form = BusForm()
        konteks = {
                'form' : form,
            }
        return render(request, 'pengguna/user.html', konteks)
        
        
def hapus(request, id):
    konteks = {}
    tampil = models.DataBus.objects.filter(pk=id).delete()
    return redirect('index')

def tabel (request):
   
    return render(request, 'pengguna/tabel.html')

def icon (request):
   
    return render(request, 'pengguna/icon.html')


def typo (request):
   
    return render(request, 'pengguna/typo.html')

# PENGAJAR

# def tampilguru(request):
#     if request.POST:
#         models.pengajar.objects.all()
        
#     ptampil = models.pengajar.objects.all()
#     return render(request, 'pengajar.html',
# 		{ 'data': ptampil,
# 		})

# def detailguru(request, id):
# 	gdetail = models.pengajar.objects.filter(pk=id).first()
# 	return render(request, 'detailpengajar.html',
# 		{ 'data': gdetail,
# 		})

# # MURID

# def tampilmurid(request):
#     if request.POST:
#         models.murid.objects.all()
        
#     mtampil = models.murid.objects.all()
#     return render(request, 'murid.html',
# 		{ 'data': mtampil,
# 		})

# def detailmurid(request, id):
# 	mdetail = models.murid.objects.filter(pk=id).first()
# 	return render(request, 'detailmurid.html',
# 		{ 'data': mdetail,
# 		})
