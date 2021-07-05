from django.urls import path, re_path,include
from WEB import views as webviews
from django.views.generic import TemplateView



urlpatterns = [
    path('', webviews.Home, name='home-web'),
    path('tentang-kami/', webviews.Tentangkami, name = 'Tentang-Kami'),
    path('kontak/', webviews.kontak, name = 'kontak'),
    path('subscribe/', webviews.email_list_signup, name= 'subscribe'),
    re_path('tag/(?P<tag>[\w-]+)/$', webviews.Taglist.as_view(), name='tag'),
    re_path('staff/(?P<staff_slug>[\w-]+)/$', webviews.webstaffDetail, name='web-staff-detail'),
    #PUSTAKA-------------------------------
    path('pelayanan-komunitas/', webviews.pelayananKomunitas, name= 'pelayanankomunitas'),
    path('pustaka/', webviews.pustaka, name= 'pustaka'),
    path('pustaka/penelitian/', webviews.pustakalistpenelitian, name= 'pustaka-penelitian'),
    path('pustaka/publikasi/', webviews.pustakalistpublikasi, name= 'pustaka-publikasi'),
    path('pustaka/regulasi/', webviews.pustakalistregulasi, name= 'pustaka-regulasi'),
    path('pustaka/pelayanan-komunitas/', webviews.pustakalistpelayanan, name= 'pustaka-pelayanan'),
    path('pustaka/informasi-hiv-aids/', webviews.pustakalist, name= 'pustaka-list'),
    path('pustaka/peningkatan-kapasitas/', webviews.pustakalistpeningkatan, name= 'pustaka-peningkatan'),
    re_path('pustaka/(?P<publikasi_slug>[\w-]+)/$', webviews.Pustakadet, name='pusdet-detail'),
    path('kegiatan/', webviews.PublicationList.as_view(), name='kegiatan'),
    path('research-fellowship/', webviews.Internship, name='fellow'),

    path('berita/artikel/', webviews.ArtikelList, name='artikel-list'),
    path('berita/artikel/penelitian/', webviews.ArtikelPenelitian, name='artikel-penelitian'),
    path('berita/artikel/advokasi/', webviews.ArtikelAdvokasi, name='artikel-advokasi'),
    path('berita/artikel/peningkatan-kapasitas/', webviews.ArtikelPeningkatan, name='artikel-peningkatan'),
    path('berita/artikel/pelayanan-komunitas/', webviews.ArtikelPelayanan, name='artikel-pelayanan'),
    re_path('berita/artikel/(?P<berita_slug>[\w-]+)/$', webviews.ArtikelDetail, name='art-detail'),

    path('events/upcoming-event/', webviews.EventList, name='event-lalu'),
    path('events/', webviews.Event, name='event-list'),
    re_path('event/(?P<acara_slug>[\w-]+)/$', webviews.Eventdet, name='event-detail'),

    path('berita/dokumentasi/', webviews.DokumentasiList, name='dokumentasi'),

    path('berita/dokumentasi/penelitian/', webviews.DokumentasiPenelitian, name='dokumentasi-penelitian'),
    path('berita/dokumentasi/advokasi/', webviews.DokumentasiAdvokasi, name='dokumentasi-advokasi'),
    path('berita/dokumentasi/peningkatan-kapasitas/', webviews.DokumentasiPeningkatan, name='dokumentasi-peningkatan'),
    path('berita/dokumentasi/pelayanan-komunitas/', webviews.DokumentasiPelayanan, name='dokumentasi-pelayanan'),
    path('berita/dokumentasi/newsletter/', webviews.DokumentasiNewsletter, name='newsletter'),
    re_path('berita/dokumentasi/(?P<berita_slug>[\w-]+)/$', webviews.Dokumendetail, name='dak-detail'),

    path('berita/newsletter/', webviews.NewsletterList, name='newsletter'),
    re_path('berita/newsletter/(?P<berita_slug>[\w-]+)/$', webviews.Dokumendetail, name='dak-detail'),

    path('kegiatan/penelitian/', webviews.DokumentasiPenelitian, name='kegiatan-penelitian'),
    path('kegiatan/advokasi/', webviews.DokumentasiAdvokasi, name='kegiatan-advokasi'),
    path('kegiatan/peningkatan-kapasitas/', webviews.DokumentasiPeningkatan, name='kegiatan-peningkatan'),
    path('kegiatan/pelayanan-komunitas/', webviews.DokumentasiPelayanan, name='kegiatan-pelayanan'),


    path('kesehatan-jiwa/', webviews.Kesehatanjiwa, name='Kesehatanjiwa'),
    path('kesehatan-jiwa/database/', webviews.kesjiwdata, name='kesjiwlist'),
    path('kesehatan-jiwa/regulasi-kesehatan-jiwa/', webviews.kesjiwregulasi, name='kesjiwregulasi'),
    path('kesehatan-jiwa/produk-pengetahuan-pph/', webviews.kesjiwproduk, name='kesjiwproduk'),
    path('kesehatan-jiwa/artikel-jurnal-kesehatan-jiwa/', webviews.kesjiwartikel, name='kesjiwartikel'),
    re_path('kesehatan-jiwa/jurnal/(?P<AnotatedCOP_slug>[\w-]+)/$', webviews.KesjiwDetail, name='anotate-detail'),
    path('cop/', webviews.cop, name='cop'),
    path('privacy-policy/', webviews.PrivacyPolicy, name='privacy'),
    path('internship/', TemplateView.as_view(template_name='web/internship.html'), name='internship'),
]