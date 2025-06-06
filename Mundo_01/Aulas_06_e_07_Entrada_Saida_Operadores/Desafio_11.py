#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada litro de tinta pinta uma area de 2 metros quadrados.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 11 ##')
print ()
larg = float(input('- Forneça a largura, em metros, da parede que será pintada: '))
alt = float (input('- Agora, digite a altura, em metros, dessa mesma parede: '))
area = (larg * alt)
print ()
print (f'A área da parede corresponde a: {area:.2f} m²')
tinta = (area / 2) * 1
print (f'Quantidade de tinta para pintar a parede que possui {area:.2f}m²: {tinta:.2f}L de tinta')
