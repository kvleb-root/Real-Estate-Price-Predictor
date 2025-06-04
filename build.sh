#!/usr/bin/env bash
# exit on error
set -o errexit

# Installation des dépendances
pip install -r requirements.txt

# Collecte des fichiers statiques
python manage.py collectstatic --no-input

# Migrations de la base de données
python manage.py migrate 