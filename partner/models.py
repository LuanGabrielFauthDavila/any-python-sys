from django.db import models


class Partner(models.Model):
    uuid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=40)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    rg_ie = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=40, unique=True)
    
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name 