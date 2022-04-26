from django.db import models

# Create your models here.
class BookData(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release = models.IntegerField()
    num_pages = models.IntegerField()
    publi_company = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title