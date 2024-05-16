
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from cataleg.views import add_product, update_product, update_stock, delete_product, list_products, product_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_product/', add_product, name='add_product'),
    path('update_product/<int:product_id>/', update_product, name='update_product'),
    path('update_stock/<int:product_id>/', update_stock, name='update_stock'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('list_products/', list_products, name='list_products'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
]