from django.urls import path, re_path,include
from WEB import views as webviews



urlpatterns = [
    path('', webviews.Home, name='home-web'),
    path('tentang-kami/', webviews.Tentangkami, name = 'Tentang-Kami'),
    path('kontak/', webviews.kontak, name = 'kontak'),
    path('subscribe/', webviews.email_list_signup, name= 'subscribe'),
    re_path('tag/(?P<tag>[\w-]+)/$', webviews.Taglist.as_view(), name='tag'),

    #PUSTAKA-------------------------------
    path('pustaka/', webviews.pustaka, name= 'pustaka'),
    path('pustaka/list/', webviews.pustakalist, name= 'pustaka-list'),
    re_path('pustaka/(?P<publikasi_slug>[\w-]+)/$', webviews.Pustakadet, name='pusdet-detail'),
    #re_path('pustaka/(?P<slug>[\w-]+)/$', webviews.PustakaDetail, name='pusdet-detail'),
    path('kegiatan/', webviews.PublicationList.as_view(), name='kegiatan'),

    #path('kegiatan/<str:slug>/', webviews.PublicationDetail.as_view(), name = 'kegiatan-detail'),
    path('berita/artikel/', webviews.ArtikelList, name='artikel-list'),
    path('berita/artikel/penelitian/', webviews.ArtikelPenelitian, name='artikel-penelitian'),
    path('berita/artikel/advokasi/', webviews.ArtikelAdvokasi, name='artikel-advokasi'),
    path('berita/artikel/peningkatan-kapasitas/', webviews.ArtikelPeningkatan, name='artikel-peningkatan'),
    path('berita/artikel/pelayanan-komunitas/', webviews.ArtikelPelayanan, name='artikel-pelayanan'),
    re_path('berita/artikel/(?P<berita_slug>[\w-]+)/$', webviews.ArtikelDetail, name='art-detail'),

    path('events/', webviews.EventList, name='event-list'),
    path('events/penelitian/', webviews.Eventpenelitian, name='event-penelitian'),
    path('events/advokasi/', webviews.Eventadvokasi, name='event-advokasi'),
    path('events/peningkatan-kapasitas', webviews.Eventpeningkatan, name='event-peningkatan'),
    path('events/pelayanan-komunitas', webviews.Eventpelayanan, name='event-pelayanan'),

    #path('artikel/<str:slug>/', webviews.NewsDetail.as_view(), name = 'artikel-detail'),
    path('berita/dokumentasi/', webviews.DokumentasiList, name='dokumentasi'),
    path('berita/dokumentasi/penelitian/', webviews.DokumentasiPenelitian, name='dokumentasi-penelitian'),
    path('berita/dokumentasi/advokasi/', webviews.DokumentasiAdvokasi, name='dokumentasi-advokasi'),
    path('berita/dokumentasi/peningkatan-kapasitas/', webviews.DokumentasiPeningkatan, name='dokumentasi-peningkatan'),
    path('berita/dokumentasi/pelayanan-komunitas/', webviews.DokumentasiPelayanan, name='dokumentasi-pelayanan'),
    #path('berita/dokumentasi/<str:slug>/', webviews.DokumentasiDetail.as_view(), name='dokumentasi-detail'),
    re_path('berita/dokumentasi/(?P<berita_slug>[\w-]+)/$', webviews.Dokumendetail, name='dak-detail'),
    #path('events/<str:slug>/', webviews.EventDetail.as_view(), name = 'event-detail'),

    path('kegiatan/penelitian/', webviews.DokumentasiPenelitian, name='kegiatan-penelitian'),
    path('kegiatan/advokasi/', webviews.DokumentasiAdvokasi, name='kegiatan-advokasi'),
    path('kegiatan/peningkatan-kapasitas/', webviews.DokumentasiPeningkatan, name='kegiatan-peningkatan'),
    path('kegiatan/pelayanan-komunitas/', webviews.DokumentasiPelayanan, name='kegiatan-pelayanan'),


    path('kesehatan-jiwa/', webviews.Kesehatanjiwa, name='Kesehatanjiwa'),

    #path('admin_export/', include("admin_export.urls", namespace="admin_export")),




    #path('staff/', webviews.Team.as_view(), name='news-list'),
]