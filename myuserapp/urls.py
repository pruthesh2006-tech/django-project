from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageview),
    path('home', views.homepageview),
    path('about', views.aboutpageview),
    path('contact', views.contactpageview),
    path('shop', views.shoppage),
    path('contactprocess', views.contactprocess),
    path('saveSession', views.saveSessionData),
    path('getSession', views.getSessionData),
    path('getSession2', views.getSessionData2),
    path('deleteSession', views.deleteSessionData),
    path('login', views.loginpage),
    path('loginprocess',views.loginprocess),
    path('dashboard', views.dashboard),
    path('logout',views.logout),
    path('maildemo',views.mailsenddemo),
    path('contactMe', views.contactMe),
    path('contactus', views.contactus),
    path('addStudent', views.addstudentform),
    path('add-student-process', views.addstudentformprocess)
]   

