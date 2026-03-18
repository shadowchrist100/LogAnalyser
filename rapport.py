#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module 2 : Génération de rapport JSON pour LogAnalyzer Pro
Prend les statistiques d'analyse et génère un rapport structuré
"""

import json
import datetime
import os
import platform

def generer_json(donnees_analyse, dossier_source, dossier_destination="rapports"):
    """
    Prend les stats et crée le fichier rapport_YYYY-MM-DD.json.
    
    Args:
        donnees_analyse (dict): Dictionnaire contenant:
            - statistiques: dict avec total_lignes, par_niveau, top5_erreurs
            - fichiers_traites: liste des fichiers analysés
        dossier_source (str): Chemin du dossier source analysé
        dossier_destination (str): Dossier où sauvegarder le rapport
    
    Returns:
        str: Chemin absolu du fichier rapport généré
    
    Raises:
        Exception: En cas d'erreur lors de la génération du rapport
    """
    try:
        # 1. Création des métadonnées
        metadata = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source": dossier_source
        }
        
        # 2. Construction de la structure complète du rapport
        rapport = {
            "metadata": metadata,
            "statistiques": donnees_analyse["statistiques"],
            "fichiers_traites": [os.path.abspath(f) for f in donnees_analyse["fichiers_traites"]]
        }
        
        # 3. Création du dossier de destination si nécessaire
        os.makedirs(dossier_destination, exist_ok=True)
        
        # 4. Génération du nom de fichier horodaté
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        nom_fichier = f"rapport_{date_str}.json"
        
        # 5. Construction du chemin absolu
        chemin_rapport = os.path.abspath(os.path.join(dossier_destination, nom_fichier))
        
        # 6. Écriture du fichier JSON
        with open(chemin_rapport, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, indent=4, ensure_ascii=False)
        
        print(f"Rapport JSON généré avec succès : {chemin_rapport}")
        return chemin_rapport
        
    except KeyError as e:
        print(f"Erreur : Clé manquante dans donnees_analyse - {e}")
        raise
    except Exception as e:
        print(f"Erreur lors de la génération du rapport : {e}")
        raise

if __name__ == "__main__":
    test_module()