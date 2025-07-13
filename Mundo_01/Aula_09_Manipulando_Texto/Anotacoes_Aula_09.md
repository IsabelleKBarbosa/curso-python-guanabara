# 📝 Anotações – Mundo 01: Aula 09

## Manipulando Texto e Cadeia de Caracteres

Manipulação de texto é o conjunto de técnicas e funções utilizadas para trabalhar com strings, que são cadeias de caracteres como palavras e frases. Com essas ferramentas, podemos fatiar, analisar, transformar, formatar e combinar textos de forma simples e eficiente, o que é essencial para desenvolver programas que lidam com nomes, mensagens, arquivos, dados de entrada, entre outros.

✅ A partir de agora, estará presente na maioria dos programas construídos.

📌 Lembrar-se:
* Cadeia de Caracteres = **string**, sempre em aspas simples ou dupla.
* Python diferencia letra maíscula e minúscula.
  
Em Python, uma cadeia de caracteres é colocada na memória tendo cada elemento um "mini" espaço individual que possui **índice** próprio, iniciando sempre em 0. Por exemplo:

```txt
String:   C   u   r   s   o       e   m       V   í   d   e   o
Índice:   0   1   2   3   4   5   6   7   8   9  10  11  12  13
```
➡️ Isso significa que:

- `frase[0]` retorna `'C'`, o primeiro caractere da string.
- `frase[5]` retorna `' '`, que é o espaço entre as palavras "Curso" e "em".
- `frase[13]` retorna `'o'`, o último caractere da frase.

Cada caractere ocupa um índice específico, o que permite acessar, fatiar ou modificar trechos com precisão.

---

### 1. Fatiamento de Strings

Operação que permite extrair/cortar partes de uma string.
#### ✅ Sintaxe Geral: 

 `string[início:fim:passo]`

- `início`: índice de onde a extração começa (inclusivo).
- `fim`: índice onde a extração termina (exclusivo).
- `passo`: define de quantos em quantos índices a leitura será feita.
  
#### Exemplos:

`frase[9]` → retorna o caractere que está no índice 9.

`frase[9:13]` → extrai a sequência do índice 9 até 12 (o índice 13 não é incluído).

`frase[9:21:2]` → extrai do índice 9 até o 20, pulando de 2 em 2.

`frase[9::3]` → começa no índice 9 e vai até o final da string, pulando de 3 em 3

```python
frase = 'Curso em Vídeo'

print(frase[9])        # V
print(frase[9:13])     # Víde
print(frase[9:21:2])   # Véo
print(frase[9::3])     # Vó
```
📌 Lembrar-se:
* O índice fim não é incluído no resultado.
* O fatiamento também funciona com índices negativos para contar de trás para frente.


### 2. Análise de Strings

Conjunto de funções para **analisar o conteúdo de uma string**, como descobrir seu tamanho, contar quantas vezes um caractere aparece ou localizar a posição de palavras ou letras.

#### ✅ Funções principais:

- `len()` → retorna o comprimento (número de caracteres) da string.
- `count()` → conta quantas vezes um caractere ou trecho aparece.
- `find()` → localiza a posição da primeira ocorrência de um trecho.
- `in` → verifica se uma substring existe dentro da string (retorna `True` ou `False`).

#### Exemplos:

```python
frase = 'Curso em Vídeo'

print(len(frase))            # 14 → total de caracteres
print(frase.count('o'))      # 3 → número de vezes que 'o' aparece
print(frase.count('o', 0, 13)) # 2 → contagem de 'o' do índice 0 ao 12
print(frase.find('Vídeo'))   # 9 → posição onde 'Vídeo' começa
print(frase.find('Android')) # -1 → não encontrado
print('Curso' in frase)      # True → verifica se 'Curso' está na frase
```

### 3. Transformação de Strings

As funções de transformação permitem **alterar o formato do texto**, como colocar tudo em maiúsculo, minúsculo, substituir trechos, ou capitalizar palavras.

#### ✅ Funções principais:

- `replace()` → substitui um trecho da string por outro.
- `upper()` → transforma todos os caracteres em **maiúsculo**.
- `lower()` → transforma todos os caracteres em **minúsculo**.
- `capitalize()` → coloca a primeira letra da string em **maiúsculo**, e o restante em **minúsculo**.
- `title()` → coloca a **primeira letra de cada palavra** em maiúsculo.
- `strip()` → remove **espaços extras** no início e no final da string.
  - `lstrip()` → remove apenas os espaços **à esquerda**.
  - `rstrip()` → remove apenas os espaços **à direita**

#### Exemplos:

```python
frase = 'Curso em Vídeo'

print(frase.replace('Vídeo', 'Python'))  # Curso em Python
print(frase.upper())     # CURSO EM VÍDEO
print(frase.lower())     # curso em vídeo
print(frase.capitalize())# Curso em vídeo
print(frase.title())     # Curso Em Vídeo

print(frase.strip())       # Curso em Vídeo (sem espaços nas pontas)
print(frase.lstrip())      # Curso em Vídeo  (remove à esquerda)
print(frase.rstrip())      #   Curso em Vídeo (remove à direita)
```
> Observação: Transformações **não alteram o valor original da string** a menos que armazene o resultado em uma variável. Técnicas para modificar objetos diretamente serão abordadas mais adiante, em conteúdos sobre **Orientação a Objetos**.


### 4. Divisão e Junção de Strings

Python permite **dividir uma string em partes menores** (como palavras ou sílabas) e também **unir elementos** usando separadores personalizados.

#### ✅ Funções principais:

- `split()` → divide a string em uma lista de palavras, usando **espaço por padrão** como separador.
- `join()` → faz o oposto do `split`: **junta elementos de uma lista** em uma única string, usando um separador definido.

#### Exemplos:

```python
frase = 'Curso em Vídeo'

palavras = frase.split()
print(palavras)     # ['Curso', 'em', 'Vídeo']
print(palavras[0])  # Curso
print(palavras[2])  # Vídeo
print(palavras[2][3])  # o (letra de dentro da palavra)

# Agora vamos juntar
frase_nova = '-'.join(palavras)
print(frase_nova)   # Curso-em-Vídeo
```
📌 Atenção: O `split()` retorna uma **lista**, e para acessar palavras ou até letras dentro delas usando **índice duplo**: `lista[indice][subindice]`.

```python
frase = 'Curso em Vídeo'
palavras = frase.split()

print(palavras)         # ['Curso', 'em', 'Vídeo']
print(palavras[0])      # 'Curso'  → primeira palavra
print(palavras[0][2])   # 'r'      → terceira letra da primeira palavra
```
---

### 📝 Importante: `.zfill()` e `.just()`

Esses métodos são úteis para **formatar strings** quando é preciso alinhar ou preencher com zeros, especialmente em sistemas que precisam exibir números ou nomes com formatação padronizada, como boletos, relatórios, ou arquivos de texto alinhados.

#### ✅ `.zfill(tamanho)`
Preenche a string com zeros (`0`) à esquerda até atingir o tamanho desejado.

```python
num = '7'
print(num.zfill(3))   # 007
```

#### ✅ .rjust(tamanho) e .ljust(tamanho)
`.rjust()` → alinha a string à direita, preenchendo com espaços (ou outro caractere).

`.ljust()` → alinha a string à esquerda, preenchendo com espaços (ou outro caractere).

```python
nome = 'Ana'
print(nome.rjust(10))         # '       Ana'
print(nome.ljust(10, '-'))    # 'Ana-------'
```




