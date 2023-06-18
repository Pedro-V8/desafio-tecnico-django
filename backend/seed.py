import os
from apps.proposta.models import Formulario , Campo

class Seeder:

    def __init__(self):
        self.formulario = []
        self.campos = []


    def create_formulario(self):
        print('\t- Criando formulario...')
        self.formulario = Formulario.objects.bulk_create([
            Formulario(
                status=True,
            )
        ])
        print('\t  Successfully created', len(self.formulario), 'slaves', '\n')

    def create_capos(self):
        print('\t- Criando campos...')
        formulario = Formulario.objects.first()
        
        self.camps = Campo.objects.bulk_create([
            Campo(
                nome_campo='Nome Teste',
                tipo='string',
                status=True,
                id_formulario=formulario,
            ),
            Campo(
                nome_campo='Endereco Teste',
                tipo='string',
                status=True,
                id_formulario=formulario,
            ),
            Campo(
                nome_campo='Valor Teste',
                tipo='float',
                status=True,
                id_formulario=formulario,
            )])
        print('\t  Successfully created', len(self.campo), 'campus', '\n')
