
from django.shortcuts import render, redirect 
from .forms import *
from django import forms
from .models import DataBus
  
# Create your views here. 
# def Bus(request): 
  
#     if request.method == 'POST': 
#         form = HotelForm(request.POST, request.FILES) 
  
#         if form.is_valid(): 
#             form.save() 
#             return redirect('success') 
#     else: 
#         form = HotelForm() 
#     return render(request, 'hotel_image_form.html', {'form' : form}) 
  
  
# def success(request): 
#     return HttpResponse('successfully uploaded')


# class PostFormBus(forms.Form):
#     nama_bus = forms.CharField(max_length=20)
#     merk_bus = forms.CharField(max_length=20)
#     bus_tersedia = forms.IntegerField()
#     tanggal_pembuatan = forms.DateField(
#         widget = forms.SelectDateWidget(
#             years=range(1945,2040,1),
#         )
#     )
#     kategori = forms.ChoiceField(
#         choices= [
#             ('Kecil','kecil'),
#             ('Sedang','Sedang'),
#             ('Besar', 'besar'),
#         ]
#     )
    # nomor_plat = forms.CharField(max_length=10)
    # jml_kursi = forms.IntegerField()
    # keterangan = forms.CharField(
    #     widget = forms.Textarea
    # )


# class BusForm(forms.Form): 
#     Judul = forms.CharField(max_length = 100)
#     Merk_Seri_Bus =  forms.CharField(max_length = 100)
#     Tahun_Pembuatan =  forms.DateField(
#         widget= forms.SelectDateWidget(
#             years=range(1945,2201,1),
#         )
#     )
#     No_Plat = forms.CharField(max_length = 15)
#     Pilih_Kategori = forms.ChoiceField(
#         choices=[
#             ('kecil','Bus Kecil'),
#             ('sedang','Bus Medium'),
#             ('besar','Bus Besar'),
#         ]
#     )
#     Jumlah_Kursi = forms.IntegerField()
#     AC = forms.BooleanField()
#     DVD = forms.BooleanField()
#     Toilet = forms.BooleanField()
#     Stop_Kontak = forms.BooleanField()
#     Sabuk_Pengaman = forms.BooleanField()
#     Bagasi = forms.BooleanField()
#     WIFI = forms.BooleanField()
#     TV = forms.BooleanField()
#     Bantal = forms.BooleanField()
#     Selimut = forms.BooleanField()
#     Smoking_Area = forms.BooleanField()
#     gambar = forms.ImageField()
#     Tambahan = forms.CharField(
#         widget = forms.Textarea
#     ) 

class BusForm(forms.ModelForm): 
    class Meta: 
        model = DataBus 
        fields = "__all__"

        # widgets = {
        #     'judul' : forms.TextInput({'class':'form-control'}),
        #     'merk_seri_bus' : forms.TextInput({'class':'form-control'}),
        #     'tahun_pembuatan' : forms.NumberInput({'class':'form-control'}),
        #     'no_plat' : forms.TextInput({'class':'form-control'}),
        #     'kategori' : forms.Select({'class':'form-control'}),
            
        # }