from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from productos.models import Presentacion, Producto


class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto


class ProductoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'descripcion']
    list_display = (
        'lote', 'presentacion', 'nombre', 'descripcion', 'fecha_expiracion', 'fecha_produccion', 'tipo',
        'precio_compra',
        'precio_venta', 'stock',)
    resource_class = ProductoResource


admin.site.register(Producto, ProductoAdmin)


class PresentacionResource(resources.ModelResource):
    class Meta:
        model = Presentacion


class PresentacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre',)
    resource_class = PresentacionResource


admin.site.register(Presentacion, PresentacionAdmin)
