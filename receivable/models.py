from django.db import models


class Receivable(models.Model):
    total = models.FloatField(blank=False, default=0)


    def __str__():
        pass