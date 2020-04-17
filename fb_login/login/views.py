from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    app_id = 247987559730617
    context = {
        "app_id": app_id,
    }
    return render(request, 'login.html', context)


def login(request):
    return HttpResponse('hello django')
