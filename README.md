# LogAnalyser -Pipeline d'Analyse et d'Archivage
## **1.Description du projet**
    LogAnalyzer Pro est un outil en ligne de commade (CLI) conçu pour automatiser la supervision des logs··
    applicatifs dans un envrionnement DevOps. Il permet d'analyser des fichiers logs, de générer des rapports..
    statistiques dans un environnement DevOps. Il permet d'analyser des fichiers logs, de générer des rapports.
___
## **2.Prérequis et installation**
    - __Version Python__ : Python 3.x..
    - **Dependances** :Aucune bibliotheque externe n'est nécessaire
    - **Installation** : Clonez le dépôt et assurez vous que les scripts ont les droits d'exécution
***
## **3.Utilisation**
    Le script principal main accepte les arguments: ..
    ```
        bash
        python3 main.py --source./logs_test --dest ./backups --niveau ERROR -- retention 15
    ```
    | Argument | Description              | Défaut |
    |----------|:------------------------:|--------|
    | --source |Chemin (relatif ou absolu)<br>
                vers le dossier de logs (Obligatoire)| N/A |
    | --dest   |Chemin vers le dossier de destination<br>
                des archives |N/A |
    | --niveau |Niveau de filtrage:ALL,ERROR<br>
                WARN,INFO | ALL |
    |--retention|Nombre de jours avant<br>
                suppresion des anciens archives| 30|
---
## **4.Description des modules**
    - main.py: Point d'entrée qui orchestre l'appel des modules et gère les arguments CLI
    - analyser.py: Scanne les fichiers .log,filtre les entrées, et calcul les statistiques..
        (Top 5 des erreurs, Nombre de lignes analysées...)
    - rapport.py:Génère un rapport JSON structuré contenant les métadonnées et les statistiques.
    -archiver.py: Compresse les logs traités en.tar.gz et néttoie les rapports obsolètes
***
## **5.Planification CRON**
    Pour exécuter l'analyse tous les dimanches à 03H00 du matin, ajouter la ligne suivante à votre crontab..
    ```
        0 3 * * 0 /usr/bin/python3 /chemin/absolu/vers/loganalyser/main.py --source /chemin/vers/logs --dest /chemin/vers/backup
    ```