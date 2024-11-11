from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Emails(models.Model):
    cuerpo=models.CharField(max_length=60)
    destinatario=models.ForeignKey(User,on_delete=models.CASCADE)

class Pais(models.Model):
    nombre_del_pais=models.CharField(max_length=60)
    id_user=models.ForeignKey(User,on_delete=models.CASCADE)

