from django.contrib import admin

from product import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ProductStock)
class ProductStockAdmin(admin.ModelAdmin):
    pass