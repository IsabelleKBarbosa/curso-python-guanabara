#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 40 ##')
print ()
print ('=== SITUAÇÃO ESCOLAR ===')
print ('Forneça o que se pede para calcular a média do(a) estudante:\n')
n1 = float (input('Digite a primeira nota: '))
n2 = float (input ('Digite a segunda nota: '))
media = (n1 + n2) / 2
print ()
print (f'Resultado: \033[7m{media:.1f}\033[m')
if media < 5:
    print ('Status: \033[1;31mREPROVADO\033[m')
elif media >= 5 and media < 7:
    print ('Status: \033[1;33mRECUPERAÇÃO\033[m')
elif media >= 7:
    print ('Status: \033[1;32mAPROVADO\033[m')
