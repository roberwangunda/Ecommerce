from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from Main_App.models import Product, OrderItem, DeliveryInformation, Order, Category, Images, Description_header
import json
import datetime
from django.shortcuts import get_object_or_404


def home_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        category = Category.objects.all()
        products_latest = Product.objects.order_by('pk')[:1]
        products_picked = Product.objects.all().order_by('-pk')[:1]
        descriptions = Description_header.objects.all()
        slider = Product.objects.all()[3]
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']

    context = {
        'slider':slider,
        'order': order, 
        'cartItems': cartItems, 
        'category':category, 
        'products_latest': products_latest, 
        'products_picked': products_picked,
        'descriptions': descriptions
    }
    
    return render(request, "home.html", context)




def product_view(request):
    # products = Product.objects.all()[:5]
    # one_entry = Entry.objects.get(pk=1)
    products_latest = Product.objects.order_by('pk')[:5]
    products_picked = Product.objects.all().order_by('-pk')[:3]
    kitchen = Product.objects.filter(category__name='refrigeratipn')[:3]
    products= Product.objects.filter(category__name='pastry and baking')

    context = {
        'products': products,
        'products_latest': products_latest,
        'products_picked': products_picked,
        'kitchen': kitchen
    }
    return render(request, "product.html", context)
