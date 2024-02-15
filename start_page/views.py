from django.shortcuts import render


def landing(request):
    return render(request, 'start_page/base.html')