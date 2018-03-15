# Introduction à Python [![GitHub stars](https://img.shields.io/github/stars/Tofull/introduction_python.svg?style=social&label=Star)](https://GitHub.com/Tofull/introduction_python/stargazers/)

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/fold_left.svg?logo=twitter&style=social&label=_Tofull)](https://twitter.com/_Tofull) [![Github URL](https://img.shields.io/badge/style--green.svg?logo=github&style=social&label=tofull)](https://github.com/tofull)

Une introduction à Python écrite par Loïc Messal.

Cette introduction est conçue pour faire découvrir des notions de programmation à travers le langage python. 
Aucune connaissance/expérience préalable liée à cet univers n'est nécessaire.

L'objectif est de comprendre certains concepts et gagner en autonomie avec la programmation.

Organisée comme telle :
- [Chapitre 0 : L'histoire de Python](00_Python.ipynb)
- Chapitre 1 : Les variables de bases
- Chapitre 2 : Les variables plus complexes
- Chapitre 3 : Les tests et boucles
- Chapitre 4 : Les fonctions
- Chapitre 5 : Des fonctions pour les variables complexes
- Chapitre 6 : La Programmation Orientée Objet
- Chapitre 7 : Des snippets (manipuler des fichiers)
- Chapitre 8 : Les snippets en pratique
- Chapitre 9 : Des modules standards
- Chapitre 10 : Introduction à d'autres modules
- Chapitre 11 : Des outils pour reproduire tout ça

## Détails
Ces notebooks sont accessibles directement depuis Github. Ils ont toutefois été pensés pour être lus par le module RISE (permettant de coupler jupyter et reveal.js) afin d'avoir une présentation live.

## Voir l'introduction
Il existe plusieurs possibilités pour voir cette introduction :
- avec play with docker (recommandée) :  
    [![Try in PWD](https://cdn.rawgit.com/play-with-docker/stacks/cff22438/assets/images/button.png)](http://play-with-docker.com?stack=https://raw.githubusercontent.com/tofull/introduction_python/master/docker_stack.yml&stack_name=notebooks)

- avec github :  
    commencer directement sur `https://github.com/Tofull/introduction_python/blob/master/00_Python.ipynb` (attention, la présentation RISE n'est pas disponible avec ce mode)

- en local avec docker :  
    ```sh
    git clone https://github.com/Tofull/introduction_python
    cd introduction_python
    docker build -t introduction_python .
    docker run -it -p 8888:8888 --rm introduction_python
    ```
    et aller sur `http://localhost:8888/notebooks/00_Python.ipynb`

- en local (non recommandé) :  
    ```sh
    git clone https://github.com/Tofull/introduction_python
    cd introduction_python
    pip install jupyter
    pip install RISE
    pip install -r requirements.txt
    jupyter notebook --ip=0.0.0.0
    ```
    et aller sur `http://localhost:8888/notebooks/00_Python.ipynb`


## Motivation
Cette introduction a été écrite pour répondre aux besoins des économistes de JLR, une société qui évalue le prix des biens immobiliers sur toute l'Amérique du nord. Un seul des économistes connaissait python. Il souhaitait faire monter en compétence l'ensemble de son équipe pour travailler en commun et m'a demandé de rédiger cette introduction. C'est finalement bien plus que l'équipe des économistes qui a bénéficié de cette introduction.

## Social
Si tu apprécies cette introduction, laisses-y une étoile :star: : [![GitHub stars](https://img.shields.io/github/stars/Tofull/introduction_python.svg?logo=github&style=social&label=Star)](https://GitHub.com/Tofull/introduction_python/stargazers/)

Si tu repères une amélioration ou une fausseté, merci de l'indiquer à la communauté [en créant une issue](https://github.com/Tofull/introduction_python/issues/new). Peut-être qu'une issue similaire a déjà été soulevée. [Une petite vérification](https://github.com/Tofull/adventure/issues) avant de poster la tienne peut t'aider.

Pour suivre mes activités : [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/fold_left.svg?logo=twitter&style=social&label=_Tofull)](https://twitter.com/_Tofull) [![Github URL](https://img.shields.io/badge/style--green.svg?logo=github&style=social&label=tofull)](https://github.com/tofull) [![Blog URL](https://img.shields.io/badge/style--green.svg?style=social&label=sur%20mon%20blog)](https://tofull.github.io/) 