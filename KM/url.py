from django.urls import path, re_path
from KM import views as kmviews

from django.contrib.auth.decorators import login_required, permission_required 

urlpatterns = [
    path('', kmviews.homepage, name = 'KM-home'),
    path('staff/', kmviews.stafflist, name = 'KM-Staff'),
    #path('staff/<str:slug>/', kmviews.Staffdetail, name='staff-detail'),
    re_path('staff/(?P<staff_slug>[\w-]+)/$', kmviews.staffDetail, name='staff-detail'),
    path('staff/peningkatan-kapasitas/add/', kmviews.PeningkatanAdd, name='add-peningkatan'),
    path('staff/publikasi/add/', kmviews.PenelitianAdd, name='add-publikasi'),


    path('inventaris/', kmviews.inventaris, name = 'KM-Inventaris'),

    path('kegiatan/', kmviews.kegiatan, name = 'KM-Kegiatan'),
    path('kontak/', kmviews.kontak, name= 'KM-Kontak'),

    path('media/media-advokasi/', kmviews.media, name= 'KM-Media'),
    path('media/manajemen/', kmviews.manajemen, name= 'KM-Manajemen'),

    path('evaluasi/penelitian/', kmviews.evaluasi, name= 'KM-evaluasipenelitian'),
    path('evaluasi/peningkatan-kapasitas/', kmviews.evaluasikapasitas, name= 'KM-Evaluasikapasitas'),

    path('pelaporan/', kmviews.lapor, name= 'KM-Lapor'),
    path('kalender/', kmviews.kalender, name= 'KM-Kalender'),

    path('penelitian/', kmviews.profilpenelitian, name='KM-Penelitian'),
    re_path('penelitian/(?P<penelitian_slug>[\w-]+)/$', kmviews.PenelitianDetail, name='penelitian-detail'),

    path('peningkatan-kapasitas/', kmviews.profilpeningkatan, name='KM-Peningkatan'),
    re_path('peningkatan-kapasitas/(?P<peningkatanKapasitas_slug>[\w-]+)/$', kmviews.PeningkatanDetail, name='peningkatan-detail'),

    path('kalender/', kmviews.kalender, name='kalender'),

    path('laporan/staff', kmviews.staff_pdf, name='print-staff'),
    path('laporan/acara', kmviews.acara_pdf, name='print-acara'),
    path('laporan/berita', kmviews.berita_pdf, name='print-berita'),
    path('laporan/inventaris', kmviews.inv_pdf, name='print-inv'),
    path('laporan/penelitian', kmviews.penelitian_pdf, name='print-penelitian'),



]
