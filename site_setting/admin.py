from django.contrib import admin
from . import models
# Register your models here.


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'is_active']
    list_editable = ['url', 'is_active']


admin.site.register(models.SiteSetting)
admin.site.register(models.Slider, SliderAdmin)
