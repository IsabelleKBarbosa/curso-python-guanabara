#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
print ('_____________________________________________________________________')
print ('## ATIVIDADE PRÁTICA ##')
print ()
n = int (input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print ('Os resultados obtidos são: ')
print (f' - O dobro: {d} \n - O triplo: {t} \n - A raiz quadrada: {rq:.2f}')
