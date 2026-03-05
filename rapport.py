#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import datetime
import os

def generer_json(donnees_analyse, dossier_source):
    """
    Prend les stats et crée le fichier rapport_YYYY-MM-DD.json.
    """
    # Piste : Construisez le dictionnaire final avec les clés :
    # metadata (date, utilisateur, os, source) [cite: 32]
    # statistiques (total_lignes, par_niveau, top5_erreurs) [cite: 32]
    # fichiers_traites [cite: 32]
    
    # Utilisez json.dump(dictionnaire, fichier, indent=4)
    pass