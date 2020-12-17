from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BusForm
from .models import DataBus, Images
from django.forms import modelformset_factory


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
    image = models.Images.objects.all()
    data = {
        'data':tampil,
        'image' : image,
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
    # ImageFormSet = modelformset_factory(Images, fields = ('image',), extra=4)
    # if request.method == 'POST':
    #     form = BusForm(request.POST)
    #     formset = ImageFormSet(request.POST or None, request.FILES or None)
    #     if form.is_valid() and formset.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user
    #         post.save()

    #         for form in formset.cleaned_data:
    #             try:
    #                 images = form['image']
    #                 photo = Images(post=post, images=images)
    #                 photo.save()
    #             except print(0):
    #                 break

    # else:
    #     form = BusForm()
    #     formset = ImageFormSet(queryset=Images.objects.none())

    # context = {
    #     'form': form, 
    #     'formset': formset
    # }
    # return render(request, 'pengguna/user.html', context)

        
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
