#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main"""

__author__ = "Jacson F. Heiderscheidt"
__copyright__ = "Copyright 2021, Allpy Project"
__credits__ = ["JFH"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "JFH"
__email__ = "jacsonfh@gmail.com"
__status__ = "Estudo de POO"

from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)

p1.comer('maçã')
p1.parar_comer()
p1.parar_comer()
p1.comer('maçã')



