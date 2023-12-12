from django.db import models


class User(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sector_choices = [
        ('Colbun', 'Colbun'),
        ('Panimávida', 'Panimávida'),
        ('Maule sur', 'Maule sur'),
        ('La Guardia', 'La Guardia'),
        ('San Nicolas', 'San Nicolas'),
        ('Quinamavida', 'Quinamavida'),
        ('Rari', 'Rari'),
        ('Capilla Palacio', 'Capilla Palacio'),
    ]
    sector = models.CharField(max_length=15, choices=sector_choices)
    estado_choices = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(max_length=10, choices=estado_choices)
    tipo_usuario_choices = [
        ('Cliente', 'Cliente'),
        ('Funcionario', 'Funcionario'),
    ]
    tipo_usuario = models.CharField(max_length=20, choices=tipo_usuario_choices)

    def __str__(self):
        return self.nombre


class Lectura(models.Model):
    codigo_lectura = models.CharField(max_length=20, unique=True)
    usuario_realiza_lectura = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lecturas_realizadas')
    usuario_toma_lectura = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lecturas_tomadas')
    lectura = models.FloatField()

    def __str__(self):
        return f"{self.codigo_lectura} - {self.lectura}"


class Pago(models.Model):
    codigo_pago = models.CharField(max_length=20, unique=True)
    usuario_registra_pago = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pagos_registrados')
    usuario_recibe_pago = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pagos_recibidos')
    pago = models.FloatField()

    def __str__(self):
        return f"{self.codigo_pago} - {self.pago}"
