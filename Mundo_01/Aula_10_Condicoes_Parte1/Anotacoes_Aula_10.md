# 📝 Anotações – Mundo 01: Aula 10

## Condições - Parte 01

### O que são estruturas condicionais?
São comandos que permitem ao programa **tomar decisões** com base em **testes lógicos**.  
Elas são fundamentais para construir programas que **reagem de formas diferentes dependendo de certas condições**. Em outras palavras, são desvios que podem ocorrer na sequência do algoritmo, dependendo de uma possibilidade.

📌 **Indentação** é o recuo aplicado no início de uma linha de código para indicar que ela faz parte de um **bloco de instruções**. Sua utilização é **obrigatória** em blocos condicionais.

### 1. Estrutura Condicional Simples (If)

Executa um bloco de código **somente se** uma condição for verdadeira.
#### Exemplo:

```python
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O número é par.')

```

### 2. Estrutura Condicional Composta (If...Else)

A estrutura composta permite executar um bloco de código **se a condição for verdadeira**, e outro **se for falsa**.
#### Exemplo:

```python
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

```

---


### 📝 Importante: Operadores Úteis em Condições

Ao trabalhar com estruturas condicionais, pode ser utilizados operadores para **comparar valores** (relacionais) e **combinar condições** (lógicos).

### ✅ Operadores relacionais

| Operador | Significado         | Exemplo     | Resultado            |
|----------|---------------------|-------------|----------------------|
| `==`     | Igual a             | `a == b`    | True se a for igual a b |
| `!=`     | Diferente de        | `a != b`    | True se a for diferente de b |
| `>`      | Maior que           | `a > b`     | True se a for maior que b |
| `<`      | Menor que           | `a < b`     | True se a for menor que b |
| `>=`     | Maior ou igual a    | `a >= b`    | True se a ≥ b         |
| `<=`     | Menor ou igual a    | `a <= b`    | True se a ≤ b         |

### ✅ Operadores lógicos

| Operador | Significado                             | Exemplo                  | Resultado                                 |
|----------|-----------------------------------------|--------------------------|-------------------------------------------|
| `and`    | E – Todas as condições devem ser verdadeiras | `a > 0 and b > 0`       | True se **ambas** forem verdadeiras       |
| `or`     | OU – Pelo menos uma condição verdadeira     | `a > 0 or b > 0`        | True se **uma ou ambas** forem verdadeiras |
| `not`    | NÃO – Inverte o resultado lógico             | `not a == b`            | True se `a == b` for falso                |

---

📌 Esses operadores são essenciais para criar **condições mais complexas e realistas**. Sem eles, o programa não saberia como reagir a diferentes situações, e o código ficaria limitado.


