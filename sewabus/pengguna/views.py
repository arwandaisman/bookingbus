from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib import messages
from .forms import BusForm
from .models import DataBus
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect



def edit(request,id):
    if request.POST:
        models.DataBus.objects.filter(pk=id).update(
        judul=request.POST['judul'],
        # jumlah=request.POST['jumlah'],
        # harga=request.POST['harga'],
        # produksi=request.POST['produksi'],
        # exp=request.POST['exp'],  
        )
        return redirect('index')
    tampil = models.DataBus.objects.filter(pk=id).first()
    return render(request, 'pengguna/edit.html',
    { 'data' : tampil,
    })



# # Create your views here.
# def Bus (request): 
  
#     if request.method == 'GET': 
  
#         # getting all the objects of hotel. 
#         Hotels = Hotel.objects.all()  
#         return render((request, 'display_hotel_images.html', 
#                      {'hotel_images' : Hotels})) 

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
		
# def user(request):
   
#     return render(request, 'pengguna/user.html')

def tabel (request):
   
    return render(request, 'pengguna/tabel.html')

def icon (request):
   
    return render(request, 'pengguna/icon.html')


def typo (request):
   
    return render(request, 'pengguna/typo.html')

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
    # context = {} 
    # context['form'] = BusForm 
    # return render( request, "pengguna/user.html", context) 

def hapus(request, id):
    konteks = {}
    tampil = models.DataBus.objects.filter(pk=id).delete()
    return redirect('index')