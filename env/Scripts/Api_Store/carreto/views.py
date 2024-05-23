from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from cataleg.models import Product
from comandes.models import Order
from client.models import Client
from .models import Cart

@api_view(['POST'])
# Crear un carretó per al client
def create_cart(request, client_id):
    client = Client.objects.filter(id=client_id).first() 
    # Comprovar si el client existeix
    if not client:
        return Response({"status": "error", "message": "No hem trovat al client"}, status=404)
    # Crear un nou carretó per al client
    cart = Cart.objects.create(client=client)
    return Response({"status": "success", "message": "Carretó creat", "Carreto número": str(cart)})

@api_view(['POST'])
# Afegir un producte al carretó del client
def add_product_to_cart(request, client_id, product_id):
    client = Client.objects.filter(id=client_id).first()
    # Comprovar si el client existeix
    if not client:
        return Response({"status": "error", "message": "No hem trovat al client"}, status=404)
    cart = Cart.objects.filter(client=client).first()
    # Comprovar si el carretó existeix
    if not cart:
        return Response({"status": "error", "message": "Cart not found."}, status=404)
    product = Product.objects.filter(id=product_id).first()
    # Comprovar si el producte existeix
    if not product:
        return Response({"status": "error", "message": "Product not found."}, status=404)
    # Comprovar si el producte està en estoc
    if product.stock <= 0:
        return Response({"status": "error", "message": "Producte sense stock"})
    # Afegir el producte al carretó
    cart.products.add(product)
    return Response({"status": "success", "message": "Producte afegit al carretó", "Carreto número": str(cart)})

@api_view(['DELETE'])
# Eliminar un producte del carretó del client
def remove_product_from_cart(request, client_id, product_id):
    cart = Cart.objects.filter(client_id=client_id).first()
    # Comprovar si el carretó existeix
    if not cart:
        return Response({"status": "error", "message": "Cart not found."}, status=404)
    product = Product.objects.filter(id=product_id).first()
    # Comprovar si el producte existeix
    if not product:
        return Response({"status": "error", "message": "Product not found."}, status=404)
    # Eliminar el producte del carretó
    cart.products.remove(product)
    return Response({"status": "success", "message": "Producte eliminat del carretó", "Carretó número": str(cart)})

@api_view(['DELETE'])
# Netejar el carretó del client
def clear_cart(request, client_id):
    cart = Cart.objects.filter(client_id=client_id).first()
    # Comprovar si el carretó existeix
    if not cart:
        return Response({"status": "error", "message": "Cart not found."}, status=404)
    # Netejar el carretó
    cart.products.clear()
    return Response({"status": "success", "message": "Carretó netejat", "Carretó número": str(cart)})

@api_view(['GET'])
# Llistar els productes del carretó del client
def list_cart_products(request, client_id):
    cart = Cart.objects.filter(client_id=client_id).first()
    # Comprovar si el carretó existeix
    if not cart:
        return Response({"status": "error", "message": "Cart not found."}, status=404)
    # Obtenir els productes del carretó
    products = cart.products.all()
    return Response({"status": "success", "message": "Productes del carretó", "Productes": [product.name for product in products]})

@api_view(['POST'])
# Realitzar una compra amb el carretó del client
def purchase(request, client_id):
    cart = Cart.objects.filter(client_id=client_id).first()
    # Comprovar si el carretó existeix
    if not cart:
        return Response({"status": "error", "message": "Cart not found."}, status=404)
    # Crear una nova comanda amb el carretó
    order = Order.objects.create(cart=cart)
    
    # Obtenir els productes del carretó per a la comanda
    products = [{"name": product.name, "price": product.price} for product in cart.products.all()]
    
    return Response({"status": "success", "message": "Compra feta", "Ticket": products})

@api_view(['GET'])
# Llistar tots els carrets
def list_all_carts(request):
    carts = Cart.objects.all()
    return Response({"status": "success", "Carretós": [str(cart) for cart in carts]})