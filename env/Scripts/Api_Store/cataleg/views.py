from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from django.http import Http404
from django.core.exceptions import ValidationError
from .serializers import ProductSerializer
from django.utils import timezone

# Funcionalitat per afegir un producte
@api_view(['POST'])
def add_product(request):
    try:
        # Creem un nou producte amb les dades rebudes
        product = Product.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            price=request.data['price'],
            stock=request.data['stock'],
        )
        # Si tot ha anat bé, retornem un missatge de confirmació
        return Response({"message": "Producte afegit correctament!!.", "product": product.name})
    except ValidationError as e:
        # Si hi ha hagut algun error de validació, el retornem
        return Response({"message": "Error adding product.", "details": str(e)})

# Funcionalitat per actualitzar un producte
@api_view(['PUT'])
def update_product(request, product_id):
    try:
        # Obtenim el producte que volem actualitzar
        product = Product.objects.get(id=product_id)
        # Actualitzem les seves dades amb les que ens han passat
        product.name = request.data.get('name', product.name)
        product.description = request.data.get('description', product.description)
        product.price = request.data.get('price', product.price)
        product.updated_at = timezone.now()
        product.save()
        # Si tot ha anat bé, retornem un missatge de confirmació
        return Response({"message": "Producte actualitzat!!.", "product": str(product.name)})
    except Product.DoesNotExist:
        # Si el producte no existeix, retornem un error
        raise Http404

# Funcionalitat per actualitzar el stock d'un producte
@api_view(['PUT'])
def update_stock(request, product_id):
    try:
        # Obtenim el producte que volem actualitzar
        product = Product.objects.get(id=product_id)
        # Actualitzem el seu stock amb el que ens han passat
        product.stock = request.data.get('stock', product.stock)
        product.save()
        # Si tot ha anat bé, retornem un missatge de confirmació
        return Response({"message": "Stock actualitzat!! .", "Nou stock": str(product.stock)})
    except Product.DoesNotExist:
        # Si el producte no existeix, retornem un error
        raise Http404

# Funcionalitat per esborrar un producte
@api_view(['DELETE'])
def delete_product(request, product_id):
    try:
        # Obtenim el producte que volem esborrar
        product = Product.objects.get(id=product_id)
        # Marquem el producte com a esborrat
        product.is_deleted = True
        product.save()
        # Si tot ha anat bé, retornem un missatge de confirmació
        return Response({"message": "Product deleted.", "Productw esborrat": product.name})
    except Product.DoesNotExist:
        # Si el producte no existeix, retornem un error
        raise Http404

# Funcionalitat per llistar els productes
@api_view(['GET'])
def list_products(request):
    # Obtenim tots els productes que no estan esborrats
    products = Product.objects.filter(is_deleted=False)
    # Creem una llista amb els noms dels productes
    product_list = [product.name for product in products]
    # Retornem la llista de productes
    return Response({"message": "Llista dels productes.", "Producte": product_list})

# Funcionalitat per llistar el detall d'un producte
@api_view(['GET'])
def product_detail(request, product_id):
    try:
        # Obtenim el producte del qual volem el detall
        product = Product.objects.get(id=product_id)
        # Creem un serialitzador per aquest producte
        serializer = ProductSerializer(product)
        # Retornem el detall del producte
        return Response({"message": "Product detail.", "product": serializer.data})
    except Product.DoesNotExist:
        # Si el producte no existeix, retornem un error
        raise Http404