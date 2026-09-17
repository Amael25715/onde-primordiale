#!/usr/bin/env python3
"""Tests unitaires pour analyse_hydrogene.py"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from analyse_hydrogene import (
    charge_constantes_reference,
    compare_a_reference,
    resume_ecarts,
    ALPHA_INV,
)


def test_reference_keys():
    ref = charge_constantes_reference()
    assert "alpha_inv" in ref
    assert "mu" in ref
    assert ref["alpha_inv"] == ALPHA_INV
    print("OK  test_reference_keys")


def test_compare_zero_ecart():
    ref = charge_constantes_reference()
    ecarts = compare_a_reference(ref, ref)
    for v in ecarts.values():
        assert v is not None and abs(v) < 1e-15
    print("OK  test_compare_zero_ecart")


def test_compare_ecart_connu():
    ref = {"alpha_inv": 100.0}
    mesure = {"alpha_inv": 101.0}
    ecarts = compare_a_reference(mesure, ref)
    assert abs(ecarts["alpha_inv"] - 0.01) < 1e-12
    print("OK  test_compare_ecart_connu")


def test_resume_non_vide():
    text = resume_ecarts({"alpha_inv": 0.0})
    assert "alpha_inv" in text
    print("OK  test_resume_non_vide")


if __name__ == "__main__":
    test_reference_keys()
    test_compare_zero_ecart()
    test_compare_ecart_connu()
    test_resume_non_vide()
    print("TOUS LES TESTS analyse_hydrogene SONT PASSES")
