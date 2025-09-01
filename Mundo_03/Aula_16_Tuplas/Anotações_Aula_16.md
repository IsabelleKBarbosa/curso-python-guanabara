# 📝 Anotações – Mundo 03: Aula 16

### Variáveis Compostas

> Nas **variáveis simples**, ao atribuir um valor, o espaço na memória fica reservado apenas para ele.  
> Quando um novo valor é atribuído, o anterior é apagado e substituído.
> 
> As **variáveis compostas** permitem armazenar **vários valores em um único espaço de memória**, mantendo-os organizados em uma estrutura única.
>  
> Em Python, existem 3 tipos principais de variáveis compostas: **Tuplas, Listas e Dicionários**.

📌 Esse recurso é essencial para manipular coleções de dados de forma prática e eficiente.

---

## 1. Variáveis Compostas: Tuplas
Características principais
- Uma **tupla** é uma **coleção ordenada de valores**.
- É representada por **parênteses `()`**.
- É **imutável**: elementos **não podem ser alterados, adicionados ou removidos** após a criação.
- Pode armazenar **dados de tipos diferentes** *(strings, números, etc.)*.
- Permite **acesso por índice** e **fatiamento**, assim como as strings.
- Pode ser **percorrida com laços de repetição**, como o `for`.

### Exemplos práticos

#### - Criando e acessando elementos
```python
cores = ('azul', 'verde', 'vermelho', 'amarelo')

print(cores[0])     # azul
print(cores[-1])    # amarelo
print(cores[1:3])   # ('verde', 'vermelho')
```

#### - Percorrendo uma tupla com `for`
```python
animais = ('gato', 'cachorro', 'pássaro')

for pet in animais:
    print(f'Eu gosto de {pet}')
```

#### - Usando `enumerate()` para indicar posição e elemento
```python
escolha = ('maçã', 'banana', 'laranja')

for pos, fruta in enumerate(escolha):
    print(f'A posição {pos} contém {fruta}')
```
✓ Neste exemplo:
> O índice começa em **0**. Portanto, a primeira linha será:  
> `A posição 0 contém maçã`  
> E assim por diante, para os próximos elementos.  
>
> Se quiser que a contagem apareça/comece em **1** (ao invés de 0), há duas opções:  
> - Somar **+1** ao índice dentro do f-string: `{pos + 1}`  
> - Usar o parâmetro `start=1` no `enumerate`:  
>   ```python
>   for pos, fruta in enumerate(escolha, start=1):
>       print(f'A posição {pos} contém {fruta}')
>   ```

---
### ⚠️ Funções úteis que podem ser utilizadas: 

```python
numeros = (10, 20, 10, 40, 50)

print(len(numeros))          # 5 → quantidade de elementos/tamanho da tupla
print(numeros.count(10))     # 2 → quantas vezes aparece o 10
print(numeros.index(40))     # 3 → posição do número 40
print(sorted(numeros))       # [10, 10, 20, 40, 50] → lista ordenada

# Fatiamento
print(numeros[1:4])          # (20, 10, 40) → do índice 1 ao 3
print(numeros[:3])           # (10, 20, 10) → do início até o índice 2
print(numeros[2:])           # (10, 40, 50) → do índice 2 até o final

# Acessando com índices negativos
print(numeros[-1])           # 50 → último elemento
print(numeros[-2])           # 40 → penúltimo elemento
```
📌 Lembre-se: 
* No fatiamento, o índice final é sempre excluído do resultado.
* Índices negativos percorrem a tupla de trás para frente.
