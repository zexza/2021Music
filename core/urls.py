from django.urls import path
from .views import home, login, cart, productlist, productdetail,myaccount, contact, checkout, webpay_plus_commit,add_product_catalogo,add_product_carrito,decrement_product,remove_product,clear_cart

urlpatterns = [
    path('', home, name="home"),
    path('index.html', home, name="home"),
    path('login.html', login, name="login"),
    path('cart.html', cart, name="cart"),
    path('product-list.html', productlist, name="productlist"),
    path('product-detail.html', productdetail, name="productdetail"),
    path('my-account.html', myaccount, name="my-account"),
    path('contact.html', contact, name="contact"),
    path('checkout.html', checkout, name="checkout"),
    path('terminal.html', webpay_plus_commit),

    path('decrement_product/<int:product_id>/', decrement_product, name='decrement_product'),
    path('add_product_carrito/<int:product_id>/', add_product_carrito, name='add_product_carrito'),
    path('add_product_catalogo/<int:product_id>/', add_product_catalogo, name='add_product_catalogo'),
    path('remove_product/<int:product_id>/', remove_product, name='remove_product'),
    path('clear/', clear_cart, name='clear_cart'),
]
