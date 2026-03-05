#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os
import platform

def analyser_logs(dossier_source, niveau_filtre="ALL"):
    """
    Scanne le dossier, filtre les lignes et calcule les stats.
    Retourne un dictionnaire prêt pour le module rapport.
    """
    # Pistes :
    # - Utilisez glob.glob(os.path.join(dossier_source, "*.log")) [cite: 23]
    # - Métadonnées : platform.system() et os.environ.get('USER') [cite: 29, 32]
    # - Structure de retour attendue :
    return {
        "total_lignes": 0,
        "par_niveau": {"ERROR": 0, "WARN": 0, "INFO": 0},
        "top5_erreurs": [],
        "fichiers_traites": []
    }