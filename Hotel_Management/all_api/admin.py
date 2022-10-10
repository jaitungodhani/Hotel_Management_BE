from django.contrib import admin
from .models import Table,Category,Item,Order,Bill
# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display=["name"]
    list_filter=["name"]
    search_fields=["name"]
    list_editable=["name"]
    list_display_links= None
admin.site.register(Table,TableAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=["name"]
    search_fields=["name"]
    list_editable=["name"]
    list_display_links=None
admin.site.register(Category,CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display=["name","category","price"]
    list_filter=["category","price"]
    search_fields=["Item"]
    list_display_links=["name"]
admin.site.register(Item,ItemAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=["id","Item","quantity","status","table","pay"]
    list_filter=["table","Item","status","pay"]
    list_editable=["pay","status"]
    list_display_links=None
    search_fields=["id","table"]
    list_display_links=["id"]
admin.site.register(Order,OrderAdmin)

class BillAdmin(admin.ModelAdmin):
    list_display=["id","table","pay","total_amount"]
    list_editable=["pay"]
    list_filter=["table","pay"]
    search_fields=["id","table"]
    list_display_links=["id"]
admin.site.register(Bill,BillAdmin)