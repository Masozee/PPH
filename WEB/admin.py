from django.contrib import admin
from .models import *

# Register your models here.
class BeritaAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = ['Kategori','Agenda', 'judul', 'penulis', 'dibuat', 'dirubah']
    list_filter = ()
    search_fields = ["judul", "Agenda" ]
    list_per_page = 25

admin.site.register(Berita, BeritaAdmin)

admin.site.register(TentangKami)


class AcaraAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = ['Agenda', 'judul', 'lokasi', 'dibuat', 'dirubah']
    list_filter = ()
    search_fields = ["judul" ]
    list_per_page = 25
admin.site.register(Acara, AcaraAdmin)




admin.site.register(HomeSLide)
admin.site.register(Kontak)
admin.site.register(Donor)
admin.site.register(downloadForm)
admin.site.register(Signup)

