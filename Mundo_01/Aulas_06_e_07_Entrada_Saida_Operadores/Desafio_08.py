#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
print ('_____________________________________________________________________')
print ('## ATIVIDADE PRÁTICA ##')
print ()
n = float (input ('Digite o número em metros para ser convertido: '))
print (f'A medida de {n:.1f}m corresponde a: ')
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print (f' - Quilômetro: {km}km \n - Hectômetro: {hm}hm \n - Decâmetro: {dam}dam \n - Decímetro: {dm}dm \n - Centímetro: {cm:.0f}cm \n - Milímetro: {mm:.0f}mm')
