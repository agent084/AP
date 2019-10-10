from django.urls import path

from . import views

app_name = "boilerplate"

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('search/', views.search, name="search"),
    path('about.html', views.about, name='about'),
    path('store.html', views.store, name='store'),
    path('<slug>/cart/', views.cart, name="cart"),
    path('mycart/', views.mycart, name="mycart"),
    path('contact.html', views.contact, name='contact'),
    path('<slug>/', views.shop_single, name='shop_single'),
    path('checkout.html', views.checkout, name='checkout'),
    path('thankyou.html', views.thankyou, name='thankyou'),
    path('account.html', views.account, name='account'),
    path('categories/<slug>/', views.categories, name="categories"),
    path('api/products/', views.api_products, name="api_products"),

]
