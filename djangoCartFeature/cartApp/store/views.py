from django.shortcuts import render
from .models import Product, Cart, CartItem
from django.http import JsonResponse
import json
from store.function import getProducts
# Create your views here.
def index(request):
    #Deletes old products from model's database
    products = Product.objects.all().delete()
    #API request for new products
    getProducts()
    #fetches new products from model's database
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "index.html", context)

def cart(request):
    context = {}
    return render(request, "cart.html", context)


def addToCart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user,completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity +=1
        cartitem.save()
    return JsonResponse("it is working", safe=False)
 