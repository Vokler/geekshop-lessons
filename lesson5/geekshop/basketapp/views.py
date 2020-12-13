from django.shortcuts import render


def basket(request):
    return render(request, 'basketapp/basket.html')
