# 📝 Anotações – Mundo 01: Aula 08 

## Utilizando Módulos: Bibliotecas em Python

### O que são Módulos?

Em Python, um **módulo** é um arquivo com extensão `.py` que contém definições de variáveis, funções, classes e/ou código executável. Funcionam como recursos adicionais para obter novas/melhores funções. Cada módulo representa um **namespace** próprio, permitindo:

- **Organização** do código em funcionalidades coesas;  
- **Reuso** de trechos de código em diferentes programas;  
- **Isolamento** de escopos, evitando conflitos de nomes.

O programa em Python já vem com o básico, por isso, se quiser aumentar as funções é necessário fazer a implementação de bibliotecas. Para usar um módulo, basta importá-lo no seu programa com `import` ou `from … import …`, tornando disponíveis seus componentes conforme necessário. É fundamental, como boa prática, **declarar nas primeiras linhas.**  

### Tipos de Módulos

- **Built-in**: módulos que já vêm com a instalação do Python (ex.: `math`, `sys`, `datetime`).
- **Externos (PyPI)**: módulos criados pela comunidade e distribuídos no Python Package Index. Instalados via `pip`.

---

### Comandos de Importação

#### ✓ 1. Comando `import`
Importa o módulo inteiro. Utiliza o nome do módulo como prefixo para acessar seus itens.

```python
import math

print(math.sqrt(25))      # saída: 5.0
print(math.pi)            # saída: 3.141592653589793
```

#### ✓ 2. Comando `from … import …`
Importa apenas um elemento/função da biblioteca.

```python
from datetime import date, timedelta
hoje = date.today()
print(hoje)
``` 

#### Observação: 
**Namespace** é um espaço de nomes que associa identificadores a objetos (variáveis, funções, classes, módulos) em Python, isolando escopos e evitando conflitos de nomes. 

> - Todo módulo faz parte de algum pacote ou biblioteca, mas nem toda biblioteca é apenas um módulo — ela é tipicamente um agrupamento de pacotes e módulos relacionados.  

