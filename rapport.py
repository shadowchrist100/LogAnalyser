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

def test_module():
    """
    Fonction de test pour valider le module
    """
    print("Test du module rapport.py...")
    
    # Données de test simulées (ce qui viendrait du module 1)
    donnees_test = {
        "statistiques": {
            "total_lignes": 150,
            "par_niveau": {"ERROR": 1, "WARN": 15, "INFO": 134},
            "top5_erreurs": ["Échec connexion base de données"]
        },
        "fichiers_traites": [
            "logs_test/app1.log",
            "logs_test/app2.log",
            "logs_test/app3.log"
        ]
    }
    
    try:
        # Test de génération
        chemin = generer_json(donnees_test, "logs_test")
        
        # Vérification que le fichier existe
        if os.path.exists(chemin):
            print(f"Fichier créé : {chemin}")
            
            # Affiche le contenu pour vérification
            with open(chemin, 'r', encoding='utf-8') as f:
                contenu = json.load(f)
                print("\n Aperçu du rapport généré :")
                print(json.dumps(contenu, indent=2, ensure_ascii=False)[:500] + "...")
        else:
            print("Le fichier n'a pas été créé")
            
    except Exception as e:
        print(f"Test échoué : {e}")

if __name__ == "__main__":
    test_module()