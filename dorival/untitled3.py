# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:55:18 2023

@author: Libertas
"""

def quadrado(x):
    y = x * x
    return y

def love(a,b):
    print(f'{a} gosta de {b}')

valor_para_calculo=int(input('Digite um numero: '))
resultado = quadrado (valor_para_calculo)
print(resultado)

nome1=input('nome 1: ')
nome2=input('nome 2: ')
love(nome1,nome2)