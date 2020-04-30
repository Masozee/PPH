# users/admin.py
import csv
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from .forms import *
from .models import CustomUser, Visitor


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


class CustomUserAdmin(admin.ModelAdmin, ExportCsvMixin):
    ordering = ['username']
    list_display = ['username','first_name','last_name','email','is_staff', ]
    exclude = ('password',)
    list_filter = (
        ['is_staff']
    )
    search_fields = ["username", "organisasi"]
    list_per_page = 25
    actions = ["export_as_csv"]
admin.site.register(CustomUser, CustomUserAdmin)
