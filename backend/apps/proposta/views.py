from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.proposta.tasks import avalia_proposta
from services.gera_protocolo import Protocolo
from .models import Campo, Formulario, Registro
from .serializers import CampoSerializer, FormularioSerializer, RegistroSerializer


"""
    Definição das ViewsSets para as Urls, cada ViewSet possui um queryset e um serializer_class, que são utilizados pelo Django Rest Framework para
    definir o que será retornado pela API.
    Vale ressaltar que o RegistroViewSet possui uma característica diferente, pois ele é responsável por salvar cada registro novo com um protocolo único
    para que o celery possa avaliar a proposta de empréstimo. Assim cada prosposta está identificada com um protocolo para a identificação pelo administrador
"""


class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

    def create(self, request, *args, **kwargs):
        registros = request.data

        protocolo_obj = Protocolo()
        protocolo = protocolo_obj.gerar_protocolo()

        for registro in registros:
            registro["protocolo"] = protocolo

            serializer = self.get_serializer(data=registro)
            if serializer.is_valid(raise_exception=True):
                self.perform_create(serializer)

        avalia_proposta.delay(protocolo)
        headers = self.get_success_headers(serializer.data)
        return Response(
            "Registros salvos com sucesso.",
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class FormularioViewSet(viewsets.ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer


class CampoViewSet(viewsets.ModelViewSet):
    queryset = Campo.objects.all()
    serializer_class = CampoSerializer
