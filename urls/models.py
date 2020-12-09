from django.db import models


class Url(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.name
