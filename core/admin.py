from django.contrib import admin
from .models import Categoria, Marca, Producto, carrito
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "cantidad", "marca"]
    list_editable = ["precio", "cantidad"]
    search_fields = ["nombre"]
    list_filter = ["marca"]
    list_per_page = 10


admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(carrito)