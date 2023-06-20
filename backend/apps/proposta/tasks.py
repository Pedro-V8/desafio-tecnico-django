from celery import shared_task

from apps.proposta.models import PropostaRegistro


# Função que verifica se existe uma proposta de empréstimo no banco de dados.
def verifica_ocorrencia():
    return PropostaRegistro.objects.exists()


"""
    Função que avalia uma proposta de empréstimo, para garantir que a fim de testes metade das propostas sejam negadas e a outra metade aprovada,
    o script verifica se a última ocorrência no banco de dados é uma proposta aprovada, caso seja, a próxima proposta será negada e vice-versa.
"""


@shared_task
def avalia_proposta(protocolo):
    if not verifica_ocorrencia():
        proposta = PropostaRegistro(protocolo=protocolo, status="aprovado")
        proposta.save()
        return "Criado com sucesso"
    else:
        proposta = PropostaRegistro.objects.latest("id")

        if proposta.status == "aprovado":
            nova_proposta = PropostaRegistro(protocolo=protocolo, status="negado")
            nova_proposta.save()
            return "Criado com sucesso"
        else:
            nova_proposta = PropostaRegistro(protocolo=protocolo, status="aprovado")
            nova_proposta.save()
            return "Criado com sucesso"
