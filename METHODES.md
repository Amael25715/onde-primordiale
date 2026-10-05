# METHODES.md - Pistes de test et d'invalidation

**Mise a jour :** 6 octobre 2026

## 1. Objectif

Transformer autant que possible le niveau 0 (parabole) en :
- niveau 2 (prediction ou borne), ou
- mention explicite **non testable avec les outils actuels**.

Regle : une intuition sans test ni etiquette non testable n'entre pas dans les decisions techniques des autres depots.

## 2. Tests classes

| Test | Ce que ca departage | Statut |
|------|---------------------|--------|
| Dynamique de l'energie noire (DESI, supernovae, Euclid) | Lambda fige vs champ qui evolue | En cours ; thawing a confirmer |
| GW stochastiques (LISA, pulsar timing) | Transition de phase / choc primordial | Prochaine decennie |
| Echos / spectroscopie fusions TN | Horizon classique vs structure / rebond | LIGO/Virgo/KAGRA, LISA |
| Courbe de Page (theorie + analogues labo) | Info perdue vs conservee dans notre espace | Actif en theorie |
| Variation de alpha, mu = m_e/m_p (horloges, astro) | Constantes vraiment fixes | Bornes deja tres serrees |
| Masse max des etoiles a neutrons | Version naive Smolin (univers-bebes) | Deja sous pression (~2+ Msun) |
| Stabilite du vide de Higgs (m_top, couplages) | Notre vide = minimum local ou pas | LHC / futurs collideurs |
| CMB : non-gaussianites, anomalies grande echelle | Relique d'un avant / d'un choc | Donnees existantes, lecture disputee |
| Spectroscopie H vs QED | Residu inexplique (proxy, pas preuve d'onde) | NIST / metrologie ; stub code/analyse_hydrogene.py |

### Ce qui ne teste pas le dehors du ballon

- Une frequence unique de l'hydrogene.
- Le boson de Higgs est l'onde primordiale.

Trop en aval, trop d'explications concurrentes.

## 3. Invalidation

On prefere une hypothese **tuable** a une hypothese indestructible.

- Energie noire = constante ET aucun fond GW de transition ET horizons parfaitement classiques -> la parabole choc + fond evolutif perd ses leviers proches.
- Info des TN detruite (rupture d'unitarite) -> voie A cassee ; restent B/C ou autre physique.
- Variation de constantes incoherente avec un seul tempo -> a retravailler, pas a celebrer prematurement.

## 4. Spectroscopie / hydrogene (proxy labo)

- Comparer NIST / 1S-2S aux predictions QED.
- Documenter tout ecart residuel **sans** l'interpreter comme preuve d'onde.
- Code : `code/analyse_hydrogene.py`.
- Sources : `data/SOURCES.md`.

## 5. Fine-tuning

Documenter les fenetres de complexite (atomes, etoiles, chimie) comme *contrainte*. Ca oriente la boussole, ca ne prouve pas un designer.

## 6. Indicateurs terrestres (niveau 0 uniquement)

Cycles / dechets / centralisation : proxy operationnel (gouttes, ethique), **pas** une mesure de l'onde primordiale.

## 7. Ce qu'on ne fait pas

- Affirmer que l'hypothese est demontree.
- Confondre boussole ethique et description physique.
- Fusionner ce depot avec gouttes-eau au niveau des claims cosmologiques.
- Coder un detecteur d'onde primordiale sans prediction chiffree distincte du MS.
