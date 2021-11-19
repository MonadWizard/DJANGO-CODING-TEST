from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from product.models import Variant, ProductVariantPrice, ProductVariant

from product.forms import ProductForm



class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


def search(request):
    queryset_list = ProductVariantPrice.objects.order_by('id')

    # title
    if 'title' in request.POST:
        title = request.POST['title']
        if title:
            queryset_list = queryset_list.filter(product__title__contains=title)

    # variant
    varient_list = ProductVariant.objects.all()

    if 'variant' in request.POST:
        variant = request.POST['variant']
        if variant:
            queryset_list = queryset_list.filter(product_variant_one__variant__title__contains=variant) \
                            | queryset_list.filter(product_variant_two__variant__title__contains=variant) \
                            | queryset_list.filter(product_variant_three__variant__title__contains=variant)

    # price
    price_from = request.POST.get('price_from', 0)
    price_to = request.POST.get('price_to', 1000000)
    queryset_list = queryset_list.filter(price__gte=price_from).filter(price__lte=price_to)

    # # Date
    if 'date' in request.POST:
        date = request.POST['date']
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
        'varient_list': varient_list,
        'price_from': price_from,
        'price_to': price_to,
        'listings':paged_listing,
        'values': request.GET,
    }
    template_name = 'products/list.html'
    return render(request,template_name, context)


def edit(request, edit_id):
    # if page not available then show 404
    productVP = get_object_or_404(ProductVariantPrice, pk=edit_id)  # (model,pk)
    form = ProductForm(instance=productVP)

    if request.method == "POST":
        # print("printing post : ",request.POST)
        form = ProductForm(request.POST, instance=productVP)
        if form.is_valid():
            form.save()
            # return redirect('/')

    context = {'form':form}
    template_name = 'products/edit.html'
    return render(request,template_name, context)

