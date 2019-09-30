from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('',views.index),
    path('home',views.photo),
    path('take',views.take),
    path('register',views.register),
    path('RegisterUpload',views.RegisterUpload),
    path('about',views.about),
    path('mail_to',views.mail_to),
    path('mail',views.mail),
    path('deleted',views.delete)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)