from django.views.generic import ListView
from .models import Product

class product_list(ListView):
    model = Product
    template_name = 'menu.html'

    def get_queryset(self):
        return Product.objects.filter(active=True)