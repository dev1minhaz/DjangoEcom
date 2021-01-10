from django.shortcuts import render, get_object_or_404, redirect
# authentication
from django.contrib.auth.decorators import login_required
# models
from .models import Cart, Order
from App_Shop.models import Product
# messages
from django.contrib import messages


# Create your views here.
@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    print("item:",item)
    order_item = Cart.objects.get_or_create(
        item=item, user=request.user, purchased=False)
    print("Order item object:",order_item)
    print("Order item object[0]:",order_item[0])
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    print("Order qs:",order_qs)
    # print("Order qs[0]:",order_qs[0])
    if order_qs.exists():
        order = order_qs[0]
        print("If order exists:",order)
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
            return redirect("App_Shop:home")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "This item was added to your cart")
            return redirect("App_Shop:home")
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, "This item was added to your cart!")
        return redirect("App_Shop:home")