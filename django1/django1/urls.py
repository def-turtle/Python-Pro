from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('resources/', include('main.urls')),
    path('pricing/', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', include('main.urls')),
]