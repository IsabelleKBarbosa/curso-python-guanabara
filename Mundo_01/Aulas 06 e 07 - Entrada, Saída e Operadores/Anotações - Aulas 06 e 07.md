# 📝 Anotações – Mundo 01: Aulas 06 e 07

## Tipos Primitivos e Saída de Dados

### Tipos primitivos
São os tipos básicos de dados. São eles:
- `int` → números inteiros (ex: 10, -3, 0)
- `float` → números reais com ponto flutuante (ex: 3.14, -0.5)
- `bool` → valores booleanos (lógicos) (ex: `True`, `False`)
- `str` → texto (strings), entre aspas simples ou duplas (ex: `'Python'`, `"Olá"`)

Python usa **tipagem dinâmica**, ou seja, você não precisa declarar o tipo da variável — ele é reconhecido automaticamente de acordo com o valor atribuído.

### Saída de dados
Para **mostrar informações na tela**, usamos a função `print()`.
Ela pode exibir textos, números, variáveis ou tudo isso junto.

### ✨ Importante: Conversão de Tipos

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
