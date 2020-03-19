from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Category, Food, Topping, Price, OrderItem, Order


def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    elif request.method == "POST":
        # if request to add item to cart
        if 'category' and 'food' and 'size' in request.POST:
            try:
                request.POST["category"]
                request.POST["food"]
                request.POST["size"]
            except:
                raise Http404("You Didn't Have a Correct Food Items In Your Cart")
            
            # load posted data into variables
            selectedcat = request.POST["category"]
            selectedfood = request.POST["food"]
            selectedsize = int(request.POST["size"])
            selectedtopping = request.POST.getlist('topping')
            
            # get instances of database tables
            cat_instance = Category.objects.filter(name=selectedcat).first()
            user_instance = User.objects.filter(username=request.user).first()
            food_instance = Food.objects.filter(name=selectedfood).first()
            price_instance = Food.objects.filter(name=selectedfood).first().price_food_id.all()[selectedsize]
            toppings_instances = {}
            for a,b in zip(selectedtopping, range(1, len(selectedtopping)+1)):
                toppings_instances[f"food_topping{b}"] = Topping.objects.filter(name=a, cat_id=cat_instance).first()

            # if user already had a not placed order(cart), place next item in cart
            if not Order.objects.filter(cust_id=user_instance, status="NP"):
                order = Order(cust_id=request.user, status="NP")
                order.save()

            # continue: get instances of database tables
            order_instance = Order.objects.filter(cust_id=user_instance, status="NP").first()
            
            # save order items with any possible topping
            if len(selectedtopping) == 0:
                orderitem = OrderItem(order_id=order_instance, food_id=food_instance, food_price=price_instance)
                orderitem.save()
            elif len(selectedtopping) == 1:
                orderitem = OrderItem(order_id=order_instance, food_id=food_instance, food_price=price_instance, food_topping1=toppings_instances["food_topping1"])
                orderitem.save()
            elif len(selectedtopping) == 2:
                orderitem = OrderItem(order_id=order_instance, food_id=food_instance, food_price=price_instance, food_topping1=toppings_instances["food_topping1"], food_topping2=toppings_instances["food_topping2"])
                orderitem.save()
            elif len(selectedtopping) == 3:
                orderitem = OrderItem(order_id=order_instance, food_id=food_instance, food_price=price_instance, food_topping1=toppings_instances["food_topping1"], food_topping2=toppings_instances["food_topping2"], food_topping3=toppings_instances["food_topping3"])
                orderitem.save()
            elif len(selectedtopping) == 5:
                orderitem = OrderItem(order_id=order_instance, food_id=food_instance, food_price=price_instance, food_topping1=toppings_instances["food_topping1"], food_topping2=toppings_instances["food_topping2"], food_topping3=toppings_instances["food_topping3"], food_topping4=toppings_instances["food_topping4"], food_topping5=toppings_instances["food_topping5"])
                orderitem.save()

            return redirect("index")
        # if request to place an order
        else:
            if Order.objects.filter(cust_id=request.user, status='NP').first():
                order = Order.objects.filter(cust_id=request.user, status='NP').first()
            else :
                message = {"message": "you dont have food items in your cart yet", "category": "danger"}
                raise Http404("You Didn't Have Food Items In Your Cart")
            order.status = 'PL'
            order.save()
    # if get request
    context = {
    "user": request.user,
    "cats": Category.objects.all(),
    "foods": Food.objects.all(),
    "toppings": Topping.objects.all(),
    "prices": Price.objects.all(),
    }
    # check if user has (not placed) order and return items his cart
    try:
        context["fooditems"] = Order.objects.filter(cust_id=request.user.id, status="NP").first().order_id.all()
        context["total"] = 0
        for i in context["fooditems"]:
            context["total"] += i.food_price.price
    except AttributeError :
        pass
    # check if user has (placed) orders and return orders
    try:
        context["posted_orders"] = Order.objects.filter(cust_id=request.user.id).exclude(status="NP").all()
    except:
        pass
    return render(request, "index.html", context)


@login_required
def orders_view(request, orderid):
    # 
    try:
        posted_order = Order.objects.filter(id=orderid, cust_id=request.user.id).exclude(status="NP").first()
    except:
        raise Http404("You don't have orders yet")

    context = {
    "posted_order": posted_order
    }

    # check if user has (placed) orders and return orders
    try:
        context["posted_orders"] = Order.objects.filter(cust_id=request.user.id).exclude(status="NP").all()
    except:
        pass

    try:
        context["fooditems"] = Order.objects.filter(cust_id=request.user.id, id=orderid).first().order_id.all()
    except:
        raise Http404("You don't have an order with this no")

    context["total"] = 0
    for i in context["fooditems"]:
        context["total"] += i.food_price.price
    return render(request, "orders.html", context)