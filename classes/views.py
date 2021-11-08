from django.shortcuts import render


def index(request):
    return render(request, 'classes/classes_index.html')
