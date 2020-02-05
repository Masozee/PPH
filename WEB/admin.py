from django.contrib import admin
from .models import *

# Register your models here.
class BeritaAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = ['Kategori','Agenda', 'judul', 'penulis', 'dibuat', 'dirubah']
    list_filter = (['Kategori', 'Agenda'])
    search_fields = ["judul", "Agenda" ]
    list_per_page = 25

admin.site.register(Berita, BeritaAdmin)

admin.site.register(TentangKami)


class AcaraAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = [ 'judul','Agenda', 'lokasi', 'dibuat', 'dirubah']
    list_filter = (['Agenda'])
    search_fields = ["judul" ]
    list_per_page = 25
admin.site.register(Acara, AcaraAdmin)




admin.site.register(HomeSLide)

class KontakAdmin (admin.ModelAdmin):
    ordering = ['nama_kntk']
    list_display = ['nama_kntk', 'email_kntk', 'telp_kntk', 'org_kntk', 'is_answered']
    list_filter = ()
    search_fields = ["nama_kntk" ]
    list_per_page = 25
admin.site.register(Kontak, KontakAdmin)

admin.site.register(Donor)
admin.site.register(Signup)

