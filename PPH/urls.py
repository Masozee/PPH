from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from SEARCH import views as searchviews
from USER.views import visitor
from django.contrib.auth import views as auth_views


admin.sites.AdminSite.site_header = 'PPH UNIKA ATMA JAYA'
admin.sites.AdminSite.site_title = 'PPH UNIKA ATMA JAYA'
admin.sites.AdminSite.index_title = 'PPH UNIKA ATMA JAYA'

urlpatterns = [
    path('admin/', admin.site.urls, name='webadmin'),
    path('', include('WEB.url')),
    path('km/', include('KM.url')),
    path('cari/', searchviews.SearchView.as_view(), name='cari' ),
    path('KM/cari/', searchviews.SearchKMView.as_view(), name='km-cari' ),
    path('users/', include('USER.url')),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', visitor.VisitorSignUpView.as_view(), name='visitor-signup'),
    path(r'captcha/', include('captcha.urls')),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name="password_reset"),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name="password_reset_complete")

]

#urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)