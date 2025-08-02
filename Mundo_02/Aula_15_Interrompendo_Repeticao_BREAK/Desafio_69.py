#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
from time import sleep
on = '\033[1m'
off = '\033[m'
linha = ('-'*50)
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 69 ##')
print ()
print ('=== CADASTRAMENTO ===')
homens = mulheres = m_menor_20 = maior_18 = 0
c = 1
iniciar = str(input('Iniciar Cadastramento: [S]-Sim / [N]-Não? ' )).upper().strip()[0]
while iniciar not in 'SN':
    print ('Opção inválida. Tente novamente!')
    iniciar = str(input('Iniciar Cadastramento: [S]-Sim / [N]-Não? ' )).upper().strip()[0]
print (linha)
while iniciar == 'S':
    while True:
        print ()
        print (f'\033[7m- CADASTRO Nº{c}{off}')
        idade = int (input('Digite a idade: '))
        sexo = str (input('Digite o sexo [M] - Masculino / [F] - Feminino: ')).upper().strip()[0]
        while sexo not in 'MF':
            print (f'\033[1;37mEscolha inválida.{off}')
            sexo = str(input('Digite o sexo [M] - Masculino / [F] - Feminino: ')).upper().strip()[0]
        if idade > 18:
            maior_18 += 1
        if sexo == 'M':
            homens += 1
        elif sexo == 'F':
            mulheres += 1
            if idade < 20:
                m_menor_20 += 1
        c += 1
        sleep(0.3)
        print ()
        print (f'{on}Cadastro concluído com sucesso!{off}')
        print (linha)
        cont = str (input(f'\033[1;34m- Deseja cadastrar outros dados? [S] - Sim / [N] - Não {off}')).upper().strip()[0]
        while cont not in 'SN':
            print (f'\033[1;37mEscolha inválida.{off}')
            cont = str(input(f'- Digite \033[1;32mSIM{off} para continuar ou \033[1;31mNÃO{off} para encerrar cadastramento: ')).upper().strip()[0]
        print (linha)
        iniciar = cont
        if cont == 'N':
            break
print(f'{on}Cadastramento encerrado.{off}'.center(50))
print (linha)
print ()
print (f'\033[7;35mAnálise de Dados{off}\n'.center(50))
if maior_18 == 0:
    print ('A) Não há maiores de 18 anos cadastrados.')
else:
    print (f'A) Quantidade de pessoas maiores de 18 anos: {maior_18}')
if homens > 0:
    print (f'B) Quantidade de homens cadastrados: {homens}')
elif homens == 0:
    print ('B) Não há homens cadastrados.')
if mulheres == 0:
    print ('C) Não há mulheres cadastradas.')
else:
    print (f'C) Quantidade de mulheres com menos de 20 anos: {m_menor_20}')

# OBSERVAÇÃO SOBRE A ESTRUTURA DO CÓDIGO:
# Este código está funcionando corretamente, mas identifiquei uma redundância na lógica de controle de fluxo.
# Estou utilizando duas variáveis (iniciar e cont) para controlar se o usuário deseja cadastrar ou não,
# além de usar o comando 'break' para forçar a saída do laço.
# Para tornar o código mais limpo e direto, pode-se unificar essas duas variáveis em uma única — chamada 'cadastro', por exemplo.
# Dessa forma, o próprio laço while é controlado pela resposta do usuário,
# eliminando a necessidade do 'break' e deixando a estrutura mais simples e legível.
# Deixo este comentário e meu código primário como lembrete das possibilidades de refatoração e boas práticas.
