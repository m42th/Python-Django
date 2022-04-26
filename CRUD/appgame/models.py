from django.db import models

# Create your models here.
class GameData(models.Model):
    title = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    release = models.IntegerField()
    platform = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title