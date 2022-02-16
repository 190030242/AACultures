from django.urls import path
from . import views

urlpatterns = [
    path('image/', views.indexs, name="image"),

    path('main/', views.main, name="main"),

]