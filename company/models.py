from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    uuid = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    slug = models.CharField(max_length=250, blank=False)
    name = models.CharField(max_length=40)
    fantasy = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20, unique=True)
    ie = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=40, unique=True)
    pix_key = models.CharField(max_length=19, blank=True, null=True, default="")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class CompanyWorker(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    cpf = models.CharField(max_length=14, blank=False)
    rg = models.CharField(max_length=14, blank=False)
    phone_number = models.CharField(max_length=14, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ("user",)