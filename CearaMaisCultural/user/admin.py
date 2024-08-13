from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("usuário", "cpf", "município", "é_mobilizador", "é_comissão")

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

    def save_model(self, _, obj, form, change):
        if change:
            existing_user = User.objects.get(pk=obj.pk)
            if form.cleaned_data["password"] != existing_user.password:
                obj.set_password(form.cleaned_data["password"])
            else:
                obj.password = existing_user.password
        else:
            obj.set_password(form.cleaned_data["password"])
        obj.save()


admin.site.register(User, UserAdmin)
