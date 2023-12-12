from django.contrib import admin
from .models import *
from scripts.crear_data import generar_lectura,generar_pago,generar_usuario

generar_pago()
generar_usuario()
generar_lectura()


class User_Admin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'sector', 'estado', 'tipo_usuario')
    search_fields = ['rut']
    list_filter = ('rut', 'nombre', 'apellido', 'sector', 'estado', 'tipo_usuario')


class Lectura_Admin(admin.ModelAdmin):
    list_display = ('codigo_lectura', 'usuario_realiza_lectura', 'usuario_toma_lectura')
    search_fields = ['codigo_lectura']
    list_filter = ('codigo_lectura', 'usuario_realiza_lectura', 'usuario_toma_lectura')


class Pago_Admin(admin.ModelAdmin):
    list_display = ('codigo_pago', 'usuario_registra_pago', 'usuario_recibe_pago', 'pago')
    search_fields = ['codigo_pago', 'usuario_registra_pago']
    list_filter = ('codigo_pago', 'usuario_registra_pago', 'usuario_recibe_pago', 'pago')

admin.site.register(User, User_Admin)
admin.site.register(Lectura, Lectura_Admin)
admin.site.register(Pago, Pago_Admin)