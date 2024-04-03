from django.shortcuts import render
from api.models import Product, Category
from django.http import JsonResponse

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    data = {'products':list(products.values())}
    return JsonResponse(data)

def product(request, id):
    product = Product.objects.get(id = id)
    data = {
        'product': {
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'is_active': product.is_active,
            'category_id': product.category_id
        }
    }
    return JsonResponse(data)

def categories_list(request):
    categories = Category.objects.all()
    data = {'categories':list(categories.values())}
    return JsonResponse(data)

def category(request, id):
    category = Category.objects.get(id = id)
    data = {'category': {
        'name': category.name,
    }}
    return JsonResponse(data)

def products_in_category(request, id):
    products = Product.objects.filter(category_id=id)
    data = {'products': list(products.values())}
    return JsonResponse(data)