from message_page.settings import STATIC_URL
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
if settings.DEBUG:
    urlpatterns += STATIC_URL(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)