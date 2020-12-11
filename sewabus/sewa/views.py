from django.shortcuts import render
from . import models
from pengguna.models import DataBus

def index(req):
    # task = models.Pasien.objects.all()
    # return render(req, 'sewa/index.html')
    tampil = DataBus.objects.all()   
    return render(req,'sewa/index.html',{'tampil':tampil}) 


def detail(req, id):
    tampil = DataBus.objects.filter(pk=id)
    data = {
        'data':tampil,
    }   

    return render(req, 'sewa/detail.html',data)
def biasa(req):
    return render(req, 'sewa/biasa.html')

def rinci(req):
    return render(req, 'sewa/rinci.html')
    