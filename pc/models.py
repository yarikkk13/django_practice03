from django.db import models


# Create your models here.
class PC(models.Model):
    class Meta:
        db_table = 'PCs'
        verbose_name = 'PC'

    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    ram = models.IntegerField()
    cpu = models.IntegerField()
    display = models.IntegerField()
