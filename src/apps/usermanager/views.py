from django.shortcuts import render


def register(request):
    return render(request, 'usermanager/registration.html', {})
