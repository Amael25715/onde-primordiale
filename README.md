# Onde Primordiale

Recherche exploratoire sur l'hypothèse d'une onde / force de cohésion primordiale, ses liens possibles avec l'hydrogène, les constantes fondamentales et les invariants observables.

**Statut** : cadre exploratoire et spéculatif.  
Objectif : formuler des pistes testables (ou clairement non testables) et documenter ce qui est cohérent avec les connaissances actuelles.

Aligné Message (#25715 #3581215).

## Prérequis

- Python 3.10+
- (optionnel) `numpy` pour étendre les analyses

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install numpy           # optionnel
python code/test_analyse_hydrogene.py
```

## Structure

```
onde-primordiale/
├── README.md
├── THEORIE.md          # hypothèses + niveaux de spéculation
├── METHODES.md         # pistes de test
├── DECISIONS.md
├── data/
│   └── SOURCES.md      # où trouver des données réelles (NIST, etc.)
└── code/
    ├── analyse_hydrogene.py
    └── test_analyse_hydrogene.py
```

## Ce qui n'est pas encore dans ce dépôt

- Jeux de données binaires volumineux (on pointe vers NIST plutôt que de les dupliquer).
- Simulations avancées de variation de constantes.

## Contribution

Issues et Pull Requests bienvenues. Toute affirmation doit indiquer son niveau de spéculation.
