from django.shortcuts import render, get_object_or_404

from demonstration.models import Video


def video(request, slug):
    video_obj = get_object_or_404(Video, slug=slug)
    context = {
        'video': video_obj
    }
    return render(request, 'demonstration/video.html', context)


def index(request):
    video_obj = Video.objects.order_by('created_at').all()
    context = {
        'videos': video_obj
    }
    return render(request, 'demonstration/demonstration_index.html', context)
