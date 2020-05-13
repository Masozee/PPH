from django import forms
from django.forms import ModelForm
from .models import *


class PeningkatanForm(ModelForm):
    judul = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={
                'placeholder': 'Judul materi Peningkatan kapasitas yang anda ikuti'
            }
        )
    )
    mulai = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={'class': 'datepicker-here', 'placeholder': '01/01/2020', 'data-language': "en"}),

    )
    selesai = forms.DateField(
        widget=forms.DateInput(
            format='%d/%m/%Y', attrs={'class': 'datepicker-here', 'placeholder': '01/01/2020', 'data-language': "en"}),
        input_formats=('%d/%m/%Y',)
    )

    class Meta:
        model = PeningkatanKapasitasstaff
        fields = ['kategori','judul', 'mulai', 'selesai', 'lokasi', 'pembicara','penyelenggara', 'laporan_kegiatan', 'materi']


class PenelitianForm(ModelForm):
    judul = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={
            'placeholder': 'Judul materi penelitian yang anda lakukan'
            }
        )
    )
    tahun = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={'class': 'datepicker-here', 'placeholder': '01/01/2020', 'data-language': "en"}),

    )


    class Meta:
        model = Publikasi_staff
        fields = ['tahun','judul', 'kategori', 'peran', 'tingkat','link']


class PersonalEventForm(ModelForm):
    acara = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={
            'placeholder': 'Judul materi penelitian yang anda lakukan'
        }
    )
                            )
    mulai = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={'class': 'datepicker-here', 'placeholder': '01/01/2020', 'data-language': "en"}),

    )

    selesai = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={'class': 'datepicker-here', 'placeholder': '01/01/2020', 'data-language': "en"}),

    )
    class Meta:
        model = PersonalEvent
        fields = ['acara','mulai', 'selesai', 'keterangan',]