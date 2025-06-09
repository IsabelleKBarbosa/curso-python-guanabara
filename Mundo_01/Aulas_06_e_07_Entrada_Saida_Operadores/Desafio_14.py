#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 14 ##')
print ()
celsius = float (input('Digite a temperatura em Celsius: '))
fah = ((9 / 5) * celsius) + 32
print (f' - Temperatura em  Fahrenheit: {fah:.1f} °F')
print ()
print (f' {fah:.1f}°F = {celsius:.1f}°C')
