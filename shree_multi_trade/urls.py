from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
]

admin.site.site_header = "Shree Multi Trade Admin Portal"

