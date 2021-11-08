from django.urls import path

from modules import views

app_name = 'modules'
urlpatterns = [
    path('<slug:slug>', views.details, name='details'),
]