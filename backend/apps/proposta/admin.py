from django.contrib import admin

from .models import Formulario, Campo, Registro, PropostaRegistro


# Register your models here.
@admin.register(Formulario)
class AdminFormulario(admin.ModelAdmin):
    fields = ("status", "created_at")
    list_display = ("id", "status", "created_at")


@admin.register(Campo)
class AdminCampo(admin.ModelAdmin):
    fields = ("nome_campo", "tipo", "status", "id_formulario")
    list_display = ("id", "nome_campo", "tipo", "status", "id_formulario")


@admin.register(Registro)
class AdminRegistro(admin.ModelAdmin):
    fields = ("id_formulario", "id_campo", "valor", "protocolo")
    list_display = ("id", "id_formulario", "id_campo", "valor", "protocolo")


@admin.register(PropostaRegistro)
class AdminProposta(admin.ModelAdmin):
    fields = ("protocolo", "status")
    list_display = ("id", "protocolo", "status")
