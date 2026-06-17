from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageview),
    path('home', views.homepageview),
    path('about', views.aboutpageview),
    path('contact', views.contactpageview),
    path('shop', views.shoppage),
    path('contactprocess', views.contactprocess),
]

