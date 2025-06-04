# 🏠 Prédiction de Prix Immobilier

Ce projet est une application web Django qui permet de prédire le prix d'un bien immobilier en fonction de ses caractéristiques. Le modèle de prédiction a été entraîné sur Kaggle avec un jeu de données immobilières.

## 🚀 Fonctionnalités

- Interface utilisateur moderne et responsive avec Tailwind CSS
- Formulaire intuitif pour saisir les caractéristiques du bien
- Animations et effets visuels pour une meilleure expérience utilisateur
- Prédiction en temps réel du prix estimé
- Design avec effet de verre (glassmorphism)

## 🛠️ Technologies Utilisées

- **Backend**: Django (Python)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Machine Learning**: Modèle entraîné sur Kaggle
- **Design**: Glassmorphism, Animations CSS

## 📋 Caractéristiques Prises en Compte

- Surface habitable
- Nombre de chambres
- Nombre de salles de bain
- Nombre d'étages
- Présence d'une route principale
- Présence d'une chambre d'amis
- Présence d'un sous-sol
- Système de chauffage d'eau
- Climatisation
- Places de parking
- Zone préférentielle
- État du mobilier

## 🚀 Installation

1. Clonez le repository :
```bash
git clone [votre-repo]
cd site_de_prediction
```

2. Créez un environnement virtuel et activez-le :
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Effectuez les migrations :
```bash
python manage.py migrate
```

5. Lancez le serveur :
```bash
python manage.py runserver
```

## 🎯 Utilisation

1. Accédez à l'application via `http://localhost:8000`
2. Remplissez le formulaire avec les caractéristiques du bien
3. Cliquez sur "Prédire le prix"
4. Le prix estimé s'affichera instantanément

## 🧠 Modèle de Machine Learning

Le modèle de prédiction a été entraîné sur Kaggle en utilisant un jeu de données immobilières. L'entraînement a pris en compte de nombreuses caractéristiques pour fournir des estimations précises des prix immobiliers.

Dataset utilisé : [Housing Prices Dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)

## 📝 Note

Ce projet est à des fins de démonstration et d'apprentissage. Les prédictions sont basées sur un modèle entraîné et peuvent ne pas refléter exactement les prix du marché réel.

## 👥 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 