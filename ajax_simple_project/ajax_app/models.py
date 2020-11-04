from django.db import models


# Create your models here.

class Utilizador(models.Model):

    username = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'UTILIZADOR'
        verbose_name = 'UTILIZADOR'
        verbose_name_plural = 'UTILIZADORES'

    def __str__(self):
        return self.username
