import json
import urllib
#import requests
from datetime import datetime, timedelta, time
from django.db.models import F

from django.contrib.auth import authenticate, login


from django.shortcuts import render, Http404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import modelformset_factory
from django.views.generic import DetailView, ListView, TemplateView
from .forms import ContactForm, DownloadForm, EmailSignupForm
from django.views.generic.edit import FormMixin
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from USER.decorators import visitor_required, staff_required
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .multiforms import MultiFormsView
from USER.forms import VisitorSignUpForm


form2 = EmailSignupForm()

from .models import Berita, Acara, TentangKami, HomeSLide, Kontak, Signup, downloadForm, AnotatedCOP, LayananKeswa
from KM.models import *


# Create your views here.
def Home(request):
    Slide = HomeSLide.objects.all()
    berita = Berita.objects.filter(Kategori="Dokumentasi").order_by('-tanggal').distinct()[:4]
    artikel = Berita.objects.filter(Kategori="Artikel").order_by('-tanggal').distinct()[:1]

    context = {
        "Slide": Slide,
        "Berita": berita,
        "Acara": artikel,
        "form2": form2
    }

    return render(request, "web/index.html", context)

def WebSetting(request):
    setting = HomeSLide.objects.all()
    return render(request, "web/base.html", setting)

def Tentangkami(request):
    staff = Staff.objects.filter(is_active=True, is_staff=True)
    tentangkami = TentangKami.objects.all()
    header = HomeSLide.objects.all()

    context = {
        "staff": staff,
        "tentangkami": tentangkami,
        "header": header
    }

    return render(request, "web/tentang-kami.html", context)

def DokumentasiList(request):
    dokumentasi = Berita.objects.filter(Kategori="Dokumentasi").order_by('-tanggal')
    paginator = Paginator(dokumentasi, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        dokumentasi = paginator.page(page)
    except PageNotAnInteger:
        dokumentasi = paginator.page(1)
    except EmptyPage:
        dokumentasi = paginator.page(paginator.num_pages)
    context = {
        "berita": dokumentasi,
    }

    return render(request, "web/dukomentasi.html", context)

def DokumentasiPenelitian(request):
    dokumentasi = Berita.objects.filter(Kategori="Dokumentasi", Agenda="Penelitian").order_by('-tanggal')
    paginator = Paginator(dokumentasi, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        dokumentasi = paginator.page(page)
    except PageNotAnInteger:
        dokumentasi = paginator.page(1)
    except EmptyPage:
        dokumentasi = paginator.page(paginator.num_pages)
    context = {
        "berita": dokumentasi,
    }

    return render(request, "web/dukomentasi.html", context)
def DokumentasiAdvokasi(request):
    dokumentasi = Berita.objects.filter(Kategori="Dokumentasi", Agenda="Advokasi").order_by('-tanggal')
    paginator = Paginator(dokumentasi, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        dokumentasi = paginator.page(page)
    except PageNotAnInteger:
        dokumentasi = paginator.page(1)
    except EmptyPage:
        dokumentasi = paginator.page(paginator.num_pages)
    context = {
        "berita": dokumentasi,
    }

    return render(request, "web/dukomentasi.html", context)
def DokumentasiPeningkatan(request):
    dokumentasi = Berita.objects.filter(Kategori="Dokumentasi", Agenda="Peningkatan Kapasitas").order_by('-tanggal')
    paginator = Paginator(dokumentasi, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        dokumentasi = paginator.page(page)
    except PageNotAnInteger:
        dokumentasi = paginator.page(1)
    except EmptyPage:
        dokumentasi = paginator.page(paginator.num_pages)
    context = {
        "berita": dokumentasi,
    }

    return render(request, "web/dukomentasi.html", context)
def DokumentasiPelayanan(request):
    dokumentasi = Berita.objects.filter(Kategori="Dokumentasi", Agenda="Pelayanan Komunitas").order_by('-tanggal')
    paginator = Paginator(dokumentasi, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        dokumentasi = paginator.page(page)
    except PageNotAnInteger:
        dokumentasi = paginator.page(1)
    except EmptyPage:
        dokumentasi = paginator.page(paginator.num_pages)
    context = {
        "berita": dokumentasi,
    }

    return render(request, "web/dukomentasi.html", context)
class DokumentasiDetail(DetailView):
    model = Berita
    template_name = "web/detail-artikel.html"
    def get_context_data(self, **kwargs):
        context = super(DokumentasiDetail, self).get_context_data(**kwargs)
        context['related'] = Berita.tags.similar_objects().distinct()[:4]
        return context

def Dokumendetail(request, berita_slug):
    berita = Berita.objects.get(slug=berita_slug)
    Related = Berita.objects.all()[:5]

    form = DownloadForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            obj = form.save(commit=False)
            obj.dokumen = berita.judul
            obj.url = request.build_absolute_uri()

            obj.save()

    context = {
        "object": berita,
        "related":Related,
        "form": form,
    }
    return render(request, 'web/detail-artikel.html', context)


def ArtikelList(request):
    artikel = Berita.objects.filter(Kategori="Artikel").order_by('-tanggal')
    paginator = Paginator(artikel, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        artikel = paginator.page(page)
    except PageNotAnInteger:
        artikel = paginator.page(1)
    except EmptyPage:
        artikel = paginator.page(paginator.num_pages)

    context = {
        "berita": artikel,
    }

    return render(request, "web/artikel.html", context)
def NewsletterList(request):
    artikel = Berita.objects.filter(Kategori="Newsletter").order_by('-tanggal')
    paginator = Paginator(artikel, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        artikel = paginator.page(page)
    except PageNotAnInteger:
        artikel = paginator.page(1)
    except EmptyPage:
        artikel = paginator.page(paginator.num_pages)

    context = {
        "berita": artikel,
    }

    return render(request, "web/artikel.html", context)

def ArtikelPenelitian(request):
    dokumentasi = Berita.objects.filter(Kategori="Artikel", Agenda="Penelitian").order_by('-tanggal')
    paginator = Paginator(dokumentasi, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        dokumentasi = paginator.page(page)
    except PageNotAnInteger:
        dokumentasi = paginator.page(1)
    except EmptyPage:
        dokumentasi = paginator.page(paginator.num_pages)
    context = {
        "berita": dokumentasi,
    }

    return render(request, "web/dukomentasi.html", context)

def ArtikelAdvokasi(request):
    dokumentasi = Berita.objects.filter(Kategori="Artikel", Agenda="Advokasi").order_by('-tanggal')
    paginator = Paginator(dokumentasi, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        dokumentasi = paginator.page(page)
    except PageNotAnInteger:
        dokumentasi = paginator.page(1)
    except EmptyPage:
        dokumentasi = paginator.page(paginator.num_pages)
    context = {
        "berita": dokumentasi,
    }

    return render(request, "web/dukomentasi.html", context)

def ArtikelPeningkatan(request):
    dokumentasi = Berita.objects.filter(Kategori="Artikel", Agenda="Peningkatan Kapasitas").order_by('-tanggal')
    paginator = Paginator(dokumentasi, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        dokumentasi = paginator.page(page)
    except PageNotAnInteger:
        dokumentasi = paginator.page(1)
    except EmptyPage:
        dokumentasi = paginator.page(paginator.num_pages)
    context = {
        "berita": dokumentasi,
    }

    return render(request, "web/dukomentasi.html", context)
def ArtikelPelayanan(request):
    dokumentasi = Berita.objects.filter(Kategori="Artikel", Agenda="Pelayanan Komunitas").order_by('-tanggal')
    paginator = Paginator(dokumentasi, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        dokumentasi = paginator.page(page)
    except PageNotAnInteger:
        dokumentasi = paginator.page(1)
    except EmptyPage:
        dokumentasi = paginator.page(paginator.num_pages)
    context = {
        "berita": dokumentasi,
    }

    return render(request, "web/dukomentasi.html", context)


def ArtikelDetail(request, berita_slug):
    berita = Berita.objects.get(slug=berita_slug)
    Related = Berita.objects.all()[:5]

    form = DownloadForm(request.POST)

    if request.method == 'POST':


        if form.is_valid():
            obj = form.save(commit=False)
            obj.dokumen = berita.judul
            obj.url = request.build_absolute_uri()

            obj.save()

    context = {
        "object": berita,
        "related":Related,
        "form": form,

    }
    return render(request, 'web/detail-artikel.html', context)


class PublicationList(ListView):
    model = Publikasi
    queryset = Publikasi.objects.all()
    context_object_name = "publikasi"
    paginate_by = 10
    ordering = ['-date_upload']
    template_name = "web/aktivitas.html"


def Kesehatanjiwa(request):
    Slide = HomeSLide.objects.all().distinct()[:1]
    keswa = LayananKeswa.objects.all()

    context = {
        "Slide": Slide,
        "keswa": keswa,
    }

    return render(request, "web/kesehatanjiwa.html", context)

def cop(request):
    Slide = HomeSLide.objects.all().distinct()[:1]
    berita = Berita.objects.filter(tags__slug="cop").order_by('-tanggal')
    acara = Acara.objects.filter(tags__slug="cop").order_by('-waktu_mulai')
    paginator = Paginator(berita, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        berita = paginator.page(page)
    except PageNotAnInteger:
        berita = paginator.page(1)
    except EmptyPage:
        berita = paginator.page(paginator.num_pages)

    context = {
        "acara": acara,
        "Slide": Slide,
        "berita": berita,
    }

    return render(request, "web/cop.html", context)

def EventList(request):
    now = datetime.now()
    acara = Acara.objects.filter(waktu_mulai__gte=now).order_by('waktu_mulai').distinct()
    paginator = Paginator(acara, 5)  # Show 25 contacts per page


    page = request.GET.get('page')
    try:
        acara = paginator.page(page)
    except PageNotAnInteger:
        acara = paginator.page(1)
    except EmptyPage:
        acara = paginator.page(paginator.num_pages)

    context = {
        "Acara": acara,
    }

    return render(request, "web/event.html", context)

def Eventpast(request):
    now = datetime.now()
    acara = Acara.objects.filter(waktu_mulai__lte=now).order_by('-waktu_mulai').distinct()
    paginator = Paginator(acara, 5)  # Show 25 contacts per page


    page = request.GET.get('page')
    try:
        acara = paginator.page(page)
    except PageNotAnInteger:
        acara = paginator.page(1)
    except EmptyPage:
        acara = paginator.page(paginator.num_pages)

    context = {
        "Acara": acara,
    }

    return render(request, "web/event.html", context)


def Eventpenelitian(request):
    acara = Acara.objects.all().filter(Agenda='Penelitian').order_by('-waktu_mulai').distinct()
    paginator = Paginator(acara, 5)  # Show 25 contacts per page
    eventTitle = "Event Penelitian"

    page = request.GET.get('page')
    try:
        acara = paginator.page(page)
    except PageNotAnInteger:
        acara = paginator.page(1)
    except EmptyPage:
        acara = paginator.page(paginator.num_pages)

    context = {
        "Acara": acara,
        "Judul": eventTitle,
    }

    return render(request, "web/event.html", context)

def Eventadvokasi(request):
    acara = Acara.objects.all().filter(Agenda='Advokasi').order_by('-waktu_mulai').distinct()
    paginator = Paginator(acara, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        acara = paginator.page(page)
    except PageNotAnInteger:
        acara = paginator.page(1)
    except EmptyPage:
        acara = paginator.page(paginator.num_pages)

    context = {
        "Acara": acara,
    }

    return render(request, "web/event.html", context)

def Eventpeningkatan(request):
    acara = Acara.objects.all().filter(Agenda='Peningkatan Kapasitas').order_by('-waktu_mulai').distinct()
    paginator = Paginator(acara, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        acara = paginator.page(page)
    except PageNotAnInteger:
        acara = paginator.page(1)
    except EmptyPage:
        acara = paginator.page(paginator.num_pages)

    context = {
        "Acara": acara,
    }

    return render(request, "web/event.html", context)

def Eventpelayanan(request):
    acara = Acara.objects.all().filter(Agenda='Pelayanan Komunitas').order_by('-waktu_mulai').distinct()
    paginator = Paginator(acara, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        acara = paginator.page(page)
    except PageNotAnInteger:
        acara = paginator.page(1)
    except EmptyPage:
        acara = paginator.page(paginator.num_pages)

    context = {
        "Acara": acara,
    }

    return render(request, "web/event.html", context)

def Eventdet(request, acara_slug):
    event = Acara.objects.get(slug=acara_slug)
    template_name = 'web/eventdetail.html'

    related = Acara.objects.all()[:5]

    return render(request, template_name, { 'object':event, 'related': related })

def kontak(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            u = form.save()
            users = Kontak.objects.all()

            return render(request, "web/kontak.html", {'users': users})
    else:
        form_class = ContactForm

    return render(request, "web/kontak.html", {'formh': form_class, 'form2': form2})

def pustaka(request):
    slide = HomeSLide.objects.all()
    Pustaka_HIV = Publikasi.objects.filter(tema='HIV AIDS').order_by('-date_upload').distinct()[:6]
    Pustaka_Publikasi = Publikasi.objects.filter(tema='Publikasi').order_by('-date_upload').distinct()[:6]
    Pustaka_Regulasi = Publikasi.objects.filter(tema='Regulasi').order_by('-date_upload').distinct()[:6]

    context = {
        "Slide": slide,
        "HIV": Pustaka_HIV,
        "Publikasi": Pustaka_Publikasi,
        "Regulasi": Pustaka_Regulasi
    }

    return render(request, "web/pustaka.html", context)

def Pustakadet(request, publikasi_slug):
    publikasi = Publikasi.objects.get(slug=publikasi_slug)
    template_name = 'web/detail-pustaka.html'
    if request.method == 'POST':
        form = DownloadForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.dokumen = publikasi.judul
            obj.url = request.build_absolute_uri()

            obj.save()

            #return HttpResponseRedirect('obj.download')
    else:
        form = DownloadForm()
    return render(request, template_name, {'form': form, 'object':publikasi})

@login_required
def pustakalist(request):
    slide = HomeSLide.objects.all()
    Pustaka_HIV = Publikasi.objects.filter(tema='HIV AIDS').order_by('-date_upload').distinct()
    Pustaka_Publikasi = Publikasi.objects.filter(tema='Publikasi').order_by('-date_upload').distinct()
    Pustaka_Regulasi = Publikasi.objects.filter(tema='Regulasi').order_by('-date_upload').distinct()
    Pustaka_List = Publikasi.objects.all().distinct()

    context = {
        "Slide": slide,
        "HIV": Pustaka_HIV,
        "Publikasi": Pustaka_Publikasi,
        "Regulasi": Pustaka_Regulasi,
        "list": Pustaka_List
    }
    return render(request, "web/pustaka-list.html", context)

class PustakaDetail(DetailView):
    model = Publikasi
    template_name = "web/detail-pustaka.html"
    form_class = DownloadForm

class Taglist(ListView):
    queryset = Berita.objects.all()
    template_name = "web/tag.html"
    paginate_by = 10
    context = "taglist"

    def get_queryset(self):
        return Berita.objects.filter(tags__slug__in=[self.kwargs['tag']])

#SUBSCRIBE FUNCTION
MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = 'https://{dc}.api.mailchimp.com/3.0'.format(dc=MAILCHIMP_DATA_CENTER)
members_endpoint = '{api_url}/lists/{list_id}/members'.format(
    api_url=api_url,
    list_id=MAILCHIMP_EMAIL_LIST_ID
)

def subscribe(email):
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    r = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()

def email_list_signup(request):
    form = EmailSignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email_signup_qs = Signup.objects.filter(email=form.instance.email)
            if email_signup_qs.exists():
                messages.info(request, "You are already subscribed")
            else:
                subscribe(form.instance.email)
                form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def kesjiwdata(request):
    COP = AnotatedCOP.objects.all().order_by('-tanggal').distinct()
    Pustaka_Regulasi = Publikasi.objects.filter(tema='Regulasi', tagging__slug="cop-keswa").order_by('-date_upload').distinct()[:6]
    Pustaka_Publikasi = Publikasi.objects.filter(tema='Publikasi', tagging__slug="cop-keswa").order_by('-date_upload').distinct()[:6]
    paginator = Paginator(COP, 9)
    page = request.GET.get('page')
    try:
        COP = paginator.page(page)
    except PageNotAnInteger:
        COP = paginator.page(1)
    except EmptyPage:
        COP = paginator.page(paginator.num_pages)

    context = {
        'abstracts': COP,
        'pusreg': Pustaka_Regulasi,
        'puspub': Pustaka_Publikasi,
    }
    return render(request, "web/copdatalist.html", context )
def kesjiwregulasi(request):
    judul = "Regulasi Kesehatan Jiwa"
    Pustaka_Regulasi = Publikasi.objects.filter(tema='Regulasi', tagging__slug="cop-keswa").order_by('-date_upload').distinct()
    paginator = Paginator(Pustaka_Regulasi, 9)
    page = request.GET.get('page')
    try:
        Pustaka_Regulasi = paginator.page(page)
    except PageNotAnInteger:
        Pustaka_Regulasi = paginator.page(1)
    except EmptyPage:
        Pustaka_Regulasi = paginator.page(paginator.num_pages)

    context = {
        'objects': Pustaka_Regulasi,
        'judul': judul,
    }
    return render(request, "web/kesjiwdatalist.html", context )

def kesjiwproduk(request):
    judul = "Produk Pengetahuan PPH"
    Pustaka_Publikasi = Publikasi.objects.filter(tema='Publikasi', tagging__slug="cop-keswa").order_by('-date_upload').distinct()[:6]
    paginator = Paginator(Pustaka_Publikasi, 9)
    page = request.GET.get('page')
    try:
        Pustaka_Publikasi = paginator.page(page)
    except PageNotAnInteger:
        Pustaka_Publikasi = paginator.page(1)
    except EmptyPage:
        Pustaka_Publikasi = paginator.page(paginator.num_pages)

    context = {
        'objects': Pustaka_Publikasi,
        'judul': judul
    }
    return render(request, "web/kesjiwdatalist.html", context )

def kesjiwartikel(request):
    judul = "Artikel Jurnal Kesehatan Jiwa"
    COP = AnotatedCOP.objects.all().order_by('-tanggal').distinct()
    paginator = Paginator(COP, 9)
    page = request.GET.get('page')
    try:
        COP = paginator.page(page)
    except PageNotAnInteger:
        COP = paginator.page(1)
    except EmptyPage:
        COP = paginator.page(paginator.num_pages)

    context = {
        'objects': COP,
        'judul': judul

    }
    return render(request, "web/kesjiwdatajurnal.html", context )

def KesjiwDetail(request, AnotatedCOP_slug):
    abstracts = AnotatedCOP.objects.get(slug=AnotatedCOP_slug)

    context = {
        "object": abstracts,
    }
    return render(request, 'web/copdatadetail.html', context)

