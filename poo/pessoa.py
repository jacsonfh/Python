#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""objeto pessoa"""

__author__ = "Jacson F. Heiderscheidt"
__copyright__ = "Copyright 2021, Allpy Project"
__credits__ = ["JFH"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "JFH"
__email__ = "jacsonfh@gmail.com"
__status__ = "Estudo de POO"

from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) #Variável da Classe.

    def __init__(self, nome, idade, comendo = False, falando = False): #Variáveis da Instância.
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False
        return

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

