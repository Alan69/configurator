from django.contrib import admin
from .models import Region, Urls, City
# Register your models here.

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','region_code', 'url')

admin.site.register(Region, RegionAdmin)
admin.site.register(Urls)
admin.site.register(City)