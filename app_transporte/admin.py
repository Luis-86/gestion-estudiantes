from django.contrib import admin

from .models import *

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('idEMPRESA','nombre', 'direccion', 'correo','telefono','fk_gerente')
    search_fields = ['nombre']

class BusAdmin(admin.ModelAdmin):
    list_display = ('idBUS','capacidad', 'num_bus', 'estado','climatizado','fk_empresa')
    search_fields = ['num_bus']

class RutaAdmin(admin.ModelAdmin):
    list_display = ('idRUTA','region', 'descripcion')
    search_fields = ['region']

class ViajeAdmin(admin.ModelAdmin):
    list_display = ('idVIAJE','origen', 'destino', 'fecha_hora','precio','clase','cupo', 'fk_bus', 'fk_ruta')
    search_fields = ['origen']

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('idUSUARIOS','user', 'name', 'lastname','email')
    search_fields = ['name']


admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(Ruta, RutaAdmin)
admin.site.register(Viaje, ViajeAdmin)
admin.site.register(Usuarios, UsuariosAdmin)




