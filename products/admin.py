from django.contrib import admin
from .models import offer,product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('Name','Price','Stock')
class OfferAdmin(admin.ModelAdmin):
    list_display=('Itemcode','Discount')

admin.site.register(product,ProductAdmin)
admin.site.register(offer,OfferAdmin)