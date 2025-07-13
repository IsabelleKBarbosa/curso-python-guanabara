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

### 1. Fatiamento

Operação que permite extrair/cortar partes de uma string.
#### ✓ Sintaxe Geral: 

 `string[início:fim:passo]`

- `início`: índice de onde a extração começa (inclusivo).
- `fim`: índice onde a extração termina (exclusivo).
- `passo`: define de quantos em quantos índices a leitura será feita.
  
Exemplos:

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



