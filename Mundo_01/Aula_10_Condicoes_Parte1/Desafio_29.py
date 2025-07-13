# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 29 ##')
print ()
velocidade = float (input('Velocidade do carro em km/h: '))
if velocidade > 80:
    valor = (velocidade - 80) * 7
    print ('\n- ATENÇÃO: Veículo acima do limite permitido!\n'
           f'Multa CONFIRMADA! -> O valor da MULTA é: R$ {valor:.2f}')
else:
    print ('\n- Veículo dentro do limite permitido.\n'
           'Mantenha a direção segura!')
