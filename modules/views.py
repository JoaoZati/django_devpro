from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from modules import facade


def details(request, slug):
    module = facade.find_module(slug)
    lessons = facade.list_modules_ordered_lessons(module)
    context = {
        'module': module,
        'lessons': lessons,
    }
    return render(request, 'modules/module_details.html', context)


@login_required
def lessons(request, slug):
    lesson = facade.find_lesson(slug)
    context = {
        'lesson': lesson
    }
    return render(request, 'modules/lesson_details.html', context)


def index(request):
    context = {
        'modules': facade.list_modules_and_lessons()
    }
    return render(request, 'modules/modules_index.html', context)
