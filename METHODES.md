# METHODES.md – Pistes de test et de contrainte

## 1. Objectif méthodologique

Transformer autant que possible des hypothèses spéculatives en :
- prédictions falsifiables, ou
- affirmations explicitement classées « non testables avec les outils actuels ».

## 2. Pistes concrètes

### Spectroscopie / hydrogène
- Chercher des résidus inexpliqués dans les mesures de précision (raies, structure hyperfine).
- Comparer avec les prédictions QED actuelles.
- Bibliothèques utiles : numpy, scipy, éventuellement bases de données spectrales publiques.

### Stabilité des constantes
- Suivre les limites publiées sur la variation de α, μ = m_p/m_e, etc.
- Toute détection de variation serait un signal fort (dans un sens ou dans l'autre).

### Simulations de paramètres alternatifs
- Explorer (comme la littérature de fine-tuning) ce qui se passe si l'on modifie légèrement des constantes.
- Documenter les fenêtres de complexité (atomes, étoiles, chimie).

### Indicateurs « cycles / déchets » (application terrestre)
- Même si hors cosmogonie stricte : mesurer des flux hors cycle (déchets, centralisation) comme proxy d'alignement opérationnel.

## 3. Ce qu'on ne fait pas

- Affirmer que l'hypothèse est démontrée.
- Confondre boussole éthique et description physique.
- Ignorer les contraintes observationnelles existantes.

## 4. Prochaines actions techniques

1. Stub d'analyse de données hydrogène (`code/analyse_hydrogene.py`).
2. Liste de références (papers fine-tuning, mesures de constantes).
3. Tableau des grandeurs à surveiller (mise à jour récurrente).
