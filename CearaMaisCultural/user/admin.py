from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("usuário", "cpf", "município", "é_mobilizador")

    def usuário(self, obj):
        return obj.full_name
    
    def município(self, obj):
        return obj.city
    
    @admin.display(boolean=True)
    def é_mobilizador(self, obj):
        return obj.is_staff


admin.site.register(User, UserAdmin)
