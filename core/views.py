from core.models import Categoria

from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import Prodform


from .cart import Cart
from .models import Categoria, Producto
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction

# Create your views here.

def home(request):

    allCategoria = Categoria.objects.all()
    data = {
        'allCategoria' : allCategoria
    }
    return render(request, 'core/home.html', data)


def login(request):

    return render(request, 'core/login.html')

def cart(request):
    total = 0
    FprecioC = 0
    buy_order = str(1)
    session_id = str(1)
    return_url = 'http://127.0.0.1:8000/terminal.html'
    for key, value in request.session['cart'].items():
            total = total + (float(value['price']) * value['quantity'])
            # FprecioC=(f'{total:.3f}')
            FprecioC= int(total)
    amount = FprecioC
    try:
        response = Transaction().create(buy_order, session_id, amount, return_url)
        print(amount)
        return render(request, 'core/cart.html', {"response":response})
    except TransbankError as e:
        print(e.message)
        return render(request, 'core/cart.html', {})


def productlist(request):
    allProducto = Producto.objects.all()
    data = {
        'allProducto' : allProducto
    }
    return render(request, 'core/product-list.html', data)

def productdetail(request):

    return render(request, 'core/product-detail.html')

def myaccount(request):

    return render(request, 'core/my-account.html') 
      
def contact(request):

    return render(request, 'core/contact.html') 
          
def checkout(request):

    return render(request, 'core/checkout.html') 




def webpay_plus_commit(request):
    token = request.POST.get("token_ws")
    response = Transaction.commit(token)
    return render(request, 'core/terminal.html', {"response":response,"token":token})
    

#carrito def



@csrf_protect
def add_product_catalogo(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("/product-list.html")


def add_product_carrito(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)    
    cart.add(product=product)        
    return redirect("/cart.html")


@csrf_protect
def decrement_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect("/cart.html")




@csrf_protect
def remove_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.remove(product)
    return redirect("/cart.html")




@csrf_protect
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/cart.html")


    

