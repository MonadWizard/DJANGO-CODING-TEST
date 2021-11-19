from django.contrib import admin

# Register your models here.
from .models import *

# change Register your models data's list views attribite.
class VariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')   # display items
    list_display_links = ('title', 'description')  #clickable display items
    list_filter = ('title',)   # filter display items
    list_editable = ('id', )   # editable list item
    search_fields = ('title', 'description')  # search panels filter items
    list_per_page = 2   # display list per page

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')   # display items
    list_display_links = ('title', 'description')  #clickable display items
    list_filter = ('title',)   # filter display items
    list_editable = ('id', )   # editable list item
    search_fields = ('title', 'sku')  # search panels filter items
    list_per_page = 2   # display list per page


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'file_path')   # display items
    list_display_links = ('product', 'file_path')  #clickable display items
    list_filter = ('product',)   # filter display items
    list_editable = ('id', )   # editable list item
    search_fields = ('product', 'file_path')  # search panels filter items
    list_per_page = 2   # display list per page

class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'variant_title', 'variant', 'product')   # display items
    list_display_links = ('variant_title','variant', 'product',)  #clickable display items
    list_filter = ('variant_title',)   # filter display items
    list_editable = ('id', )   # editable list item
    search_fields = ('variant_title', 'variant', 'product')  # search panels filter items
    list_per_page = 2   # display list per page


class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_variant_one', 'product_variant_two', 'product_variant_three', 'price','stock','product')   # display items
    list_display_links = ('price','stock','product',)  #clickable display items
    list_filter = ('price',)   # filter display items
    list_editable = ('id', )   # editable list item
    search_fields = ('product_variant_one', 'product_variant_two', 'product_variant_three', 'price','stock','product')  # search panels filter items
    list_per_page = 2   # display list per page


admin.site.register(Variant, VariantAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVariant , ProductVariantAdmin)
admin.site.register(ProductVariantPrice, ProductVariantPriceAdmin)
