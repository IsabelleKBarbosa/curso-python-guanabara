# 📝 Anotações – Mundo 01: Aulas 06 e 07

## Tipos Primitivos e Saída de Dados

### ✓ Tipos primitivos
São os tipos básicos de dados. São eles:
- `int` → números inteiros (ex: 10, -3, 0)
- `float` → números reais com ponto flutuante (ex: 3.14, -0.5)
- `bool` → valores booleanos (lógicos) (ex: `True`, `False`)
- `str` → texto (strings), entre aspas simples ou duplas (ex: `'Python'`, `"Olá"`)

Python usa **tipagem dinâmica**, ou seja, você não precisa declarar o tipo da variável — ele é reconhecido automaticamente de acordo com o valor atribuído.

### ✓ Saída de dados
Para **mostrar informações na tela**, usamos a função `print()`.
Ela pode exibir textos, números, variáveis ou tudo isso junto.

### 📌 Importante: Conversão de Tipos

Quando usamos a função `input()` para ler dados do usuário, o valor retornado é sempre uma **string**,  
mesmo que a pessoa digite um número.

Por isso, se quisermos trabalhar com **números**, devemos **converter manualmente** o tipo da entrada:

- `int()` → converte para número inteiro  
- `float()` → converte para número com ponto (decimal)  
- `str()` → converte para texto (string)

### Exemplo Prático:
```python
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
nome = input('Digite seu nome: ')
print(f'{nome} tem {idade} anos e mede {altura} metros.')
```
<br>

## Operadores Aritméticos

São símbolos usados para realizar **operações matemáticas** com variáveis ou valores em Python.

### ✓ Os principais operadores são:

- `+` → adição (soma)
- `-` → subtração
- `*` → multiplicação
- `/` → divisão (com ponto decimal)
- `**` → potência (exponenciação)
- `//` → divisão inteira (retorna apenas a parte inteira)
- `%` → módulo (resto da divisão)

### Exemplo Prático:
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a ** b)  # 1000 (10³)
print(a // b)  # 3
print(a % b)   # 1

```
Obs: A raiz quadrada de um número pode ser calculada usando o operador de potência com o expoente 1/2. 
Isso funciona porque elevar um número a ½ é matematicamente o mesmo que extrair sua raiz quadrada. A raiz cúbica segue o mesmo raciocínio.


### 📌 Importante: Ordem de Precedência 
Python segue uma **ordem de precedência** para resolver expressões matemáticas, assim como na matemática tradicional.  
Isso significa que algumas operações são feitas antes de outras, mesmo que venham depois no código.

1. `()` → parênteses  
2. `**` → potência  
3. `*`, `/`, `//`, `%` → multiplicação, divisão, divisão inteira e módulo  
4. `+`, `-` → adição e subtração

### Exemplo Prático:

```python
resultado = 2 + 3 * 4
print(resultado)  # 14 → multiplicação é feita antes da soma

resultado = (2 + 3) * 4
print(resultado)  # 20 → operação dentro dos parênteses é feita primeiro
```
