from django.shortcuts import render, get_object_or_404

from demonstration.models import Video


def video(request, slug):
    video_obj = get_object_or_404(Video, slug=slug)
    context = {
        'video': video_obj
    }
    return render(request, 'demonstration/video.html', context)
