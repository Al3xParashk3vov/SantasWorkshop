from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from SantasWorkshop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SantasWorkshop.base.urls')),
    path('accounts/', include('SantasWorkshop.accounts.urls')),
    path('presents/', include('SantasWorkshop.presents.urls')),
    path('blogs/', include('SantasWorkshop.blogs.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'SantasWorkshop.base.views.custom_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
