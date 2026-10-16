# Python finance basics

Traitement de données de marché en Python. Exercices réalisés en septembre 2026
dans le cadre d'une préparation à l'alternance en gestion d'actifs.

![Performance cumulée de 3 ETF STOXX Europe 600, base 100](images/base100.png)

## Notebooks

| Fichier | Contenu |
|---|---|
| `01_rendements_journaliers.ipynb` | Rendement quotidien d'un titre, meilleure et pire séance |
| `02_rendements_par_titre.ipynb` | Rendements par titre sur un fichier multi-valeurs, tickers découverts à la lecture |
| `03_lecture_csv_bourse.ipynb` | Lecture d'un historique CSV réel, gestion des données manquantes |
| `04_comparaison_etf_europe.ipynb` | Trois ETF STOXX Europe 600 comparés en base 100 — l'écart de performance confronté à l'écart de frais |
| `05_indicateurs_risque.ipynb` | Volatilité et rendement annualisés, distribution des rendements, maximum drawdown des 3 ETF |
| `06_sharpe_correlations.ipynb` | Ratio de Sharpe sous trois hypothèses de taux, corrélations entre fonds, apport d'une classe obligataire |

Les notebooks 01 à 03 n'utilisent que la bibliothèque standard. Le notebook 04 introduit pandas, yfinance et matplotlib, le notebook 05 approfondit matplotlib, le notebook 06 ajoute seaborn.

![Performance cumulée et drawdown de 3 ETF STOXX Europe 600](images/drawdown.png)

## Données

`data/aapl_us_d.csv` — historique quotidien Apple depuis 1984 (source : stooq.com).
`data/prix.txt` et `data/cotations.txt` — fichiers d'exercice, format `date;prix` et `ticker;date;prix`.
`data/etf_europe.csv` — cours de clôture ajustés de MEUD.PA, ETZ.PA et EXSA.DE,
téléchargés via yfinance le 25 septembre 2026.
`data/actions_obligations.csv` — les trois ETF actions et IEGA.AS (iShares Core € Govt Bond), 659 séances communes.

## Notions travaillées

Lecture de fichiers, dictionnaires, listes, module `csv`, gestion d'erreurs,
calcul de rendements simples et composés.

Avec pandas : `read_csv` et index temporel, `dropna`, `pct_change`, `groupby`,
mise en base 100, graphique de performance cumulée.

Indicateurs de risque : volatilité annualisée, rendement annualisé (CAGR), maximum drawdown, ratio de Sharpe, matrice de corrélation, heatmap avec `seaborn`.

## Environnement

Python 3. Les notebooks 01 à 03 s'exécutent sans installation. Les notebooks 04 et 05 requièrent `pandas`, `matplotlib` et, pour le 04, `yfinance`. Le notebook 06 requiert `seaborn`.

Tous utilisent des chemins relatifs et s'exécutent tels quels après clonage du dépôt.
