from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("título", "categoria", "agente_cultural", "mobilizador", "status")

    def título(self, obj):
        return obj.title

    def categoria(self, obj):
        return obj.category

    def agente_cultural(self, obj):
        return obj.author

    def mobilizador(self, obj):
        return obj.promoter


admin.site.register(Project, ProjectAdmin)
