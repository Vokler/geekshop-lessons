from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket


# def basket(request):
#     context = {'baskets': Basket.objects.filter(user=request.user)}
#     print(context)
#     return render(request, 'basketapp/basket.html', context)


def basket_add(request, id=None):
    product = get_object_or_404(Product, id=id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
