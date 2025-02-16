from . import views
from django.urls import path
from django_distill import distill_path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    distill_path("", views.home, name="home"),

]