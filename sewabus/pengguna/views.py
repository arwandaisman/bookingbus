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
    
    tampil = models.DataBus.objects.filter(po_id=request.user)
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
    # x = id
    # if request.POST:
    #     DataBus.objects.create(
    #         po_id = request.POST['po_id'],)
    # pof = DataBus.objects.all()
    # return render(request,'pengguna/user.html',{'pof' : pof,})
    tasks = DataBus.objects.filter(po_id=request.user)
    form = BusForm()
    if request.POST:
        form = BusForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.instance
            form.instance.po_id = request.user
            form.save()
            messages.success(request, 'Data telah ditambahkan.')
        return redirect('user')
        
    return render(request, 'pengguna/user.html',{
        'form': form,
        'data': tasks,
    })

    # form = BusForm(request.POST)
    # if form.is_valid():
    #     form.save()
    #     form = BusForm()
            
    #     konteks = {
    #     }
    #     return render(request, 'pengguna/user.html', konteks)
    # else:
    #     form = BusForm()
    #     konteks = {
    #             'form' : form,
    #         }
    
    #     return render(request, 'pengguna/user.html', konteks)

    

# def po(request):
#     x = id
#     if request.POST:
#         DataBus.objects.create(
#             po_id = request.POST['po_id'],)
#     pof = DataBus.objects.all()
#     return render(request,'pengguna/user.html',{'pof' : pof,})
    
#     pof= PoForm(request.POST)
#     if pof.is_valid():
#         pof.save()
#         pof = PoForm()
            
#         konteks = {
#             'pof' : pof,
#         }
#         return render(request,'pengguna/user.html', konteks)
#     else:
#         pof = PoForm()
#         konteks = {
#                 'pof' : pof,
#             }
    
#         return render(request, 'pengguna/user.html', konteks)

    # x = id
    # if request.POST:
    #     DataBus.objects.create(
    #         judul = request.POST['judul'],
    #         merk_seri_bus =  request.POST['merk_seri_bus'],
    #         tahun_pembuatan =  request.POST['tahun_pembuatan'],
    #         no_plat = request.POST['no_plat'],
    #         kategori = request.POST['kategori'],
    #         harga = request.POST['harga'],
    #         jml_kursi = request.POST['jml_kursi'],
    #         jml_bus= request.POST['jml_bus'],
    #         ac = request.POST['ac'],
    #         dvd = request.POST['dvd'],
    #         toilet = request.POST['toilet'],
    #         stop_kontak = request.POST['stop_kontak'],
    #         sabuk_pengaman = request.POST['sabuk_pengaman'],
    #         bagasi = request.POST['bagasi'],
    #         wifi = request.POST['wifi'],
    #         tv = request.POST['tv'],
    #         bantal = request.POST['bantal'],
    #         selimut = request.POST['selimut'],
    #         smoking_area = request.POST['smoking_area'],
    #         img = request.POST['img'],
    #         tambahan = request.POST['tambahan'],
    #         po_id = x
    #     )
    #     return redirect('home')
    # form = DataBus.objects.all()
    # return render(request,'pengguna/user.html',{'form' : form,})

    # if request.POST:
    #     DataBus.objects.create(
    #     po_id=request.user.id,
        
    #     )
    #     return redirect('index')
    # task = models.daftar.objects.all()
    # return render(request, 'tambah.html',
    # { 'data' : task,
    # })
    # if request.method == 'POST':
    #     d=DataBus.object.filter(pk=request.user.id)
        
        
        
        
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
