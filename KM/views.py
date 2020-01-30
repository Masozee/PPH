
from django.shortcuts import render, Http404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import modelformset_factory
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from USER.decorators import staff_required
from .filters import *

from taggit.models import Tag, TaggedItem

import json
import requests

from KM.models import *
from WEB.models import *


# Create your views here.
class homepage():
    pass

@staff_required
def inventaris(request):
    inventory = Inventaris.objects.all()
    
    context = {
        "inventory": inventory,
    }
    return render(request, "km/inventaris.html", context)

@staff_required
def stafflist(request):
    staff = Staff.objects.filter(is_active=True, is_staff=True)
    kepakaran = Kepakaran.objects.all()
    peminatan = Peminatan.objects.all()
    
    context = {
        "staff": staff,
        "pkr": kepakaran,
        "mnt": peminatan,
    }
    return render(request, "km/staff.html", context)

@staff_required
def staffDetail(request, staff_slug):
    staff = Staff.objects.get(slug=staff_slug)
    penelitian = Penelitian.objects.filter(tim__id=staff.id)
    kapasitas  = PeningkatanKapasitas.objects.filter(pembicara__id=staff.id, jenis='Non PPH')
    publikasi = Publikasi_staff.objects.filter(penulis__id=staff.id)

    context = {
        "staff": staff,
        "penelitian": penelitian,
        "kapasitas": kapasitas,
        "publikasi": publikasi,
    }
    return render(request, 'km/detail-staff.html', context)


@staff_required
class evaluasi():
    pass


@staff_required
class lapor():
    pass


@staff_required
def profilpenelitian(request):
    penelitian = Penelitian.objects.all()
    dokumen = DokumenPenelitian.objects.all()
    donor = Donor.objects.all()

    context = {
        "penelitian": penelitian,
        "dokumen": dokumen,
        "donor" : donor,
    }
    return render(request, "km/penelitian.html", context)


@staff_required
def PenelitianDetail(request, penelitian_slug):
    A = Penelitian.objects.get(slug=penelitian_slug)
    Dokumen = DokumenPenelitian.objects.filter(penelitian__id=A.id)
    context = {
        "A": A,
        "Dokumen": Dokumen,
    }
    return render(request, 'km/profil-penelitian.html', context)


@staff_required
def profilpeningkatan(request):
    peningkatan = PeningkatanKapasitas.objects.filter(jenis='PPH UNIKA Atma Jaya')
    dokumen = DokumenPeningkatan.objects.all()
    donor = Donor.objects.all()

    context = {
        "peningkatan": peningkatan,
        "dokumen": dokumen,
        "donor" : donor,
    }
    return render(request, "km/peningkatan-kapasitas.html", context)


@staff_required
def PeningkatanDetail(request, peningkatanKapasitas_slug):
    A = PeningkatanKapasitas.objects.get(slug=peningkatanKapasitas_slug)
    Dokumen = DokumenPeningkatan.objects.filter(Judul__id=A.id)
    context = {
        "B": A,
        "Dokumen": Dokumen,
    }
    return render(request, 'km/profil-peningkatan.html', context)


@staff_required
def media(request):
    Media = MediaAdvokasi.objects.all()
    context = {
        "A": Media,
    }
    return render(request, "km/media.html", context)


@staff_required
def manajemen(request):
    manajemen = Manajemen.objects.all()
    context = {
        "A": manajemen
    }
    return render(request, "km/manajemen.html", context)


@staff_required
class kegiatan():
    pass

@login_required(login_url='/users/login/')
def kontak(request):
    Kntk = Kontak_PPH.objects.all()

    context = {
        "kontak": Kntk,
    }
    return render(request, "km/kontak.html", context)

@login_required(login_url='/users/login/')
def kalender(request):
    return render(request, "km/kalender.html")


@staff_required
class ProfilPenelitian(DetailView):
    context_object_name = 'A'
    model = Penelitian
    template_name = "km/profil-penelitian.html"

    def get_context_data(self, **kwargs):
        context = super(ProfilPenelitian, self).get_context_data(**kwargs)
        context['Dokumen'] = DokumenPenelitian.objects.all()
        return context

@staff_required
def PenelitianDetail(request, penelitian_slug):
    A = Penelitian.objects.get(slug=penelitian_slug)
    Dokumen = DokumenPenelitian.objects.filter(penelitian__id=A.id)
    context = {
        "A": A,
        "Dokumen": Dokumen,
    }
    return render(request, 'km/profil-penelitian.html', context)


def evaluasi(request):
    return render(request, "km/evaluasi.html")

def evaluasikapasitas(request):
    return render(request, "km/evaluasi-kapasitas.html")

def pelaporan(request):
    return render(request, "km/pelaporan-staff.html")

def pelaporanorg(request):
    return render(request, "km/pelaporan-organisasi.html")