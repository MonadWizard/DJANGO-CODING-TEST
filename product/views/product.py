from django.shortcuts import render
from django.views import generic

from product.models import Variant, ProductVariantPrice

from product.choices import varient_choices


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


def search(request):
    queryset_list = ProductVariantPrice.objects.order_by('-created_at')

    # keywords
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(product__title__contains=title)   # search enter description
    # # citys
    # if 'city' in request.GET:
    #     city = request.GET['city']
    #     if city:
    #         queryset_list = queryset_list.filter(city__iexact=city)   # search enter description
    #
    # state
    if 'variant' in request.GET:
        variant = request.GET['variant']
        if variant:
            queryset_list = queryset_list.filter(product_variant_one__variant__title__contains=variant)   # search enter description

    # # bedrooms
    # if 'bedrooms' in request.GET:
    #     bedrooms = request.GET['bedrooms']
    #     if bedrooms:
    #         queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)   # search enter description
    #
    # # bedrooms
    # if 'price' in request.GET:
    #     price = request.GET['price']
    #     if price:
    #         queryset_list = queryset_list.filter(price__lte=price)   # search enter description
    #


    context = {
        # 'state_choices':state_choices,
        # 'bedroom_choices':bedroom_choices,
        'varient_choices':varient_choices,
        'listings':queryset_list,
        'values': request.GET,

    }
    template_name = 'products/list.html'
    return render(request,template_name, context)



