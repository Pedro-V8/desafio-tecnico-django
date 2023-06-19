import datetime
import random


class Protocolo:
    def __init__(self):
        self.datetime = datetime.datetime.now()
        self.ano = str(self.datetime.year)
        self.mes = str(self.datetime.month)
        self.dia = str(self.datetime.day * 100)

    def gerar_protocolo(self):
        datetime_concatenado = self.ano + self.mes + self.dia
        protocolo = datetime_concatenado + str(random.randint(100, 200))

        return protocolo
