from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body><h1>Hello Django<h1></body></html>', content_type='text/html')
