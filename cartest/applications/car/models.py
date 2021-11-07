from django.db import models


class Model(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'

class Brand(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'


class Car(models.Model):
    title = models.CharField(max_length=50)
    year = models.PositiveIntegerField(default=None)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name=None)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name=None)

    def __str__(self):
        return f'{self.brand} {self.title} {self.model} {self.year}'