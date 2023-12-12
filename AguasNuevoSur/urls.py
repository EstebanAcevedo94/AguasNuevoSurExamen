from django.contrib import admin
from django.urls import path

from sistema_web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ver_clientes, name='ver_clientes'),
    path('agregar_cliente/', agregar_cliente, name='agregar_cliente'),
    path('modificar_cliente/<str:rut>/', modificar_cliente, name='modificar_cliente'),
    path('ver_lecturas/', ver_lecturas, name='ver_lecturas'),
    path('registrar_lectura/', registrar_lectura, name='registrar_lectura'),
    path('ver_pagos/', ver_pagos, name='ver_pagos'),
    path('registrar_pago/', registrar_pago, name='registrar_pago'),
]
