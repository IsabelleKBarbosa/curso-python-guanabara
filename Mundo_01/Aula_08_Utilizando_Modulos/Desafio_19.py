#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 19 ##')
print ()
print ('A seguir, digite o nome de cada aluno participante: \n')
aluno1 = str (input('Participante 1: '))
aluno2 = str (input ('Participante 2: '))
aluno3 = str (input ('Participante 3: '))
aluno4 = str (input('Participante 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice (lista)
print ()
print (f' - O aluno sorteado é: {sorteio}')
