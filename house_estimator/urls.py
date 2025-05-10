from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('materiais.urls')),
    path('', include('user_profile.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
