import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from comandes.models import Order
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

# Funció per validar el format del número de la targeta
def validate_card_number(value):
    card_number_regex = r'^[0-9]{16}$'
    if not re.match(card_number_regex, value):
        raise ValidationError("Invalid card number format.")

# Funcionalitat per pagar una comanda
@api_view(['POST'])
def pay_order(request, order_id):
    # Obtenim les dades de la targeta des de la petició
    card_number = request.data.get('card_number')
    expiry_date = request.data.get('expiry_date')
    cvc = request.data.get('cvc')

    # Comprovem que totes les dades de la targeta estan presents
    if not all([card_number, expiry_date, cvc]):
        return Response({"message": "Missing card details."})
    
    # Validem el número de la targeta
    try:
        validate_card_number(card_number)
    except ValidationError as e:
        # Si el número de la targeta no és vàlid, retornem un missatge d'error
        return Response({"message": str(e)})

    # Obtenim la comanda que es vol pagar
    order = get_object_or_404(Order, id=order_id)

    # Retornem una resposta indicant que el pagament s'ha processat correctament
    return Response({"message": "Payment processed.", "order": {"id": order.id}})