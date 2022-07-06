from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from Main_App.models import Product, OrderItem, DeliveryInformation, Order, Category, Images, Description_header
import json
import datetime
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView


# Create your views here.

#  def home_view(request, *args, **kwargs):
#     return render(request,"home.html", {})

def contact_view(request, *args, **kwargs):
    context = {}
    return render(request, "contact.html", context)


def about_view(request, *args, **kwargs):
    my_content = {
        "my_title": "this is about us",
        "my_number": 123
    }

    return render(request, "about.html", my_content)

def checkout_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)


def cart_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(
    #         customer=customer, complete=False)
    #     total = float(['form']['total'])
    #     order.tansaction_id = transaction_id

    #     if total == float(order.get_cart_total):
    #         order.complete=True
    #     order.save()
    
        # if order.delivery ==True:
        #     deliveryAddress.objects.create(
        #         customer=customer,
        #         order=order,
        #         address=data['delivery']['address'],
        #         estate=data['delivery']['estate'],
        #         apartment=data['delivery']['apartment'],
        #     )
    # else:
    #     print('User is not logged in..')
    return JsonResponse('payment complete', safe=False)

def show_category(request, slug, id):
    # category = Category.objects.all()
    category = Category.objects.filter(id= id)
    context = { 
        # 'products': products, 
        'category':category
    }
    return HttpResponse(category)

def productDetail_view(request, slug, id):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    context = { 
        'product':product, 
        'category':category
    }
    return render(request, "product_detail.html", context)

def search_view(request):
    return render(request, 'search.html', {})

















