# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:44:46 2023

@author: Libertas
"""

def mensagem(x):
    MSG='!'+ x + '!'
    print('-'*len(MSG))
    print(MSG)
    print('-'*len (MSG))
    
mensagem('Oi, como vai voce?!')
mensagem('e,ai!')
mensagem('obabaoobabaoobabaoobabao')
mensagem(input('Qual e a sua mensagem'))