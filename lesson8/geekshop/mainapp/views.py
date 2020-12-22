from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def main(request):
    content = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request, category_id=None):
    context = {'title': 'GeekShop - Категории'}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        context.update({
            'categories': ProductCategory.objects.all(),
            'products': products,
        })
        return render(request, 'mainapp/products.html', context)

    context.update({
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    })
    return render(request, 'mainapp/products.html', context)
