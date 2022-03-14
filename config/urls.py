from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('news/', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
]
