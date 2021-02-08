from django.contrib import admin

from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', 'image', 'description', 'short_desc', ('price', 'quantity'), 'category')
    readonly_fields = ('short_desc',)
    ordering = ('name',)
    search_fields = ('name',)
