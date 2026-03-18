#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import sys
import platform
# Import des autres modules
from analyser import analyser_logs 
import rapport
import archiver

def main():
    parser = argparse.ArgumentParser(description="LogAnalyzer Pro - Ingestion et Analyse")
    parser.add_argument('--source', required=True, help="Chemin vers le dossier de logs")
    parser.add_argument('--niveau', choices=['ERROR', 'WARN', 'INFO', 'ALL'], default='ALL', 
                        help="Niveau de filtrage (défaut : ALL)")
    
    args = parser.parse_args()

    try:
        # Exécution de l'analyse
        resultats = analyser_logs(args.source, args.niveau)
        
        # Récupération des métadonnées
        utilisateur = os.environ.get('USER') or os.environ.get('USERNAME') or "Inconnu"
        systeme = platform.system()
        
        # Affichage pour validation (Module 1)
        print("-" * 30)
        print(f"RAPPORT D'ANALYSE (Utilisateur: {utilisateur} | OS: {systeme})")
        print("-" * 30)
        print(f"Fichiers traités : {len(resultats['fichiers_traites'])}")
        print(f"Total lignes analysées : {resultats['total_lignes']}")
        print(f"Répartition par niveau : {resultats['par_niveau']}")
        print(f"Top 5 Erreurs : {resultats['top5_erreurs']}")
        print("-" * 30)
        
        # Étape 2 : Rapport (Étudiant 4)
        # chemin_rapport = rapport.generer_json(resultats, source)
        
        # Étape 3 : Archivage (Étudiant 3)
        # archiver.traiter_archives(resultats['fichiers_traites'], dest, retention)
        
        print("Traitement terminé avec succès.")
    except Exception as e:
        print(f"Erreur fatale : {e}")
        sys.exit(1) # [cite: 41]

if __name__ == "__main__":
    main()