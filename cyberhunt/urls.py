from django.contrib import admin
from django.urls import path, include
import teams.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', teams.views.home, name='home'),
    path('team/', include('teams.urls')),
]
