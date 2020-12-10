from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('sewa/', include('sewa.urls')),
    path('pengguna/', include('pengguna.urls')),
    path('login/', LoginView.as_view(), name='masuk'),
    # path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('registration/', include('registration.urls')),

]
