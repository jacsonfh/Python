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

class Pessoa:
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
            
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False
