from django import forms
from django.forms import ModelForm
from .models import *


class PeningkatanForm(ModelForm):

    class Meta:
        model = PeningkatanKapasitasstaff
        fields = ['kategori','judul', 'mulai', 'selesai', 'lokasi', 'pembicara','penyelenggara', 'laporan_kegiatan', 'materi']


class PenelitianForm(ModelForm):

    class Meta:
        model = Publikasi_staff
        fields = ['tahun','judul', 'penulis', 'kategori', 'peran', 'tingkat','link']

