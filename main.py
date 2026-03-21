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
    # 1. Configuration d'argparse pour --source, --niveau, --dest, --retention
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Préciser la source des fichiers log à analyser")
    parser.add_argument("--niveau", default="ALL", choices=["ERROR", "WARN", "INFO", "ALL"], help="Niveau de filtrage")
    parser.add_argument("--retention", type =int, default=30, help="Duree avant suppression des archives" )
    parser.add_argument("--dest",  required=True, help="Dossier de destination des archives" )
    args = parser.parse_args()

    # Récupération du chemin absolu de la source et de la destination
    # Traduction du tilde par le chemin absolu du dossier personel de l'utilisateur
    source = os.path.expanduser(args.source)
    dest = os.path.expanduser(args.dest)
    source = os.path.abspath(source)
    dest = os.path.abspath(dest)
    if not os.path.isdir(source) :
        raise FileNotFoundError(f"Le dossier source n'existe pas : {source}")
        sys.exit(1)
        pass
    # 2. Construction du chemin absolu du dossier source
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(BASE_DIR, "rapports"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "backups"), exist_ok=True)
    try:
        # Étape 1 : Démarage de l'analyse des logs
        resultats = analyser_logs(source, args.niveau)
        # Étape 2 :Démarage de la rédaction du rapport
        rapport.generer_json(resultats, source, "rapports")
         # Étape 3 : Démarage de l'archivage
        archiver.traiter_archives(resultats['fichiers_traites'], dest, args.retention, "rapports")

        print("Traitement terminé avec succès.")
    except Exception as e:
        print(f"Erreur fatale : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()