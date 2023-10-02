from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:products_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:products_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:products_id>/',views.full_remove,name='full_remove'),
]