from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from django.http import Http404
from django.core.exceptions import ValidationError
from .serializers import ProductSerializer
from django.utils import timezone


#Funcionalitat per afegir un producte
@api_view(['POST'])
def add_product(request):
    try:
        product = Product.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            price=request.data['price'],
            stock=request.data['stock'],
        )
        return Response({"message": "Producte afegit correctament!!.", "product": product.name})
    except ValidationError as e:
        return Response({"message": "Error adding product.", "details": str(e)})

#Funcionalitat per actualitzar un producte
@api_view(['PUT'])
def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.name = request.data.get('name', product.name)
        product.description = request.data.get('description', product.description)
        product.price = request.data.get('price', product.price)
        product.updated_at = timezone.now()
        product.save()
        return Response({"message": "Producte actualitzat!!.", "product": str(product.name)})
    except Product.DoesNotExist:
        raise Http404

#Funcionalitat per actualitzar el stock d'un producte
@api_view(['PUT'])
def update_stock(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.stock = request.data.get('stock', product.stock)
        product.save()
        return Response({"message": "Stock actualitzat!! .", "Nou stock": str(product.stock)})
    except Product.DoesNotExist:
        raise Http404

#Funcionalitat per esborrar un producte
@api_view(['DELETE'])
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.is_deleted = True
        product.save()
        return Response({"message": "Product deleted.", "Productw esborrat": product.name})
    except Product.DoesNotExist:
        raise Http404

#Funcionalitat per llistar els productes
@api_view(['GET'])
def list_products(request):
    products = Product.objects.filter(is_deleted=False)
    product_list = [product.name for product in products]
    return Response({"message": "Llista dels productes.", "Producte": product_list})

#Funcionalitat per llistar el detall d'un producte
@api_view(['GET'])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response({"message": "Product detail.", "product": serializer.data})
    except Product.DoesNotExist:
        raise Http404