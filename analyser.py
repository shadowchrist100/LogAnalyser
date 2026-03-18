#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os
import re
import sys
from collections import Counter

def analyser_logs(dossier_source, niveau_filtre='ALL'):
    
    # Récupération du chemin absolu pour respecter les contraintes techniques
    abs_source = os.path.abspath(dossier_source)
    
    if not os.path.isdir(abs_source):
        raise FileNotFoundError(f"Le dossier source n'existe pas : {abs_source}")

    # Regex correspondant au format imposé : YYYY-MM-DD HH:MM:SS NIVEAU Message
    log_pattern = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (?P<niveau>INFO|WARN|ERROR) (?P<message>.*)$')
    
    stats = {
        "total_lignes": 0,
        "par_niveau": {"ERROR": 0, "WARN": 0, "INFO": 0},
        "top5_erreurs": [],
        "fichiers_traites": []
    }
    
    compteur_erreurs = Counter()
    compteur_niveaux = Counter({"ERROR": 0, "WARN": 0, "INFO": 0})

    # Scan des fichiers .log
    fichiers = glob.glob(os.path.join(abs_source, "*.log"))
    
    for fichier in fichiers:
        chemin_complet = os.path.abspath(fichier)
        stats["fichiers_traites"].append(chemin_complet)
        
        try:
            with open(chemin_complet, 'r', encoding='utf-8', errors='ignore') as f:
                for ligne in f:
                    ligne = ligne.strip()
                    if not ligne:
                        continue
                        
                    stats["total_lignes"] += 1
                    match = log_pattern.match(ligne)
                    
                    if match:
                        niv = match.group('niveau')
                        msg = match.group('message')
                        
                        # On compte le niveau pour les statistiques globales
                        compteur_niveaux[niv] += 1
                        
                        if (niveau_filtre == 'ALL' or niveau_filtre == niv) and niv == 'ERROR':
                            compteur_erreurs[msg] += 1
        except Exception as e:
            print(f"Erreur lors de la lecture de {fichier} : {e}", file=sys.stderr)

    # Mise à jour des résultats finaux
    stats["par_niveau"] = dict(compteur_niveaux)
    stats["top5_erreurs"] = [list(item) for item in compteur_erreurs.most_common(5)]
    
    return stats