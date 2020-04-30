from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from SEARCH import views as searchviews
from  USER import views as userviews


admin.sites.AdminSite.site_header = 'PPH UNIKA ATMA JAYA'
admin.sites.AdminSite.site_title = 'PPH UNIKA ATMA JAYA'
admin.sites.AdminSite.index_title = 'PPH UNIKA ATMA JAYA'

urlpatterns = [
    path('admin/', admin.site.urls, name='webadmin'),
    path('', include('WEB.url')),
    path('km/', include('KM.url')),
    path('cari/', searchviews.SearchView.as_view(), name='cari' ),
    path('KM/cari/', searchviews.SearchKMView.as_view(), name='km-cari' ),
    #path('users/', include('USER.url')),
    #path('users/', include('django.contrib.auth.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/signup/', visitor.VisitorSignUpView.as_view(), name='visitor-signup'),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/signup/', VisitorSignUpView.as_view(), name='visitor-signup'),
    path('accounts/signup/', userviews.signup, name='visitor-signup'),
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        userviews.activate, name='activate'),

]

#urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)