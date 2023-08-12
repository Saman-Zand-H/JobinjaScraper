from django.db import models


class DemandTechnology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name.title()
    
    class Meta:
        verbose_name_plural = "Demand Technologies"
        
    def save(self, *args, **kwargs):
        # to avoid having typos for names, like back-end instead of backend
        self.name.replace("-", "").strip().lower()
        if self.name.isascii():
            return super().save(*args, **kwargs)
