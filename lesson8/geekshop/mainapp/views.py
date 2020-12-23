from django.shortcuts import render

from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main(request):
    content = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request, category_id=None):
    """Without pagination."""
    context = {'title': 'GeekShop - Категории', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        context.update({
            'products': products,
        })
    else:
        context.update({
            'products': Product.objects.all(),
        })
    return render(request, 'mainapp/products.html', context)

# def products(request, category_id=None):
#     """With pagination."""
#     context = {'title': 'GeekShop - Категории'}
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#         context.update({
#             'categories': ProductCategory.objects.all(),
#             'products': products,
#         })
#         return render(request, 'mainapp/products.html', context)
#
#     context.update({
#         'categories': ProductCategory.objects.all(),
#         'products': Product.objects.all(),
#     })
#     return render(request, 'mainapp/products.html', context)
