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


class KontakAdmin (admin.ModelAdmin):
    ordering = ['nama_organisasi']
    list_display = ['Kontak','nama_organisasi','kategori_kontak','email', 'no_hp', 'no_telp']
    list_filter = ()
    search_fields = ["nama_organisasi" ]
    list_per_page = 25
admin.site.register(Kontak_PPH, KontakAdmin)

class PenelitianAdmin (admin.ModelAdmin):
    ordering = ['nama_kegiatan']
    list_display = ['nama_kegiatan','kategori','mulai','selesai', 'status']
    list_filter = (['kategori', 'status'])
    search_fields = ["nama_kegiatan" ]
    list_per_page = 25
admin.site.register(Penelitian, PenelitianAdmin)

class DokuPenAdmin (admin.ModelAdmin):
    ordering = ['penelitian']
    list_display = ['Judul','penelitian','Kategori']
    list_filter = (['penelitian'])
    search_fields = ["Judul" ]
    list_per_page = 25
admin.site.register(DokumenPenelitian, DokuPenAdmin)

class kapasitasAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = ['judul','kategori','jenis', 'mulai', 'selesai', 'penyelenggara']
    list_filter = ()
    search_fields = ["judul" ]
    list_per_page = 25
admin.site.register(PeningkatanKapasitas, kapasitasAdmin)

class DokPeneAdmin (admin.ModelAdmin):
    ordering = ['Judul']
    list_display = ['Judul','kategori']
    list_filter = ()
    search_fields = ["Judul" ]
    list_per_page = 25
admin.site.register(DokumenPeningkatan, DokPeneAdmin)

class MedAdvAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = ['judul','kategori', 'sumber', 'tahun']
    list_filter = (['kategori'])
    search_fields = ["judul" ]
    list_per_page = 25
admin.site.register(MediaAdvokasi, MedAdvAdmin)

class ManajemenAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = ['judul','kategori','tahun']
    list_filter = (['kategori'])
    search_fields = ["judul" ]
    list_per_page = 25
admin.site.register(Manajemen, ManajemenAdmin)

class PubStaffAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = ['judul','kategori','peserta', 'kategori', 'peran', 'tingkat']
    list_filter = (['kategori'])
    search_fields = ["judul" ]
    list_per_page = 25
admin.site.register(Publikasi_staff, PubStaffAdmin)

admin.site.register(Kepakaran)
admin.site.register(Posisi)
admin.site.register(Peminatan)
admin.site.register(Jabatan)

class PenKapStaffAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = ['judul','kategori','peserta', 'mulai', 'selesai', 'penyelenggara']
    list_filter = (['kategori'])
    search_fields = ["judul" ]
    list_per_page = 25
admin.site.register(PeningkatanKapasitasstaff, PenKapStaffAdmin)

