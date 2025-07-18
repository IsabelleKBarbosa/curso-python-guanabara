# 📝 Anotações – Mundo 02: Aula 12

## Condições - Parte 02

### 1. Estrutura Aninhadas (If... Elif)
Condições aninhadas são **desvios possíveis dentro de outros desvios**.  
Ou seja, é quando usamos um `if` dentro de outro para tomar **decisões mais específicas**, dependendo de uma condição anterior.  

📌 Dentro de uma condição aninhada, é possível utilizar quantos `if` e `elif` forem necessários.  
No entanto, o `else` pode aparecer **no máximo uma vez** e **é opcional**.

#### Exemplo:

```python
idade = int(input('Informe sua idade: '))

if idade >= 18:
    print('Você é maior de idade.')
    carteira = input('Você possui carteira de motorista? [Sim/Não]: ').strip().upper()

    if carteira == 'Sim':
        print('Pode dirigir legalmente.')
    elif carteira == 'Não':
        print('Você é maior, mas ainda não tem carteira.')
    else:
        print('Resposta inválida.')
else:
    print('Você é menor de idade.')
```
