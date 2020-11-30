from django.shortcuts import render
from django.shortcuts import render, redirect
from . import models
# from manga.form import FormManga
from django.contrib import messages

# Create your views here.
def Bus (request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Hotels = Hotel.objects.all()  
        return render((request, 'display_hotel_images.html', 
                     {'hotel_images' : Hotels})) 

def index (request):
    return render(request, 'pengguna/index.html')

def user(request):
   
    return render(request, 'pengguna/user.html')

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