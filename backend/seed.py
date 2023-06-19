import os
import sys

import django

from apps.proposta.models import Campo, Formulario

class Seeder:

    def __init__(self):
        self.formulario = []
        self.campos = []


    def limpa_db(self):
        if '--flush' in sys.argv:
            print('\t- Limpando o DB para o Seed\n')
            os.system('./manage.py flush --no-input')

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

if __name__=='__main__':
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
    django.setup()

    seeder = Seeder()

    print('Iniciando o Seed...\n') 
    seeder.create_formulario()
