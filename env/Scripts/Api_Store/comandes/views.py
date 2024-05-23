from rest_framework.decorators import api_view
from rest_framework.response import Response
from cataleg.models import Product
from .models import Order
from django.contrib.auth.models import User
from django.db.models import Sum, F
from django.shortcuts import get_object_or_404
from client.models import Client

# Funcionalitat per obtenir l'historial de comandes
@api_view(['GET'])
def order_history(request):
    # Obtenim les 10 últimes comandes
    orders = Order.objects.all()[:10]
    # Creem una llista amb les dades de cada comanda
    order_data = [{"id": order.id, "total_products": order.cart.cartitem_set.count(), "total_price": order.cart.cartitem_set.aggregate(total_price=Sum(F('product__price')*F('quantity')))['total_price']} for order in orders]
    # Retornem una resposta amb l'historial de comandes
    return Response({"status": "success", "message": "Order history retrieved.", "orders": order_data})

# Funcionalitat per obtenir l'historial de comandes d'un client específic
@api_view(['GET'])
def order_history_by_client(request, client_id):
    # Obtenim el client pel qual volem l'historial de comandes
    client = get_object_or_404(Client, id=client_id)
    # Obtenim les 10 últimes comandes del client
    orders = Order.objects.filter(cart__client=client)[:10]
    # Creem una llista amb les dades de cada comanda
    order_data = [{"id": order.id, "total_products": order.cart.cartitem_set.count(), "total_price": order.cart.cartitem_set.aggregate(total_price=Sum(F('product__price')*F('quantity')))['total_price']} for order in orders]
    # Retornem una resposta amb l'historial de comandes del client
    return Response({"status": "success", "message": "Order history for client retrieved.", "orders": order_data})