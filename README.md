# Ransomware-Sim

Ransomware-Sim est une application de simulation qui illustre le fonctionnement d’une attaque de type ransomware dans un environnement virtualisé. Ce projet est réalisé dans le cadre du TIPE des classes préparatoires. 

Le thème pour l’année 2020-2021 du TIPE commun aux filières est intitulé : enjeux sociétaux. 
Ce thème pourra être décliné sur les champs suivants : environnement, sécurité, énergie. J’ai décidé de prendre le thème de la sécurité pour mon projet, en particulier la cybersécurité.

## Fonctionnement de la simulation
Le projet se compose de trois scripts principaux :

1. **crypteur.py** :
   - Localise les fichiers présents sur le bureau de la victime.
   - Génère une clé de chiffrement aléatoire.
   - Crypte les fichiers à l'aide de la clé générée.
   - Envoie la clé au serveur via une connexion TCP.

2. **decrypteur.py** :
   - Décrypte les fichiers préalablement chiffrés à l'aide de la clé secrète saisie par l’utilisateur.

3. **server.py** :
   - Reçoit et stocke les clés de chiffrement transmises par les victimes.
   - Enregistre les informations dans un fichier texte `victime.txt`.

## Scénario de l’attaque dans un environnement virtualisé
1. **Machine virtuelle de la victime (VM1)** :
   - Le script `crypteur.py` est exécuté. Ce script localise les fichiers sur le bureau de l'utilisateur et les chiffre.
   - La clé de chiffrement est envoyée à la seconde machine virtuelle (VM2), qui agit comme serveur de commande et de contrôle (C&C).

2. **Machine virtuelle du serveur (VM2)** :
   - Le script `server.py` écoute les connexions entrantes et enregistre les informations des victimes, y compris leurs clés de chiffrement.

3. **Récupération des fichiers** :
   - Pour décrypter les fichiers, l'utilisateur exécute `decrypteur.py` sur VM1 et fournit la clé de chiffrement obtenue via le serveur (VM2).

## Prérequis
- Deux machines virtuelles configurées sur le même réseau local.
  - VM1 : Machine victime avec les fichiers à chiffrer.
  - VM2 : Serveur pour collecter les clés.
- Python 3.6 ou version ultérieure installé.

## Instructions
### 1. Configurer le serveur (VM2)
- Lancez le script `server.py` sur VM2 pour qu'il commence à écouter les connexions :
  ```bash
  python server.py
  ```

### 2. Exécuter le ransomware (VM1)
- Lancez le script `crypteur.py` sur VM1 pour localiser et chiffrer les fichiers :
  ```bash
  python crypteur.py
  ```

### 3. Récupérer les fichiers (VM1)
- Obtenez la clé de chiffrement depuis `victime.txt` sur VM2.
- Exécutez le script `decrypteur.py` sur VM1 et fournissez la clé :
  ```bash
  python decrypteur.py
  ```

