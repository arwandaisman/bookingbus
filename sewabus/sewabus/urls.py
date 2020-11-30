from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('sewa/', include('sewa.urls')),
    path('pengguna/', include('pengguna.urls')),


]
