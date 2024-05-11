from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("nome", "projeto", "data_hora")

    def nome(self, obj):
        return obj.name
    
    def projeto(self, obj):
        return obj.project
    
    def data_hora(self, obj):
        return obj.datetime


admin.site.register(Event, EventAdmin)