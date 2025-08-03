# 📝 Anotações – Mundo 02: Aula 15
## Laços de Repetição - Parte 03

### 1. Interrompendo Repetições: `break`

O `break` é um comando que **força a saída imediata de um laço (`for` ou `while`)**, independente da condição de repetição.

📌 É muito usado em **laços infinitos controlados por uma condição interna**, como menus, entradas do usuário e validações.

⚠️ O `while True` é o que cria um **laço infinito** propositalmente e sem `break` o loop infinito nunca termina.

**Sintaxe em `while`**

```python
while True:
    comando
    if condição:
        break
```

 **- Exemplo com número positivo**

```python
while True:
    numero = int(input('Digite um número positivo: '))
    if numero > 0:
        print(f'Número aceito: {numero}')
        break
    print('Valor inválido! Tente novamente.')
```
✓ Neste exemplo:
>O `while True` cria um laço infinito.<br>
>O `break` só é executado quando o número digitado for maior que zero.<br>
>Enquanto o número for zero ou negativo, o programa continuará pedindo uma nova entrada.


