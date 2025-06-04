# Guide d'Utilisation - Prédicteur de Prix Immobilier

## Table des matières
1. [Introduction](#introduction)
2. [Accès à l'application](#accès-à-lapplication)
3. [Utilisation du formulaire](#utilisation-du-formulaire)
4. [Comprendre les résultats](#comprendre-les-résultats)
5. [FAQ](#faq)
6. [Dépannage](#dépannage)

## Introduction

Bienvenue dans le guide d'utilisation du Prédicteur de Prix Immobilier. Cette application vous permet d'obtenir une estimation rapide et précise du prix d'un bien immobilier en fonction de ses caractéristiques. Le modèle utilisé a été entraîné sur un large jeu de données immobilières provenant de Kaggle.

## Accès à l'application

1. Ouvrez votre navigateur web préféré (Chrome, Firefox, Safari, etc.)
2. Accédez à l'URL : `http://localhost:8000`
3. Vous devriez voir une interface moderne avec un formulaire de saisie

## Utilisation du formulaire

### Champs obligatoires

Tous les champs du formulaire sont obligatoires. Voici comment les remplir correctement :

1. **Surface (area)**
   - Entrez la surface habitable en mètres carrés
   - Utilisez uniquement des nombres entiers
   - Exemple : 120

2. **Nombre de chambres**
   - Indiquez le nombre total de chambres
   - Minimum : 1
   - Exemple : 3

3. **Nombre de salles de bain**
   - Indiquez le nombre de salles de bain
   - Peut inclure les salles d'eau
   - Exemple : 2

4. **Nombre d'étages**
   - Indiquez le nombre total d'étages
   - Pour un plain-pied, mettez 1
   - Exemple : 2

5. **Route principale**
   - Sélectionnez "Oui" si le bien est situé sur une route principale
   - Sélectionnez "Non" dans le cas contraire

6. **Chambre d'amis**
   - Sélectionnez "Oui" si une chambre d'amis dédiée est présente
   - Sélectionnez "Non" dans le cas contraire

7. **Sous-sol**
   - Sélectionnez "Oui" si le bien possède un sous-sol
   - Sélectionnez "Non" dans le cas contraire

8. **Chauffage eau chaude**
   - Sélectionnez "Oui" pour un système de chauffage d'eau centralisé
   - Sélectionnez "Non" pour des systèmes individuels

9. **Climatisation**
   - Sélectionnez "Oui" si le bien est équipé de la climatisation
   - Sélectionnez "Non" dans le cas contraire

10. **Places de parking**
    - Indiquez le nombre de places de parking disponibles
    - Minimum : 0
    - Exemple : 2

11. **Zone préférentielle**
    - Sélectionnez "Oui" si le bien est dans un quartier recherché
    - Sélectionnez "Non" dans le cas contraire

12. **État du mobilier**
    - "Non meublé" : Aucun meuble inclus
    - "Semi-meublé" : Quelques meubles essentiels inclus
    - "Meublé" : Entièrement meublé

### Soumission du formulaire

1. Vérifiez que tous les champs sont remplis
2. Cliquez sur le bouton "Prédire le prix"
3. Attendez quelques secondes pour le calcul

## Comprendre les résultats

Après la soumission du formulaire, vous verrez :

- Le prix estimé en euros
- Le résultat s'affiche dans un cadre bien visible
- Le prix tient compte de toutes les caractéristiques saisies

## FAQ

**Q : Les prédictions sont-elles précises ?**
R : Les prédictions sont basées sur un modèle entraîné avec des données réelles, mais doivent être considérées comme des estimations.

**Q : Puis-je modifier mes données après une prédiction ?**
R : Oui, vous pouvez modifier n'importe quel champ et soumettre à nouveau le formulaire.

**Q : Les données sont-elles sauvegardées ?**
R : Non, les données ne sont pas stockées et sont uniquement utilisées pour la prédiction.

## Dépannage

### Problèmes courants

1. **Le formulaire ne se soumet pas**
   - Vérifiez que tous les champs sont remplis
   - Assurez-vous d'utiliser des nombres valides

2. **La page ne charge pas**
   - Vérifiez votre connexion internet
   - Assurez-vous que le serveur est en cours d'exécution

3. **Erreur dans la prédiction**
   - Vérifiez que les valeurs entrées sont réalistes
   - Rafraîchissez la page et réessayez

### Contact support

Pour toute question ou problème technique, n'hésitez pas à :
- Ouvrir une issue sur le repository GitHub
- Contacter l'équipe de support

---

*Note : Ce guide est susceptible d'être mis à jour. Consultez régulièrement la dernière version disponible.* 