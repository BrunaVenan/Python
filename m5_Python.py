# -*- coding: utf-8 -*-
"""M5_exercise.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AFjwPUyDkDzIUVnpkEJU49aok-z23RSX

<img src="https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png" alt="ebac-logo">

---

# **Módulo** | Python: Programação Funcional
Caderno de **Exercícios**<br>
Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)

---

# **Tópicos**

<ol type="1">
  <li>Função lambda;</li>
  <li>Função map;</li>
  <li>Função filter;</li>
  <li>Função reduce.</li>
</ol>

---

# **Exercícios**

## 0\. Preparação do ambiente

Neste exercício vamos trabalhar com o arquivo csv com dados de crédito, definido abaixo. Execute cada uma das células de código para escrever os arquivos na sua máquina virtual.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile credito.csv
# id_vendedor,valor_emprestimos,quantidade_emprestimos,data
# 104271,448.0,1,20161208
# 21476,826.7,3,20161208
# 87440,313.6,3,20161208
# 15980,-8008.0,6,20161208
# 215906,2212.0,5,20161208
# 33696,2771.3,2,20161208
# 33893,2240.0,3,20161208
# 214946,-4151.0,18,20161208
# 123974,2021.95,2,20161208
# 225870,4039.0,2,20161208

"""Vamos ler o conteúdo do arquivo em uma lista onde cada elemento é um dicionário representando as linhas do arquivo."""

emprestimos = []
with open(file='./credito.csv', mode='r', encoding='utf8') as fp:
  fp.readline() # cabeçalho
  linha = fp.readline()
  while linha:
    linha_emprestimo = {}
    linha_elementos = linha.strip().split(sep=',')
    linha_emprestimo['id_vendedor'] = linha_elementos[0]
    linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
    linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
    linha_emprestimo['data'] = linha_elementos[3]
    emprestimos.append(linha_emprestimo)
    linha = fp.readline()

for emprestimo in emprestimos:
  print(emprestimo)

"""## 1\. Função `map`

Aplique a função map na lista de `emprestimos` para extrair os valores da chave `valor_emprestimos` na lista `valor_emprestimos_lista`. Faça também a conversão de `str` para `float`.
"""

valor_emprestimos_lista = list(map(lambda x : float(x['valor_emprestimos']),emprestimos))

print(valor_emprestimos_lista)

"""---

## 2\. Função `filter`

Aplique a função filter na lista de `valor_emprestimos_lista` para filtrar apenas os valores maiores que zero (os valores negativas são erros na base de dados). Salve os valores na lista `valor_emprestimos_lista_filtrada`.
"""

valor_emprestimos_lista_filtrada = list(filter(lambda emprestimo: emprestimo > 0, valor_emprestimos_lista))



print(valor_emprestimos_lista_filtrada)

"""---

## 3\. Função `reduce`

Com a nossa lista de valores de emprestimo pronta, vamos extrair algumas métricas.

### 3\.1\. Função `reduce` para extrair a **soma**

Aplique a função reduce para somar os elementos da lista `valor_emprestimos_lista_filtrada` na variavel `soma_valor_emprestimos`.
"""

from functools import reduce

soma_valor_emprestimos = reduce(lambda x,y : x + y, valor_emprestimos_lista_filtrada,0)

print(soma_valor_emprestimos)

"""### 3\.2\. Função `reduce` para extrair a **media aritimética**

Aplique a função reduce para extrair a média aritimética (mais informações [aqui](https://pt.wikipedia.org/wiki/M%C3%A9dia#M%C3%A9dia_aritm%C3%A9tica)) dos elementos da lista `valor_emprestimos_lista_filtrada` na variavel `media_valor_emprestimos`.

Dica: Para calcular o tamanho da lista, isto é a quantidade de elementos, utilize a função len(), dentro do argumento da função coloque a lista `valor_emprestimos_lista_filtrada`.
"""

from functools import reduce

media_valor_emprestimos = reduce(lambda x,y : x + y, valor_emprestimos_lista_filtrada,0)

print(media_valor_emprestimos)

"""### 3\.3\. (**Desafio**) Função `reduce` para extrair o **desvio padrão amostral**

Aplique a função reduce para extrair a média aritimética (mais informações [aqui](https://pt.wikipedia.org/wiki/M%C3%A9dia#M%C3%A9dia_aritm%C3%A9tica)) dos elementos da lista `valor_emprestimos_lista_filtrada` na variavel `desvio_padrao_valor_emprestimos`.
"""

from functools import reduce

a = map(lambda x: (x-media_valor_emprestimos)**2,valor_emprestimos_lista_filtrada)
b = list(a)
c = reduce (lambda x,y: x+y, b)
d = c / (len(valor_emprestimos_lista_filtrada)-1)
e = pow(d,0.5)

print(e)

"""---"""