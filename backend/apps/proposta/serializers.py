from rest_framework import serializers

from .models import Campo, Formulario, Registro


class CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campo
        fields = ("id", "nome_campo", "tipo")


class FormularioSerializer(serializers.ModelSerializer):
    campos = CampoSerializer(many=True, read_only=True, source="campo_set")

    class Meta:
        model = Formulario
        fields = ("id", "campos")


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ("id", "id_formulario", "id_campo", "valor", "protocolo")
