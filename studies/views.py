from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Product


def home(request):
    return render(request, 'home.html')


def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})


@login_required
def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    lessons = product.lesson_set.order_by('id').all()
    return render(request, 'detail.html', {"lessons": lessons})
