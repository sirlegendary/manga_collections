from django.db import models

class MangaCollection(models.Model):
    name  = models.CharField(max_length=200)
    url   = models.CharField(max_length=250)

    def __str__(self):
        return self.name
