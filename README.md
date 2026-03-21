# LogAnalyzer — Pipeline d'Analyse et d'Archivage

## 1. Description du projet

LogAnalyzer Pro est un outil en ligne de commande (CLI) conçu pour automatiser la supervision des logs applicatifs dans un environnement DevOps. Il permet d'analyser des fichiers de logs, de générer des rapports statistiques et d'archiver les données traitées.

---

## 2. Prérequis et installation

- **Version Python** : Python 3.x
- **Dépendances** : Aucune bibliothèque externe n'est nécessaire
- **Installation** : Clonez le dépôt et assurez-vous que les scripts ont les droits d'exécution

---

## 3. Utilisation

Le script principal `main.py` accepte les arguments suivants :
```bash
python3 main.py --source ./logs_test --dest ./backups --niveau ERROR --retention 15
```

| Argument      | Description                                              | Défaut |
|---------------|----------------------------------------------------------|--------|
| `--source`    | Chemin (relatif ou absolu) vers le dossier de logs *(Obligatoire)* | N/A |
| `--dest`      | Chemin vers le dossier de destination des archives       | N/A    |
| `--niveau`    | Niveau de filtrage : `ALL`, `ERROR`, `WARN`, `INFO`      | `ALL`  |
| `--retention` | Nombre de jours avant suppression des anciennes archives | `30`   |

---

## 4. Description des modules

| Module          | Rôle |
|-----------------|------|
| `main.py`       | Point d'entrée : orchestre l'appel des modules et gère les arguments CLI |
| `analyser.py`   | Scanne les fichiers `.log`, filtre les entrées et calcule les statistiques (top 5 des erreurs, nombre de lignes analysées…) |
| `rapport.py`    | Génère un rapport JSON structuré contenant les métadonnées et les statistiques |
| `archiver.py`   | Compresse les logs traités en `.tar.gz` et nettoie les rapports obsolètes |

---

## 5. Planification CRON

Pour exécuter l'analyse automatiquement tous les dimanches à 03h00, ajoutez la ligne suivante à votre crontab :
```bash
0 3 * * 0 /usr/bin/python3 /chemin/absolu/vers/loganalyser/main.py \
  --source /chemin/vers/logs \
  --dest /chemin/vers/backup
```
---

## 6. Repartition des Tâches
| Membres             | Tâches
|---------------------|----------------------------------------------------------|
|`DAMASSOH Denise`    | Module 3: Archivage et Nettoyage                         |
| `LEWHE Abel`        | Module 4: Point d'entrée et Orchestration                |
|`OSSENI Rosmiyiath`  | Module 2: Génération du rapport JSON                     |
|`MOLOKE Maëlys`      | Module 1 : Ingestion et Analyse                          |

