from celery import shared_task

from apps.proposta.models import Registro , PropostaRegistro


def verifica_ocorrencia():
    return PropostaRegistro.objects.exists()

@shared_task
def avalia_proposta(protocolo):

    if not verifica_ocorrencia():
        proposta = PropostaRegistro(
            protocolo=protocolo, 
            status='aprovado'
        )
        proposta.save()
        return "Criado com sucesso"
    else:
        proposta = PropostaRegistro.objects.latest('id')

        if proposta.status == 'aprovado':
            nova_proposta = PropostaRegistro(
                protocolo=protocolo,
                status='negado'
            )
            nova_proposta.save()
            return "Criado com sucesso"
        else:
            nova_proposta = PropostaRegistro(
                protocolo=protocolo,
                status='aprovado'
            )
            nova_proposta.save()
            return "Criado com sucesso"