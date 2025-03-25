from django.urls import path
from .views import * 
app_name='Cart'
urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('',cart_view, name='cart_view'),
    path('decrease/<int:item_id>/',decrease_quantity, name='decrease_quantity'),
    path('remove/<int:cart_id>/',remove_item, name='remove_item'),
    
    path('update/', update_cart, name='update_cart'),
]