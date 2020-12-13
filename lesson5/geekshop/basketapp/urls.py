from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    # path('', basketapp.basket, name='basket'),
    path('add/<int:id>/', basketapp.basket_add, name='basket_add'),
    # path('remove/<int:pk>)/', basketapp.basket_remove, name='remove'),
]
