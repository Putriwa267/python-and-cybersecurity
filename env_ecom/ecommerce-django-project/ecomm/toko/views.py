from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.views import generic

from .models import ProdukItem, OrderProdukItem, Order

class HomeListView(generic.ListView):
    template_name = 'home.html'
    queryset = ProdukItem.objects.all()
    paginate_by = 4

class ProductDetailView(generic.DetailView):
    template_name = 'product_detail.html'
    queryset = ProdukItem.objects.all()

class CheckoutView(generic.TemplateView):
    template_name = 'checkout.html'

