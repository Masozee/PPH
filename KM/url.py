from django.urls import path, re_path
from KM import views as kmviews
from django.contrib.auth.decorators import login_required, permission_required 

urlpatterns = [
    path('', kmviews.homepage, name = 'KM-home'),
    path('staff/', kmviews.stafflist, name = 'KM-Staff'),
    #path('staff/<str:slug>/', kmviews.Staffdetail, name='staff-detail'),
    re_path('staff/(?P<staff_slug>[\w-]+)/$', kmviews.staffDetail, name='staff-detail'),

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
]
