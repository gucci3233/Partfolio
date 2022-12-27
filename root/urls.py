from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root import settings

urlpatterns = [
                  path('', include('apps.urls')),
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
