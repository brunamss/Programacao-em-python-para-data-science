
#  Com funções crie um sistema de médias notas escolares
#  Com funções crie um jogo da adivinhação

# def display ():
#     print ('NOTAS ESCOLARES')
#     print('****' *  10)

# def media (nota1, nota2, nota3):
#     soma =  nota1 + nota2 + nota3
#     return soma / 3

# def sistema_notas():
#     display()
#     nome =  input('Nome do aluno: ')
#     nota1 =  float(input('digite a nota1: '))
#     nota2 =  float(input('digite a nota2: '))
#     nota3 = float (input('digite a nota3: '))
#     m = media(nota1, nota2, nota3)
    
#     print('A média do(a)', nome, 'é',round( m, 2))


# sistema_notas ()

import random

def jogo():
    n = random.randint(1,100)
    x =int(input ('escolha um numero: '))

    if n == x: 
        print ('ganhou')
    else: 
        print ('perdeu')
jogo()