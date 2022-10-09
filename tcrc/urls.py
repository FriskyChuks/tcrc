from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from church.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/',include('profiles.urls'),name='profiles'),
    path('accounts/',include('accounts.urls'),name='accounts'),
    path('',home, name='home'),
    path('contact/',contact, name='contact'),
    path('about_us/',about_us, name='about_us'),
    path('unit_dept/',unit_dept, name='unit_dept'),
    path('submit_report/',submit_report, name='submit_report'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
