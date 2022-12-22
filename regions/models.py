from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return self.city_name

class Urls(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url
    
    class Meta:
        verbose_name_plural = "Urls"

class Region(models.Model):
    belong_city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    region_code = models.CharField(max_length=255)
    url = models.ForeignKey(Urls, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name