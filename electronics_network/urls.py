from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/api/')),
    path('admin/', admin.site.urls),
    path('api/', include('network.urls')),
]
