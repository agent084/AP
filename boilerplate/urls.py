from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('shop.html', views.shop, name='shop'),
    path('contact.html', views.contact, name='contact'),
    path('shop-single.html', views.shop_single, name='shop_single'),
    path('cart.html', views.cart, name='cart'),
    path('checkout.html', views.checkout, name='checkout'),
    path('thankyou.html', views.thankyou, name='thankyou'),      

]
