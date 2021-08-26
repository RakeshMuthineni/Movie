from django.contrib import admin
from .models import Cinima_Info

# Register your models here.
class CinimaAdmin(admin.ModelAdmin):

    list_display = [f.name for f in Cinima_Info._meta.fields]
admin.site.register(Cinima_Info,CinimaAdmin)

