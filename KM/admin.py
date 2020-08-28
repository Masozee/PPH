import csv
from django.contrib import admin
from .models import *
from django.http import HttpResponse
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class StaffAdmin (admin.ModelAdmin):
    ordering = ['nama']
    list_display = ['nama','hp', 'Tempat_Lahir', 'Tanggal_Lahir', 'is_active', 'is_staff']
    list_filter = ()
    search_fields = ["nama" ]
    list_per_page = 25
admin.site.register(Staff, StaffAdmin)


class PublikasiAdmin (admin.ModelAdmin, ExportCsvMixin):
    ordering = ['judul']
    list_display = ['judul', 'kategori', 'date_upload']
    list_filter = ([('date_upload', DateRangeFilter),'kategori'])
    search_fields = ['judul' ]
    list_per_page = 25
    actions = ["export_as_csv"]
admin.site.register(Publikasi, PublikasiAdmin)

class InventoryAdmin (admin.ModelAdmin):
    ordering = ['kategori']
    list_display = ['jenis_barang', 'kategori', 'tahun_pembelian']
    list_filter = ()
    search_fields = ['jenis_barang' ]
    list_per_page = 25

admin.site.register(Inventaris, InventoryAdmin)


class KontakAdmin (admin.ModelAdmin, ExportCsvMixin):
    ordering = ['nama_organisasi']
    list_display = ['Kontak','nama_organisasi','kategori_kontak','email', 'no_hp', 'no_telp']
    list_filter = ()
    search_fields = ["nama_organisasi" ]
    list_per_page = 25
    actions = ["export_as_csv"]
admin.site.register(Kontak_PPH, KontakAdmin)

class PenelitianAdmin (admin.ModelAdmin, ExportCsvMixin):
    ordering = ['nama_kegiatan']
    list_display = ['nama_kegiatan','kategori','mulai','selesai', 'status']
    list_filter = (['kategori', 'status'])
    search_fields = ["nama_kegiatan" ]
    list_per_page = 25
    actions = ["export_as_csv"]
admin.site.register(Penelitian, PenelitianAdmin)

class DokuPenAdmin (admin.ModelAdmin, ExportCsvMixin):
    ordering = ['penelitian']
    list_display = ['Judul','penelitian','Kategori']
    list_filter = (['penelitian'])
    search_fields = ["Judul" ]
    list_per_page = 25
    actions = ["export_as_csv"]
admin.site.register(DokumenPenelitian, DokuPenAdmin)

class kapasitasAdmin (admin.ModelAdmin, ExportCsvMixin):
    ordering = ['judul']
    list_display = ['judul','kategori','jenis', 'mulai', 'selesai', 'penyelenggara']
    list_filter = ()
    search_fields = ["judul" ]
    list_per_page = 25
    actions = ["export_as_csv"]
admin.site.register(PeningkatanKapasitas, kapasitasAdmin)

class DokPeneAdmin (admin.ModelAdmin, ExportCsvMixin):
    ordering = ['Judul']
    list_display = ['Judul','kategori']
    list_filter = ()
    search_fields = ["Judul" ]
    list_per_page = 25
    actions = ["export_as_csv"]
admin.site.register(DokumenPeningkatan, DokPeneAdmin)

class MedAdvAdmin (admin.ModelAdmin, ExportCsvMixin):
    ordering = ['judul']
    list_display = ['judul','kategori', 'sumber', 'tahun']
    list_filter = (['kategori'])
    search_fields = ["judul" ]
    list_per_page = 25
    actions = ["export_as_csv"]
admin.site.register(MediaAdvokasi, MedAdvAdmin)

class ManajemenAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = ['judul','kategori','tahun']
    list_filter = (['kategori'])
    search_fields = ["judul" ]
    list_per_page = 25
admin.site.register(Manajemen, ManajemenAdmin)

class PubStaffAdmin (admin.ModelAdmin, ExportCsvMixin):
    ordering = ['judul']
    list_display = ['judul','kategori','peserta', 'kategori', 'peran', 'tingkat']
    list_filter = (['kategori'])
    search_fields = ["judul" ]
    list_per_page = 25
    actions = ["export_as_csv"]
admin.site.register(Publikasi_staff, PubStaffAdmin)

admin.site.register(Kepakaran)
admin.site.register(Posisi)
admin.site.register(Peminatan)
admin.site.register(Jabatan)

class PenKapStaffAdmin (admin.ModelAdmin, ExportCsvMixin):
    ordering = ['judul']
    list_display = ['judul','kategori','peserta', 'mulai', 'selesai', 'penyelenggara']
    list_filter = (['kategori'])
    search_fields = ["judul" ]
    list_per_page = 25
    actions = ["export_as_csv"]
admin.site.register(PeningkatanKapasitasstaff, PenKapStaffAdmin)

admin.site.register(PersonalEvent)