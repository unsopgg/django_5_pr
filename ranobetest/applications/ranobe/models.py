from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'


class Tags(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'


class Type(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'


class Ranobe(models.Model):
    title = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name=None)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name=None)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name=None)

    def __str__(self):
        return f'{self.title} {self.genre} {self.type}'