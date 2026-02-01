from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorting = request.GET.get('sort')
    phones = Phone.objects.all()
    if sorting == 'name':
        phones = sorted(phones, key=lambda x: x.name)
    elif sorting == 'min_price':
        phones = sorted(phones, key=lambda x: x.price)
    elif sorting == 'max_price':
        phones = sorted(phones, key=lambda x: x.price, reverse=True)

    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(slug=slug)[0]
    }
    return render(request, template, context)
