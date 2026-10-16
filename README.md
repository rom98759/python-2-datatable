# python-2-datatable

**Piscine Python pour la Data Science de l'École 42 — module 02 « DataTable ».**
Chargement, filtrage et visualisation de jeux de données socio-économiques
(espérance de vie, population, revenu par pays) avec **pandas** et **matplotlib**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![matplotlib](https://img.shields.io/badge/matplotlib-11557c?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-1a1a1a?style=flat-square)

<!-- CAPTURE À FOURNIR : déposer les graphes générés, ex. docs/ex01.png / docs/ex03.png -->
> 📈 _Graphiques générés par ex01/ex02/ex03 — captures à venir._

## Exercices

| Ex | Fichier | Ce qu'il fait |
|----|---------|---------------|
| **00** | `ex00/load_csv.py` | Charge un CSV, affiche ses dimensions et le retourne en `DataFrame`. |
| **01** | `ex01/aff_life.py` | Trace l'**espérance de vie** d'un pays au fil des années. |
| **02** | `ex02/aff_pop.py` | Compare la **population** de deux pays sur une même courbe. |
| **03** | `ex03/projection_life.py` | Nuage de points **espérance de vie / revenu**, avec conversion des valeurs `3.25M`, `400k`, `1.2B` en nombres. |

## Lancement

Prérequis : Python 3 + les dépendances.

```bash
pip install -r requirements.txt     # pandas, matplotlib
python ex01/aff_life.py             # affiche le graphe
```

> Les scripts attendent les CSV fournis par le sujet (espérance de vie,
> population, revenu). Place-les à côté des scripts ou adapte le chemin dans
> `load_csv.py`.

## Structure

```
ex00/   chargement d'un CSV en DataFrame
ex01/   espérance de vie dans le temps (1 pays)
ex02/   comparaison de population (2 pays)
ex03/   projection espérance de vie vs revenu
```

## Licence

MIT — voir [LICENSE](LICENSE).
