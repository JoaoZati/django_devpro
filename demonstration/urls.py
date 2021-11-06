from django.urls import path

from demonstration.views import video

app_name = 'demonstration'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]
