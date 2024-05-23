from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client

# Funcionalitat per afegir un usuari
@api_view(['POST'])
def add_user(request):
    # Obtenim les dades de l'usuari des de la petició
    data = request.data
    # Creem un nou usuari amb les dades rebudes
    new_user = Client(
        nom=data['nom'],
        cognoms=data['cognoms'],
        email=data['email'],
        password=data['password']
    )
    # Guardem l'usuari a la base de dades
    new_user.save()
    # Retornem una resposta indicant que l'usuari s'ha afegit correctament
    return Response({"status": "success", "message": "User added successfully."})

# Funcionalitat per obtenir tots els usuaris
@api_view(['GET'])
def get_users(request):
    # Obtenim tots els usuaris de la base de dades
    users = Client.objects.all().values('id', 'nom', 'cognoms', 'email')
    # Retornem una resposta amb la llista d'usuaris
    return Response({"status": "success", "users": list(users)})