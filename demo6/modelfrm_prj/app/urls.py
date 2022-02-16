from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from . import models
from django.conf.urls.static import static


urlpatterns = [

	path('fertility/', views.fertility, name="fertility"),
	path('show/', views.showdata, name="showdata"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)