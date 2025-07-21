#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 56 ##')
print ()
print ('Agrupamento e Análise')
print ('Informe os dados a seguir:\n')
soma = 0
h_nome = ''
h_idade = 0
contador_m = 0
contador_h = 0
quant_nova = 0
for x in range (1,5):
    print (f'== {x}º Pessoa ==')
    nome = str (input('Nome: ')).strip().title()
    idade = int (input('Idade: '))
    soma += idade
    sexo = int (input('Sexo ([1] - Masculino / [2] - Feminino ): '))
    if sexo == 2:
        contador_m += 1
    elif sexo == 1:
        contador_h += 1
    else:
        print ('Código não reconhecido. Tente novamente.')
    if sexo == 1 and idade > h_idade:
        h_idade = idade
        h_nome = nome
    if sexo == 2 and idade < 20:
        quant_nova += 1
    print ('_'*20)
print ()
print ('\n\033[7mESTATÍSTICA GERAL\033[m')
media = soma / 4
print (f'- Média das Idades: {media}')
if contador_h > 0:
    print (f'- Homem mais velho: {h_nome}, {h_idade} anos')
if contador_m > 0:
    print (f'- Mulheres com menos de 20 anos: {quant_nova}')
elif contador_m == 0:
    print ('Não há mulheres cadastradas nesse agrupamento.')
