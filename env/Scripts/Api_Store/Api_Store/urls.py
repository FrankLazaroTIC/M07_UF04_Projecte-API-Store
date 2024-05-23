from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# Importem totes les funcions de les views de totes les nostres apps
from client.views import add_user, get_users 
from cataleg.views import add_product, update_product, update_stock, delete_product, list_products, product_detail
from carreto.views import create_cart, add_product_to_cart, remove_product_from_cart, clear_cart, list_cart_products, purchase , list_all_carts
from comandes.views import order_history, order_history_by_client
from pagament.views import pay_order

urlpatterns = [
    path('admin/', admin.site.urls),
    # Funcions de APP Clients
    path('add_user/', add_user, name='add_user'),
    path('get_users/', get_users, name='get_users'),
    # Funcions de APP Cataleg
    path('add_product/', add_product, name='add_product'),
    path('update_product/<int:product_id>/', update_product, name='update_product'),
    path('update_stock/<int:product_id>/', update_stock, name='update_stock'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('list_products/', list_products, name='list_products'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    # Funcions de APP Carreto
    path('create_cart/<int:client_id>/', create_cart, name='create_cart'),
    path('add_product_to_cart/<int:client_id>/<int:product_id>/', add_product_to_cart, name='add_product_to_cart'),
    path('remove_product_from_cart/<int:client_id>/<int:product_id>/', remove_product_from_cart, name='remove_product_from_cart'),
    path('clear_cart/<int:client_id>/', clear_cart, name='clear_cart'),
    path('list_all_carts/', list_all_carts, name='list_all_carts') , 
    path('list_cart_products/<int:client_id>/', list_cart_products, name='list_cart_products'),
    path('purchase/<int:client_id>/', purchase, name='purchase'),
    # Funcions de APP Comandes
    path('order_history/', order_history, name='order_history'),
    path('order_history_by_client/<int:client_id>/', order_history_by_client, name='order_history_by_client'),
    # Funcions de APP Pagament
    path('pay_order/<int:order_id>/', pay_order, name='pay_order'),
]