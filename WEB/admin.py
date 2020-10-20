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

# Register your models here.
class BeritaAdmin (admin.ModelAdmin):
    ordering = ['judul']
    list_display = ['Kategori','Agenda', 'judul', 'penulis', 'dibuat', 'dirubah']
    list_filter = (['Kategori', 'Agenda'])
    search_fields = ["judul", "Agenda" ]
    list_per_page = 25

admin.site.register(Berita, BeritaAdmin)

admin.site.register(TentangKami)


class AcaraAdmin (admin.ModelAdmin, ExportCsvMixin):
    ordering = ['judul']
    list_display = [ 'judul','Agenda', 'lokasi', 'waktu_mulai', 'waktu_selesai']
    list_filter = (['Agenda', ('waktu_mulai', DateRangeFilter)])
    search_fields = ["judul" ]
    list_per_page = 25
    actions = ["export_as_csv"]
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

class DownloadAdmin (admin.ModelAdmin, ExportCsvMixin):
    ordering = ['-date_created']
    list_display = ['nama', 'email','dokumen', 'organisasi', 'date_created',]
    list_filter = (
        [('date_created', DateRangeFilter)]
    )
    search_fields = ["dokumen"]
    list_per_page = 25
    actions = ["export_as_csv"]

admin.site.register(downloadForm, DownloadAdmin)

admin.site.register(AnotatedCOP)

class LaKesWa(admin.ModelAdmin, ExportCsvMixin):
    ordering = ['-nama']
    list_display = ['nama','provinsi','kota','kategori', 'alamat', 'telpon',]
    search_fields = ["nama", "kota"]
    list_per_page = 25
    actions = ["export_as_csv"]

admin.site.register(LayananKeswa, LaKesWa)