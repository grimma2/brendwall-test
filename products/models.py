from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name
