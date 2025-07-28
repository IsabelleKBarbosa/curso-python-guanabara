# 📝 Anotações – Mundo 02: Aula 13
##  Laços de Repetição - Parte 01

### 1. Estrutura de Repetição: `FOR`
Também é conhecido como **laço com variável de controle**, porque usa-se uma variável (como `x`, `i` ou `c`) que **controla quantas vezes o laço será executado**, dentro de um intervalo definido com `range()`.  

Esse tipo de laço segue exatamente os valores indicados — por isso, é ideal quando já se sabe o **início**, o **fim** e o **passo** da repetição.  

✅ É muito útil para **repetir comandos de forma controlada e eficiente**, evitando duplicação de código e tornando o programa mais organizado.

📌 Lembrar-se: fazer a **indentação correta** é fundamental para o funcionamento da estrutura. Sem ela, o Python gerará erro e o bloco de repetição não será reconhecido.

* Sintaxe do `for` com `range()`

```python
for variável in range(início, fim, passo):
    bloco_de_código
```

**Exemplos com Números:**
```python
# Contando de 0 a 4
for c in range(0, 5):
    print(c)  # 0 1 2 3 4

# Contagem regressiva de 10 até 0
for c in range(10, -1, -1):
    print(c)

# Contando de 0 a 8 pulando de 2 em 2
for c in range(0, 10, 2):
    print(c)  # 0 2 4 6 8
```
**Exemplo com entrada do usuário:**
```python
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
```
> Use `n+1` porque o `range()` não inclui o número final.

### * Observação:
  💬 O `for` também funciona com strings, listas e outros tipos de sequência, não só com `range()`.
**Exemplo:**
```python
nome = 'Python'
for letra in nome:
    print(letra)
```


  
