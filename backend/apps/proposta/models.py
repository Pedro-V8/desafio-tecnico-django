from datetime import datetime

from django.db import models

# Create your models here.


class Formulario(models.Model):
    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"

    status = models.BooleanField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.id)


class Campo(models.Model):
    class Meta:
        verbose_name = "Campo"
        verbose_name_plural = "Campos"

    nome_campo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    status = models.BooleanField()
    id_formulario = models.ForeignKey("Formulario", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_campo


class Registro(models.Model):
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    id_formulario = models.ForeignKey("Formulario", on_delete=models.CASCADE)
    id_campo = models.ForeignKey("Campo", on_delete=models.CASCADE)
    valor = models.CharField(max_length=500)
    protocolo = models.CharField(max_length=100)

    def __str__(self):
        return self.valor


class PropostaRegistro(models.Model):
    STATUS = [("aprovado", "Aprovado"), ("negado", "Negado")]

    class Meta:
        verbose_name = "Proposta"
        verbose_name_plural = "Propostas"

    protocolo = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.status
