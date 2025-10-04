
# Projet AWS CDK Free Tier - Bucket S3

## Version française

Ce projet s’inscrit dans une démarche d’apprentissage pratique pour la certification AWS Developer Associate.  
Il montre comment utiliser AWS CDK (Python) pour déployer un bucket S3 simple, sécurisé et conforme aux bonnes pratiques AWS, tout en restant dans les limites du Free Tier.

### Objectif
L’objectif est de créer une infrastructure minimale mais conforme aux standards de sécurité AWS :
- Versioning activé pour la restauration des données
- Chiffrement côté serveur (SSE-S3 / AES-256)
- Blocage complet de l’accès public
- SSL obligatoire (HTTPS uniquement)
- Conservation du bucket lors de la suppression de la stack pour éviter toute perte accidentelle

### Prérequis
- Python 3.x  
- AWS CDK v2  
- AWS CLI configurée avec un utilisateur IAM à privilèges restreints (`cdk-deployer`)

### Installation et déploiement
```bash
# Créer et activer l’environnement virtuel
python3 -m venv .env
source .env/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Synthétiser et déployer la stack
cdk synth
cdk deploy --profile cdk-deployer

# AWS CDK Free Tier Project - S3 Bucket

