from django.urls import path

from classes import views

app_name = 'classes'
urlpatterns = [
    path('', views.index, name='index'),
]
