# -*- coding: utf-8 -*-
"""M2_Python_Exercicio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u3Rm4Sj31ntJ76QcYbF9b4p9OAODlXpC

<img src="https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png" alt="ebac-logo">

---

# **Módulo 02** | Python: Estruturas de Dados
Caderno de **Exercícios**<br>
Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)

---

# **Tópicos**

<ol type="1">
  <li>Listas;</li>
  <li>Conjuntos;</li>
  <li>Dicionários.</li>
</ol>

---

# **Exercícios**

## 1\. Listas

Criei uma lista chamada `filmes` com o nome dos 10 primeiros filmes mais bem avaliados no site no [IMDB](https://www.imdb.com/chart/top/). Imprima o resultado.
"""

filmes = ['The Shawshank Redemption','The Godfather','The Dark Knight','The Godfather Part II','12 Angry Men',
          'Schindler_s List',' The Lord of the Rings_The Return of the King ','Pulp Fiction',
          'The Lord of the Rings_The Fellowship of the Ring','The Good, the Bad and the Ugly']
print (filmes)

"""Simule a movimentação do *ranking*. Utilize os métodos `insert` e `pop` para trocar a posição do primeiro e do segundo filme da lista. Imprima o resultado.


"""

filmes = ['The Shawshank Redemption','The Godfather','The Dark Knight','The Godfather Part II','12 Angry Men','Schindler_s List',
          'The Lord of the Rings: The Return of the King ', 'Pulp Fiction','The Lord of the Rings: The Fellowship of the Ring',
          'The Good, the Bad and the Ugly']

filmes.pop(1)
filmes.insert(0,'The Godfather')

print(filmes)

"""---

## 2\. Conjuntos

Aconteceu um erro no seu *ranking*. Simule a duplicação dos três últimos filmes da lista. Imprima o resultado.
"""

filmes = ['The Shawshank Redemption','The Godfather','The Dark Knight','The Godfather Part II','12 Angry Men',
          'Schindler_s List',' The Lord of the Rings_The Return of the King ','Pulp Fiction',
          'The Lord of the Rings_The Fellowship of the Ring','The Good, the Bad and the Ugly']

filme1= ['Pulp Fiction']
filme2= ['The Lord of the Rings_The Fellowship of the Ring']
filme3= ['The Good, the Bad and the Ugly']

filmes_error = filmes + filme1 + filme2 + filme3
print (filmes_error)

"""Utiliza a conversão `set` e `list` para remover os valores duplicados. Imprima o resultado."""

filmes = {'The Shawshank Redemption','The Godfather','The Dark Knight','The Godfather Part II','12 Angry Men',
          'Schindler_s List',' The Lord of the Rings_The Return of the King ','Pulp Fiction',
          'The Lord of the Rings_The Fellowship of the Ring','The Good, the Bad and the Ugly'}
print(filmes)
print(type(filmes))

filmes = ['The Shawshank Redemption','The Godfather','The Dark Knight', 'The Godfather Part II', '12 Angry Men'
          'Schindler_s List', ' The Lord of the Rings_The Return of the King','Pulp Fiction',
          'The Lord of the Rings_The Fellowship of the Ring',
          'The Good, the Bad and the Ugly', 'Pulp Fiction','The Lord of the Rings_The Fellowship of the Ring',
          'The Good, the Bad and the Ugly']

filmes_sem_duplicatas = set(filmes)

print(filmes_sem_duplicatas)



filmes = ['The Shawshank Redemption','The Godfather','The Dark Knight','The Godfather Part II','12 Angry Men',
          'Schindler_s List',' The Lord of the Rings_The Return of the King ','Pulp Fiction','The Lord of the Rings_The Fellowship of the Ring',
          'The Good, the Bad and the Ugly']

"""---

## 3\. Dicionários

Repita os exercícios da parte 1 (listas). Os elementos da lista `filmes` devem ser dicionários no seguinte formato: `{'nome': <nome-do-filme>, 'ano': <ano do filme>}, 'sinopse': <sinopse do filme>}`.

filmes = {'nome':'The Shawshank Redemption',\, 'ano': '1994', 'sinopse':'Over the course of several years, two convicts form a friendship, seeking consolation and, eventually, redemption basic compassion.'}
print(filmes)
"""

#filmes = ['The Shawshank Redemption','The Godfather','The Dark Knight','The Godfather Part II','12 Angry Men',
 #         'Schindler_s List',' The Lord of the Rings_The Return of the King ','Pulp Fiction',
 #          'The Lord of the Rings_The Fellowship of the Ring','The Good, the Bad and the Ugly']

filmes = {'nome': 'The Shawshank Redemption', 'ano': 1994, 'sinopse': 'Over the course of several years, two convicts form a friendship, seeking consolation, eventually, redemption basic compassion.'}
print(filmes)

filmes_1 = {'nome': 'Filme 1: The Shawshank Redemption', 'ano': 'Ano: 1994', 'sinopse': 'Sinopse: Over the course of several years, two convicts form a friendship, seeking consolation, eventually, redemption basic compassion.'}
print(filmes_1['nome'], '\n',filmes_1['ano'], '\n',filmes_1['sinopse'], '\n', '\n')

filmes_2 = {'nome': 'Filme 2: The Godfather', 'ano': 'Ano: 1972', 'sinopse': 'Sinopse:The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'}
print(filmes_2['nome'], '\n',filmes_2['ano'], '\n',filmes_2['sinopse'], '\n', '\n')

filmes_3 = {'nome': 'Filme 3: The Dark Knight', 'ano': 'Ano: 2008', 'sinopse': 'Sinopse:When the menace known as the Joker wreaks havoc, chaos on the people of Gotham, Batman must accept one of the greatest psychological,physical tests of his ability to fight injustice.'}
print(filmes_3['nome'], '\n',filmes_3['ano'], '\n',filmes_3['sinopse'], '\n', '\n')

filmes_4 = {'nome': 'Filme 4: The Godfather Part II', 'ano': 'Ano:1974' , 'sinopse': 'Sinopse:The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.'}
print(filmes_4['nome'], '\n',filmes_4['ano'], '\n',filmes_4['sinopse'],'\n', '\n')

filmes_5 = {'nome': 'Filme 5: 12 Angry Men', 'ano': 'Ano: 1957', 'sinopse': 'Sinopse:The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.'}
print(filmes_5['nome'], '\n',filmes_5['ano'], '\n',filmes_5['sinopse'],'\n', '\n')

filmes_6 = {'nome': 'Filme 6: Schindler_s List', 'ano': 1993, 'sinopse': 'Sinopse:In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.'}
print(filmes_6['nome'], '\n',filmes_6['ano'], '\n',filmes_6['sinopse'],'\n', '\n')

filmes_7 = {'nome': 'Filme 7: The Lord of the Rings: The Return of the King', 'ano': 'Ano: 2003', 'sinopse': 'Sinopse:Gandalf and Aragorn lead the World of Men against Sauron_s army to draw his gaze from_ Frodo , Sam As they approach Mount Doom , the One Ring.'}
print(filmes_7['nome'], '\n',filmes_7['ano'], '\n',filmes_7['sinopse'],'\n', '\n')

filmes_8 = {'nome': 'Filme 8: Pulp Fiction', 'ano': 'Ano: 1994', 'sinopse': 'Sinopse:The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'}
print(filmes_8['nome'], '\n',filmes_8['ano'], '\n',filmes_8['sinopse'],'\n', '\n')

filmes_9 = {'nome': 'Filme 9: The Lord of the Rings: The Fellowship of the Ring', 'ano': 'Ano: 1994', 'sinopse': 'Sinopse:The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'}
print(filmes_9['nome'], '\n',filmes_9['ano'], '\n',filmes_9['sinopse'],'\n', '\n')

filmes_10 = {'nome': 'Filme 10: The Good, the Bad and the Ugly', 'ano': 'Ano: 1966', 'sinopse': 'Sinopse:A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.'}
print(filmes_10['nome'], '\n',filmes_10['ano'], '\n',filmes_10['sinopse'],'\n', '\n')

filmes_1 = {'nome': 'Filme 1: The Shawshank Redemption', 'ano': 'Ano: 1994', 'sinopse': 'Sinopse: Over the course of several years, two convicts form a friendship, seeking consolation, eventually, redemption basic compassion.'}

filmes_2 = {'nome': 'Filme 2: The Godfather', 'ano': 'Ano: 1972', 'sinopse': 'Sinopse:The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'}

filmes_3 = {'nome': 'Filme 3: The Dark Knight', 'ano': 'Ano: 2008', 'sinopse': 'Sinopse:When the menace known as the Joker wreaks havoc, chaos on the people of Gotham, Batman must accept one of the greatest psychological,physical tests of his ability to fight injustice.'}

filmes_4 = {'nome': 'Filme 4: The Godfather Part II', 'ano': 'Ano:1974' , 'sinopse': 'Sinopse:The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.'}

filmes_5 = {'nome': 'Filme 5: 12 Angry Men', 'ano': 'Ano: 1957', 'sinopse': 'Sinopse:The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.'}

filmes_6 = {'nome': 'Filme 6: Schindler_s List', 'ano': 1993, 'sinopse': 'Sinopse:In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.'}

filmes_7 = {'nome': 'Filme 7: The Lord of the Rings: The Return of the King', 'ano': 'Ano: 2003', 'sinopse': 'Sinopse:Gandalf and Aragorn lead the World of Men against Sauron_s army to draw his gaze from_ Frodo , Sam As they approach Mount Doom , the One Ring.'}

filmes_8 = {'nome': 'Filme 8: Pulp Fiction', 'ano': 'Ano: 1994', 'sinopse': 'Sinopse:The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'}

filmes_9 = {'nome': 'Filme 9: The Lord of the Rings: The Fellowship of the Ring', 'ano': 'Ano: 1994', 'sinopse': 'Sinopse:The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'}

filmes_10 = {'nome': 'Filme 10: The Good, the Bad and the Ugly', 'ano': 'Ano: 1966', 'sinopse': 'Sinopse:A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.'}



ranking = [filmes_1,filmes_2,filmes_3,filmes_4,filmes_5,filmes_6,filmes_7,filmes_8,filmes_9,filmes_10]


for filme in ranking:
    print('{}\n{}\n{}\n'.format(filme['nome'], filme['ano'], filme['sinopse']))

print(type(ranking))

