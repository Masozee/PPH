from django.contrib import admin
from .models import *

class StaffAdmin (admin.ModelAdmin):
    ordering = ['nama']
    list_display = ['nama','hp', 'Tempat_Lahir', 'Tanggal_Lahir', 'is_active', 'is_staff']
    list_filter = ()
    search_fields = ["nama" ]
    list_per_page = 25
admin.site.register(Staff, StaffAdmin)


class PublikasiAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = ['judul', 'kategori', 'date_upload']
    list_filter = ()
    search_fields = ['judul' ]
    list_per_page = 25
admin.site.register(Publikasi, PublikasiAdmin)

class InventoryAdmin (admin.ModelAdmin):
    ordering = ['kategori']
    list_display = ['jenis_barang', 'kategori', 'tahun_pembelian']
    list_filter = ()
    search_fields = ['jenis_barang' ]
    list_per_page = 25
admin.site.register(Inventaris, InventoryAdmin)


admin.site.register(Kontak_PPH)
admin.site.register(Penelitian)
admin.site.register(DokumenPenelitian)
admin.site.register(PeningkatanKapasitas)
admin.site.register(DokumenPeningkatan)
admin.site.register(MediaAdvokasi)
admin.site.register(Manajemen)
admin.site.register(Publikasi_staff)
admin.site.register(Kepakaran)
admin.site.register(Posisi)
admin.site.register(Peminatan)
admin.site.register(Jabatan)
admin.site.register(PeningkatanKapasitasstaff)