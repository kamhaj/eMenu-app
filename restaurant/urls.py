from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ## admin
    path('admin/', admin.site.urls),

    ## eMenu app API
    path('api/eMenu/', include('eMenu.urls', namespace='eMenu')),
]
