from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model): 
    name = models.CharField(max_length=50) 
    hotel_Main_Img = models.ImageField(upload_to='images/') 

# class Jenis(models.Model):
#     jenis = models.CharField(max_length = 10)

#     def __str__(self):
#         return self.jenis 


class DataBus(models.Model):
    jenis_bus = (
        ('kecil', 'Kecil'),
        ('medium', 'Medium'),
        ('besar', 'Besar'),
    )
    judul = models.CharField(max_length = 100,default=None)
    merk_seri_bus =  models.CharField(max_length = 100,default=None)
    tahun_pembuatan =  models.IntegerField(default=2015)
    no_plat = models.CharField(max_length = 15,default=None)
    # kategori = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)
    kategori = models.CharField(max_length=10, choices=jenis_bus,default=None, null=True)
    harga = models.IntegerField(default=100000)
    jml_kursi = models.IntegerField(default=None)
    jml_bus= models.IntegerField(default=None)
    ac = models.BooleanField("ac", default=False)
    dvd = models.BooleanField("DVD/Video", default=False)
    toilet = models.BooleanField("Toilet", default=False)
    stop_kontak = models.BooleanField("Stop Kontak", default=False)
    sabuk_pengaman = models.BooleanField("Sabuk Pengaman", default=False)
    bagasi = models.BooleanField("Bagasi", default=False)
    wifi = models.BooleanField("WIFI", default=False)
    tv = models.BooleanField("TV", default=False)
    bantal = models.BooleanField("Bantal", default=False)
    selimut = models.BooleanField("Selimut", default=False)
    smoking_area = models.BooleanField("Smoking Area", default=False)
    img = models.ImageField(upload_to='gambar/',blank=True)
    tambahan = models.TextField(default=None,null=True)
    # po_id = models.IntegerField(blank=True, null = True)
    po_id = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='po_id')
    # owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='mahasiswa')
   

    def __str__(self): 
        return self.judul 
    
    

# class GambarBus(models.Model):
#     gambar1 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar2 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar3 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar4 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar5 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar6 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar7 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar8 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar9 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar10 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar11 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar12 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar13 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar14 = models.ImageField(upload_to='static/image/',blank=True)
#     gambar15 = models.ImageField(upload_to='static/image/',blank=True)
    
#     def __str__(self): 
#         return self.gambar1
