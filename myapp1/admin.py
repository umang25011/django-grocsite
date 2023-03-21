from django.contrib import admin
from django.db import models
from .models import Type, Item, Client, OrderItem, Description

@admin.action(description="First Name Cap")
def firstNameUpper(obj):
    return obj.first_name.upper()

@admin.action(description="Change City")
def changeCity(modeladmin, request, queryset):
    queryset.update(city="CH")

@admin.action(description="Delete Action")
def delete_action(modeladmin, request, queryset):
    actions = super().get_actions(request)
    print(actions)
    if "delete_action" in actions:
        del actions["delete_action"]
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', firstNameUpper, 'last_name', "city", "local_client")
    ordering = ["first_name"]
    actions = [changeCity, delete_action]

class ItemInline(admin.TabularInline):
    model = Item

class TypeAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

# Register your models here.
admin.site.register(Type, TypeAdmin)
admin.site.register(Item)
admin.site.register(Client, ClientAdmin)
admin.site.register(OrderItem)
admin.site.register(Description)