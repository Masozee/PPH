from django import forms
from .models import *

class PeningkatanKapasitasForm(forms.ModelForm):

    class Meta:
        model = PeningkatanKapasitas_staff
        fields = ('kategori','judul', 'mulai', 'selesai', 'lokasi', 'pembicara','penyelenggara', 'laporan_kegiatan', 'materi' )

