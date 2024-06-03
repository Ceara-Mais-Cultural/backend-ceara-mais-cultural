from django.contrib import admin
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("usuário", "cpf", "município", "é_mobilizador", 'é_comissão')

    def usuário(self, obj):
        return obj.full_name

    def município(self, obj):
        return obj.city

    @admin.display(boolean=True)
    def é_mobilizador(self, obj):
        return obj.is_staff
    
    @admin.display(boolean=True)
    def é_comissão(self, obj):
        return obj.is_superuser

    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

        if not change:
            Token.objects.create(user=obj)


admin.site.register(User, UserAdmin)
