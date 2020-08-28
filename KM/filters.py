from .models import *
import django_filters

"""class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Staff
        fields = ['username', 'first_name', 'last_name', ]"""

class PublikasiFilter(django_filters.FilterSet):
    class Meta:
        model = Publikasi
        fields = ['project', 'tema' ]

class InventoryFilter(django_filters.FilterSet):
    class Meta:
        model = Inventaris
        fields = ['kategori']

class KontakFilter(django_filters.FilterSet):
    class Meta:
        model = Kontak_PPH
        fields = ['kategori_kontak']