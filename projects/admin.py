from django.contrib import admin
from .models import Technologies, Project

admin.site.register(Technologies)

@admin.register(Project)
class ProyectoAdmin(admin.ModelAdmin):
    filter_horizontal = ('technologies',)