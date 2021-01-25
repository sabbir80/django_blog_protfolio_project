from django.db import models


# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title
