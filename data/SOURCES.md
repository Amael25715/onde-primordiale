# Sources de données – Hydrogène et constantes

On ne stocke pas ici de gros fichiers spectrales (licence, taille, mise à jour).  
On documente **où** les récupérer et comment les utiliser.

## Spectres / raies de l'hydrogène

1. **NIST Atomic Spectra Database**  
   - URL : https://physics.nist.gov/PhysRefData/ASD/lines_form.html  
   - Requête typique : élément `H`, spectre de raies  
   - Export possible en TSV / ASCII

2. **CODATA** (constantes fondamentales)  
   - https://physics.nist.gov/cuu/Constants/  
   - Utile pour α, m_p/m_e, Rydberg, etc.

3. **Articles de précision** (structure hyperfine, 1S-2S)  
   - Chercher les mesures récentes de la fréquence 1S-2S de l'hydrogène (laboratoires de métrologie).

## Fichiers locaux (optionnel)

Si tu télécharges un export NIST, place-le par exemple dans :

```
data/hydrogene/nist_H_lines.tsv
```

(ne pas committer de très gros fichiers sans accord)

## Utilisation prévue

- Comparer des mesures tabulées aux prédictions QED.
- Documenter tout écart résiduel (sans l'interpréter prématurément comme preuve d'onde primordiale).
