from django.http import HttpResponse
from django.views import View

from .models import Type, Item, Client, OrderItem
from django.shortcuts import get_object_or_404, render
from .forms import BookForm, OrderItemForm
import calendar


def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index.html', {'type_list': type_list})


def about(request):
    return render(request, "myapp1/about.html")


def detail(request, type_no):
    typename = get_object_or_404(Type, id=type_no)
    item_list = Item.objects.filter(type=typename)

    return render(request, "myapp1/detail.html", {"typename": typename, "item_list": item_list})


class OrdersList(View):
    def get(self, request):
        users = Client.objects.all()
        items = Item.objects.all()
        response = HttpResponse()
        users_html = "<h1>Users</h1> <p>"
        for user in users:
            users_html += str(user.id) + " : " + user.get_full_name() + " <br/>"

        users_html += "</p>"
        response.write(users_html)
        items_html = "<h1>Items</h1> <p>"
        for item in items:
            items_html += str(item.id) + " : " + item.name + " <br/>"

        items_html += "</p>"
        response.write(items_html)
        return response


class OrdersCreate(View):
    def get(self, request, user_id, item_id):
        client = get_object_or_404(Client, id=user_id)
        item = get_object_or_404(Item, id=item_id)
        new_order = OrderItem(client=client, item=item)
        new_order.save()

        response = HttpResponse()
        response.write(f"Order of {item.name} by {client.get_full_name()} Placed Successfully")

        return response


def order(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        print("Not Cleaned Data: ")
        print(form)
        # print(form.cleaned_data)
        if form.is_valid():
            print("Cleaned Data: ")
            print(form.cleaned_data)
            message = f"Your Order of book: {form.cleaned_data['title']} Successful"
            myform = BookForm()
            return render(request, "myapp1/order.html", {"myform": myform, "message": message})
    else:
        myform = BookForm()
        return render(request, "myapp1/order.html", {"myform": myform})


def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp1/items.html', {'itemlist': itemlist})

def placeorder(request):
    if request.method == "POST":
        form = OrderItemForm(request.POST)
        form.save()
        if form.is_valid():
            print(form.cleaned_data)
            new_form = OrderItemForm()
            return render(request, "myapp1/placeorder.html", {"form": new_form, "message" : f"Order of {form.cleaned_data['item'].name} Placed Successfully"})
    else:
        form = OrderItemForm()
        return render(request, "myapp1/placeorder.html", {"form": form})

# original function-based view orders was handling a single HTTP GET request. When converting this to a class-based view,
# we created a new class OrderView that inherits from Django's built-in View class. We then defined a get method within '
# this class to handle the HTTP GET request.
# The get method performed the same functionality, but in a more cleaner way as the same class would be able to handle
# future POST, PUT, and DELETE methods in the same class.
# Also, we only need to register the Class only once in urls.py instead of for every request.
