from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    queryset_list = ProductVariantPrice.objects.order_by('created_at')

    # title
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(product__title__contains=title)

    # variant
    if 'variant' in request.GET:
        variant = request.GET['variant']
        if variant:
            queryset_list = queryset_list.filter(product_variant_one__variant__title__contains=variant)

    # price
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 1000000)
    queryset_list = queryset_list.filter(price__gte=price_from).filter(price__lte=price_to)

    # # Date
    if 'date' in request.GET:
        date = request.GET['date']
        if date:
            queryset_list = queryset_list.filter(created_at__date=date)

    paginator = Paginator(queryset_list, 2)
    page = request.GET.get('page')
    try:
        paged_listing = paginator.page(page)
    except PageNotAnInteger:
        paged_listing = paginator.page(1)
    except EmptyPage:
        paged_listing = paginator.page(paginator.num_pages)



    context = {
        'price_from': price_from,
        'price_to': price_to,
        'varient_choices':varient_choices,
        'listings':paged_listing,
        'values': request.GET,
    }
    template_name = 'products/list.html'
    return render(request,template_name, context)



