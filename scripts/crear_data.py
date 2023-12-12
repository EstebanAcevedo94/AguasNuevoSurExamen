import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AguasNuevoSur.settings")

from faker import Faker
from sistema_web.models import *

fake = Faker('es_ES')  # Configurando Faker para usar el idioma español


def generar_usuario():
    rut = fake.unique.random_int(min=10000000, max=99999999)  # Ejemplo de generación de un rut aleatorio
    nombre = fake.first_name()
    apellido = fake.last_name()
    sector = fake.random_element(elements=(
    'Colbun', 'Panimávida', 'Maule sur', 'La Guardia', 'San Nicolas', 'Quinamavida', 'Rari', 'Capilla Palacio'))
    estado = fake.random_element(elements=('Activo', 'Inactivo'))
    tipo_usuario = 'Cliente'

    return User.objects.create(rut=rut, nombre=nombre, apellido=apellido, sector=sector, estado=estado,
                               tipo_usuario=tipo_usuario)


def generar_lectura(usuario_realiza, usuario_toma):
    codigo_lectura = fake.unique.uuid4()
    lectura = fake.random_float(min=0, max=100)

    return Lectura.objects.create(codigo_lectura=codigo_lectura, usuario_realiza_lectura=usuario_realiza,
                                  usuario_toma_lectura=usuario_toma, lectura=lectura)


def generar_pago(usuario_registra, usuario_recibe):
    codigo_pago = fake.unique.uuid4()
    pago = fake.random_float(min=0, max=1000)

    return Pago.objects.create(codigo_pago=codigo_pago, usuario_registra_pago=usuario_registra,
                               usuario_recibe_pago=usuario_recibe, pago=pago)


# Generar datos ficticios
for _ in range(10):  # Puedes ajustar la cantidad de registros que deseas generar
    usuario_realiza = generar_usuario()
    usuario_toma = generar_usuario()
    generar_lectura(usuario_realiza, usuario_toma)
    generar_pago(usuario_realiza, usuario_toma)

print("Datos ficticios generados exitosamente.")

if __name__ == '__main__':
    generar_usuario()
    generar_lectura()
    generar_pago()