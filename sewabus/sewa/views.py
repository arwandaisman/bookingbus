from django.shortcuts import render
from . import models
from pengguna.models import Jenis, DataBus

def index(req):
    # task = models.Pasien.objects.all()
    # return render(req, 'sewa/index.html')

    tampil = DataBus.objects.all()
    data = {
        'data':tampil,
    }   
    return render(req,'sewa/index.html',data) 


def detail(req):
    tampil = DataBus.objects.all()
    data = {
        'data':tampil,
    }   

    return render(req, 'sewa/detail.html',data)

def biasa(req):
    # if req.POST:
    #     models.Pasien.objects.create(
    #     # no_pasien=req.POST['no_pasien'],
    #     nama_pasien=req.POST['nama_pasien'],
    #     ttl=req.POST['ttl'],
    #     jenis_kelamin=req.POST['jenis_kelamin'],
    #     golongan_darah=req.POST['golongan_darah'],
    #     alamat_pasien=req.POST['alamat_pasien'],
    #     no_hp=req.POST['no_hp'])

        # return redirect('sewa')
    # task = models.Pasien.objects.all()
    return render(req, 'sewa/biasa.html')

def rinci(req):
    # if req.POST:
    #     models.Pasien.objects.create(
    #     # no_pasien=req.POST['no_pasien'],
    #     nama_pasien=req.POST['nama_pasien'],
    #     ttl=req.POST['ttl'],
    #     jenis_kelamin=req.POST['jenis_kelamin'],
    #     golongan_darah=req.POST['golongan_darah'],
    #     alamat_pasien=req.POST['alamat_pasien'],
    #     no_hp=req.POST['no_hp'])

        # return redirect('sewa')
    # task = models.Pasien.objects.all()
    return render(req, 'sewa/rinci.html')
    