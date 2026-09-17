# Python finance basics

Traitement de données de marché en Python, sans bibliothèque externe.
Exercices réalisés en septembre 2026 dans le cadre d'une préparation
à l'alternance en gestion d'actifs.

## Notebooks

| Fichier | Contenu |
|---|---|
| `01_rendements_journaliers.ipynb` | Rendement quotidien d'un titre, meilleure et pire séance |
| `02_rendements_par_titre.ipynb` | Rendements par titre sur un fichier multi-valeurs, tickers découverts à la lecture |
| `03_lecture_csv_bourse.ipynb` | Lecture d'un historique CSV réel, gestion des données manquantes |

## Données

`data/aapl_us_d.csv` — historique quotidien Apple depuis 1984 (source : stooq.com).
`data/prix.txt` et `data/cotations.txt` — fichiers d'exercice, format `date;prix` et `ticker;date;prix`.

## Notions travaillées

Lecture de fichiers, dictionnaires, listes, module `csv`, gestion d'erreurs,
calcul de rendements simples et composés.

## Environnement

Python 3, sans dépendance. Les notebooks utilisent des chemins relatifs
et s'exécutent tels quels après clonage du dépôt.
