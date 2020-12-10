from django.contrib import admin
# from pengelola import models

# Register your models here.
# admin.site.register(models.murid)
# admin.site.register(models.pengajar)
# admin.site.register(models.KtgAmpu)

from pengguna.models import DataBus
# from pengguna.models import DataBus, Jenis
# admin.site.register(DataBus)



class AdminBus(admin.ModelAdmin):
    list_display = ['judul','merk_seri_bus', 'no_plat', 'kategori','jml_kursi']
    search_fields = ['judul','merk_seri_bus']
    # list_filter = ('jml_kursi')
    # list_per_page = 4

admin.site.register(DataBus, AdminBus)
# admin.site.register(Jenis)




# from datawisata.models import Datawisata,Jenis

# class WisataAdmin(admin.ModelAdmin):
#     list_display = ['nama_wisata','kabupaten','jml_pengunjung', 'lokasi', 'jenis_id']
#     search_fields = ['nama_wisata','kabupaten']
#     list_filter = ('kabupaten','jenis_id')
#     list_per_page = 4

# admin.site.register(Datawisata, WisataAdmin)
# admin.site.register(Jenis)