#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 76 ##')
print ()
linha = ('-'*50)
print (linha)
print ('LISTAGEM DE PREÇOS'.center(50))
print (linha)

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Mochila', 120.32, 'Livro', 34.9)

for x in range(0, len(lista), 2):
    produto = lista[x]
    valor = lista[x + 1]
    print(f'{produto:.<40} R${valor:>7.2f}')

print(linha)
