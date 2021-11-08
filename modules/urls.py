from django.urls import path

from modules import views

app_name = 'modules'
urlpatterns = [
    path('<slug:slug>', views.details, name='details'),
    path('lessons/<slug:slug>', views.lessons, name='lesson')
]
