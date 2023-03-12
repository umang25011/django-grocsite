
from django.urls import path
from . import views
from .views import OrdersList, OrdersCreate

app_name = 'myapp1'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:type_no>/', views.detail, name='details'),
    path('orders/', OrdersList.as_view(), name="list_details"),
    path('c-orders/<int:user_id>/<int:item_id>', OrdersCreate.as_view(), name="create_order"),
    path("order/", views.order, name="order"),
    path("placeorder/", views.placeorder, name="placeorder"),
    path("items/", views.items, name="items"),
]
