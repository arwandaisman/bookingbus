from django.shortcuts import render
from django.shortcuts import render, redirect
from . import models
# from manga.form import FormManga
from django.contrib import messages
# import base64
# import io
# from PIL import Image
from .forms import BusForm
from .models import DataBus
from django.http import HttpResponse, HttpResponsePermanentRedirect

# Create your views here.
def Bus (request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Hotels = Hotel.objects.all()  
        return render((request, 'display_hotel_images.html', 
                     {'hotel_images' : Hotels})) 

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
    tampil = models.DataBus.objects.filter(pk=id).delete()
    return redirect('index')


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