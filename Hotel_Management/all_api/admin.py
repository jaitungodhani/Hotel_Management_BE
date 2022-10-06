from django.contrib import admin
from .models import Table
# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display=["name"]
    list_filter=["name"]
    search_fields=["name"]
    list_editable=["name"]
    list_display_links= None
admin.site.register(Table,TableAdmin)