from django.db import models
#si no carga las tablas en la base de datos usar:
#python manage.py makemigrations "certamen3App"

class CoffeeForm(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=100, primary_key=True)
    tipo_solicitud = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=200)
    #EN ALGUNAS PARTES DEL CODIGO EL NOMBRE DEL OBJETO SE MOSTRABA COMO GENERICO, EJ:MARCA OBJECT(NISSAN)
    #PARA SOLUCIONAR ESTO HACER LO SIGUIENTE:
    def __str__(self):
        titulo = self.tipo_solicitud+" - "+self.correo
        return titulo