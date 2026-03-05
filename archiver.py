#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tarfile
import shutil
import os
import time
import subprocess

def verifier_espace_disque():
    """Vérifie l'espace via subprocess avant archivage."""
    # Piste : Utilisez subprocess.check_output(['df', '-h']) [cite: 39]
    pass

def traiter_archives(fichiers, dossier_dest, jours_retention):
    """Archive les logs et nettoie les vieux rapports."""
    # Piste Archivage : tarfile.open(..., "w:gz") [cite: 34]
    # Piste Nettoyage : os.path.getmtime() pour l'âge [cite: 38]
    pass