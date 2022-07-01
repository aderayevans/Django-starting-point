from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('home.urls')),
    # path('home/', include('home.urls')),
    path('polls/', include('polls.urls')),
    path('library/', include('library.urls')),
]
