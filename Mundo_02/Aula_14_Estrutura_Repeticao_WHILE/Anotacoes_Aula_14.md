# 📝 Anotações – Mundo 02: Aula 14
## Laços de Repetição - Parte 02

### 1. Estrutura de Repetição: `while`

Executa comandos **enquanto uma condição for verdadeira**, mesmo sem saber exatamente quantas vezes o laço será repetido.  
Por isso, também é chamada de **estrutura de repetição com teste lógico**.

📌 Diferente do `for`, o `while` **não precisa de um intervalo definido**, apenas de uma **condição de parada**.  
É ideal quando **não se sabe previamente** quantas vezes será necessário repetir. 

✅ Em resumo, o bloco se repete **até que a condição se torne falsa**.

**- Exemplo:**

```python
contador = 0    
while contador < 5:
    print(contador)
    contador += 1

# Saída: 0 1 2 3 4
```
✓ Atenção: Para evitar laço infinito, é fundamental atualizar a variável de controle dentro do laço!

Neste exemplo, leia-se:
>"O contador começa em 0. <br>
>Enquanto for menor que 5, o programa imprime o valor e acrescenta uma unidade.<br>
>Quando o valor chega a 5, a condição se torna falsa e o laço é encerrado."

<br>

**- Exemplo com entrada do usuário:**

```python
resposta = ''
while resposta != 's':
    resposta = input('Deseja sair? [s/n] ').strip().lower()
print('Programa encerrado.')
```
Leia-se:
>"Enquanto a resposta for diferente de 's', continue perguntando.<br>
>Quando for igual a 's', a condição se torna falsa e o laço é encerrado."


