from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from SEARCH import views as searchviews


admin.sites.AdminSite.site_header = 'PPH UNIKA ATMA JAYA'
admin.sites.AdminSite.site_title = 'PPH UNIKA ATMA JAYA'
admin.sites.AdminSite.index_title = 'PPH UNIKA ATMA JAYA'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WEB.url')),
    path('km/', include('KM.url')),
    path('cari/', searchviews.SearchView.as_view(), name='cari' ),
    path('users/', include('USER.url')),
    path('users/', include('django.contrib.auth.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)