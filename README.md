# Onde Primordiale

Recherche exploratoire : formuler des **paraboles de travail** sur des trous du Modele Standard + relativite generale, puis les confronter a la physique connue.

**Ceci n'est pas une doctrine.** C'est un laboratoire d'hypotheses : imaginer ce qui *pourrait* relier conservation, horizons et vide, puis **challenger** jusqu'a ce que ca tienne ou casse.

**Statut** : exploratoire. Toute affirmation doit porter un niveau (voir `THEORIE.md`).

Alignement operationnel : #25715 #3812155 (cohesion = collaboration, pas domination).

## Trois niveaux (obligatoires)

| Niveau | Role | Exemple |
|--------|------|---------|
| **0 - Boussole** | Image / parabole pour orienter les questions | stase + choc, ballon, Amour = cohesion |
| **1 - Hypothese** | Enonce physique encore ouvert | vide metastable, info des TN, energie du vide |
| **2 - Test** | Mesure, borne, ou explicitement non testable | DESI, LISA, alpha, Page curve, masse NS |

Confondre 0 et 2 est une erreur de methode.

## Prerequis

- Python 3.10+
- (optionnel) `numpy`

```bash
python -m venv .venv
source .venv/bin/activate
pip install numpy
python code/test_analyse_hydrogene.py
```

## Structure

```
onde-primordiale/
|-- README.md
|-- THEORIE.md
|-- METHODES.md
|-- DECISIONS.md
|-- data/SOURCES.md
|-- code/analyse_hydrogene.py
|-- code/test_analyse_hydrogene.py
```

## Contribution

Issues / PR. Challenger est le mode par defaut.
Une intuition sans niveau est a classer avant d'etre debattue comme fait.
