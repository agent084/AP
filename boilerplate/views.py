from django.shortcuts import render

def index(request):
    return render(request, 'boilerplate/index.html', context=None)
def about(request):
    return render(request, 'boilerplate/about.html', context=None)
def shop(request):
    return render(request, 'boilerplate/shop.html', context=None)
def contact(request):
    return render(request, 'boilerplate/contact.html', context=None)
def shop_single(request):
    return render(request, 'boilerplate/shop-single.html', context=None)
def cart(request):
    return render(request, 'boilerplate/cart.html', context=None)
def checkout(request):
    return render(request, 'boilerplate/checkout.html', context=None)
def thankyou(request):
    return render(request, 'boilerplate/thankyou.html', context=None)