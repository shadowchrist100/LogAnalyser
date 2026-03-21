#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tarfile
import shutil
import os
import time
import subprocess

def verifier_espace_disque(fichiers, dossier_dest):
    """Vérifie l'espace via subprocess avant archivage."""
    # 1. Calculer la taille totale des logs à archiver
    taille_totale_logs = sum(os.path.getsize(f) for f in fichiers if os.path.exists(f))
    try:
        # 1. Exécuter la commande df -h
        output = subprocess.check_output(['df', '-B1', dossier_dest]).decode('utf-8')
        
        # 2. Parser la sortie
        lines = output.strip().split('\n')
        if len(lines) >= 2:
            # 3. Prendre la ligne du disque principal (ligne 1)
            parts = lines[1].split()
            if len(parts) >= 4:
                # 4. Récupérer l'espace disponible (colonne 3)
                espace_dispo = int(parts[3])  # "74G" dans l'exemple
                print(f"Espace disque disponible : {espace_dispo}")
                return espace_dispo >= taille_totale_logs
        return False
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la vérification de l'espace disque : {e}")
        return False

def traiter_archives(fichiers, dossier_dest, jours_retention, dossier_rapport):
    """Archive les logs et nettoie les vieux rapports."""
    
    # 1. Vérifier l'espace disque AVANT l'archivage
    if not verifier_espace_disque(fichiers, dossier_dest):
        print("Espace disque insuffisant, archivage annulé.")
        return False
    
    # 2. Créer le dossier de destination s'il n'existe pas
    os.makedirs(dossier_dest, exist_ok=True)
    
    # 3. Créer l'archive avec timestamp (temporairement dans le dossier courant)
    timestamp = time.strftime("%Y-%m-%d")  # Format demandé: backup_YYYY-MM-DD.tar.gz
    nom_archive_temp = f"backup_{timestamp}.tar.gz"
    nom_archive_final = os.path.join(dossier_dest, nom_archive_temp)
    
    # 4. Archivage des fichiers (création temporaire)
    try:
        with tarfile.open(nom_archive_temp, "w:gz") as tar:
            for fichier in fichiers:
                if os.path.exists(fichier):
                    tar.add(fichier, arcname=os.path.basename(fichier))
                    print(f"Ajouté à l'archive : {fichier}")
        
        # 5. DÉPLACER l'archive vers la destination avec shutil
        shutil.move(nom_archive_temp, nom_archive_final)
        print(f"Archive déplacée vers : {nom_archive_final}")
        
        # 6. Nettoyage des vieux rapports JSON
        temps_actuel = time.time()
        seuil_temps = temps_actuel - (jours_retention * 24 * 60 * 60)  # Conversion en secondes
        
        if os.path.exists(dossier_rapport):
            for fichier in os.listdir(dossier_rapport):
                chemin_fichier = os.path.join(dossier_rapport, fichier)
                # Vérifier que c'est un fichier JSON
                if os.path.isfile(chemin_fichier) and fichier.endswith('.json'):
                    age_fichier = os.path.getmtime(chemin_fichier)
                    if age_fichier < seuil_temps:
                        os.remove(chemin_fichier)
                        print(f"Supprimé (vieux rapport JSON) : {fichier}")
        
        return True
        
    except Exception as e:
        print(f"Erreur lors de l'archivage : {e}")
        return False