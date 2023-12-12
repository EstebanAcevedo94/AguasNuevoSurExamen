from django.contrib import admin


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
