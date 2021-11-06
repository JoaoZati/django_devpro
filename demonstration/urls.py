from django.urls import path

from demonstration.views import video, index

app_name = 'demonstration'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', index, name='index'),
]
