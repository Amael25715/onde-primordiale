#!/usr/bin/env python3
"""
Analyse exploratoire liée à l'hydrogène et aux constantes de référence.

Objectif : point d'entrée pour charger des grandeurs tabulées et les comparer
à des références connues. N'affirme aucune détection d'anomalie.

Voir data/SOURCES.md pour les sources (NIST, CODATA).
"""

from __future__ import annotations

from typing import Any

# Valeurs approximatives de référence (mettre à jour avec CODATA si besoin)
ALPHA_INV = 137.035999084  # 1/α (CODATA-like)
MU_PROTON_ELECTRON = 1836.15267343  # m_p / m_e


def charge_constantes_reference() -> dict[str, float]:
    """Retourne un dictionnaire de grandeurs de référence.

    Returns:
        dict avec au minimum 'alpha_inv' et 'mu'.
    """
    return {
        "alpha_inv": ALPHA_INV,
        "mu": MU_PROTON_ELECTRON,
    }


def compare_a_reference(
    mesure: dict[str, float],
    reference: dict[str, float] | None = None,
) -> dict[str, float | None]:
    """Compare des mesures à une référence.

    Args:
        mesure: grandeurs mesurées ou postulées {nom: valeur}.
        reference: référence ; si None, utilise charge_constantes_reference().

    Returns:
        Écarts relatifs (mesure - ref) / ref pour chaque clé commune.
    """
    if reference is None:
        reference = charge_constantes_reference()
    ecarts: dict[str, float | None] = {}
    for k, v in mesure.items():
        if k in reference:
            ref = reference[k]
            ecarts[k] = (v - ref) / ref if ref != 0 else None
    return ecarts


def resume_ecarts(ecarts: dict[str, float | None]) -> str:
    """Formatage lisible des écarts relatifs."""
    lines = []
    for k, e in ecarts.items():
        if e is None:
            lines.append(f"  {k}: N/A")
        else:
            lines.append(f"  {k}: {e:.3e} (relatif)")
    return "\n".join(lines) if lines else "  (aucun)"


if __name__ == "__main__":
    print("analyse_hydrogene — références :")
    ref = charge_constantes_reference()
    for k, v in ref.items():
        print(f"  {k} = {v}")
    # Exemple : écart nul si on repasse les mêmes valeurs
    print("Écarts vs référence (auto) :")
    print(resume_ecarts(compare_a_reference(ref)))
