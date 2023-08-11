from django.db import models


class DemandTechnology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name.title()
