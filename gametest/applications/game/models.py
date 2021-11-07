from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.title}'


class Platform(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.title}'


class Game(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField(default=2010)
    studio = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='game')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='platform')


    def __str__(self):
        return f'{self.title} {self.year} \n {self.studio} {self.genre} \n {self.platform}'