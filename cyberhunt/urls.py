from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import teams.views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', teams.views.home, name='home'),
    path('team/', include('teams.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
