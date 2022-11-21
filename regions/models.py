from django.db import models


class Urls(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Urls"

class Region(models.Model):
    name = models.CharField(max_length=255)
    region_code = models.CharField(max_length=255)
    url = models.ForeignKey(Urls, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name