from django.shortcuts import render

from modules import facade


def details(request, slug):
    module = facade.find_module(slug)
    context = {
        'module': module,
    }
    return render(request, 'modules/module_details.html', context)
