import json
import urllib
import requests

from django.shortcuts import render, Http404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import modelformset_factory
from django.views.generic import DetailView, ListView, TemplateView
from .forms import ContactForm, DownloadForm, EmailSignupForm
from django.views.generic.edit import FormMixin
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .utils import SendSubscribeMail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from lazysignup.decorators import allow_lazy_user
from taggit.models import Tag, TaggedItem
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .multiforms import MultiFormsView


form2 = EmailSignupForm()

from .models import Berita, Acara, TentangKami, HomeSLide, Kontak, Signup
from KM.models import Publikasi, Staff


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
    context = {
        "object": berita,
        "related":Related,
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
    context = {
        "object": berita,
        "related":Related,

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
    berita = Berita.objects.filter(tags__slug="kesehatan-jiwa")
    paginator = Paginator(berita, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        berita = paginator.page(page)
    except PageNotAnInteger:
        berita = paginator.page(1)
    except EmptyPage:
        berita = paginator.page(paginator.num_pages)

    context = {
        "Slide": Slide,
        "berita": berita,
    }

    return render(request, "web/kesehatanjiwa.html", context)

def EventList(request):
    acara = Acara.objects.all().order_by('-waktu_mulai').distinct()
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
    Pustaka_HIV = Publikasi.objects.filter(tema='HIV AIDS').order_by('date_upload').distinct()[:6]
    Pustaka_Publikasi = Publikasi.objects.filter(tema='Publikasi').order_by('date_upload').distinct()[:6]
    Pustaka_Regulasi = Publikasi.objects.filter(tema='Regulasi').order_by('date_upload').distinct()[:6]

    context = {
        "Slide": slide,
        "HIV": Pustaka_HIV,
        "Publikasi": Pustaka_Publikasi,
        "Regulasi": Pustaka_Regulasi
    }

    return render(request, "web/pustaka.html", context)

def Pustakadet(request, publikasi_slug):

    publikasi = Publikasi.objects.get(slug=publikasi_slug)

    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():

            u = form.save()
            users = DownloadForm.objects.all()

            return render(request, "web/detail-pustaka.html", {'users': users})
    else:
        form_class = DownloadForm

    return render(request, "web/detail-pustaka.html", {'form': form_class, 'object': publikasi})

#@login_required(login_url='/users/login/')
@allow_lazy_user
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

    def get_context_data(self, **kwargs):
        context = super(PustakaDetail, self).get_context_data(**kwargs)
        context['form'] = DownloadForm(initial={'POST': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PustakaDetail, self).form_valid(form)

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


#----------multiple form --------------

def form_redir(request):
    return render(request, 'pages/form_redirect.html')


def multiple_forms(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        subscription_form = EmailSignupForm(request.POST)
        if contact_form.is_valid() or subscription_form.is_valid():
            # Do the needful
            return HttpResponseRedirect(reverse('form-redirect'))
    else:
        contact_form = ContactForm()
        subscription_form = EmailSignupForm()

    return render(request, 'pages/multiple_forms.html', {
        'contact_form': contact_form,
        'subscription_form': subscription_form,
    })


class MultipleFormsDemoView(MultiFormsView):
    template_name = "web/cbv_multiple_forms.html"
    form_classes = {'contact': ContactForm,
                    'subscription': EmailSignupForm,
                    }

    success_urls = {
        'contact': reverse_lazy('form-redirect'),
        'subscription': reverse_lazy('form-redirect'),
    }

    def contact_form_valid(self, form):
        title = form.cleaned_data.get('title')
        form_name = form.cleaned_data.get('action')
        print(title)
        return HttpResponseRedirect(self.get_success_url(form_name))

    def subscription_form_valid(self,):
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