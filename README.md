## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/tristan-mn/OPC_DA_P13_ORANGE_COUNTY_LETTINGS_DEVOPS.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin/`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

Nécessite :
- Compte CircleCi
- Compte Docker
- Compte Heroku
- Compte Sentry

Le déploiement est géré par le fichier config.yml présent dans le dossier ./.circleci. Ce dernier est provoqué lors d'un push du code vers le repository GitHub.
Un push sur la branche main déclenchera les tests pytest ainsi que les tests flake8. Par la suite, l'application est conteneurisée avec Docker et pour finir 
elle est déployée en ligne grâce à Heroku.

URL de l'application en ligne : https://lettings-2f52c82babb6.herokuapp.com/

Dans le cas d'un push sur une branche autre que "main", seuls les tests pytest et flake8 seront réalisés.

Dans le dépôt CircleCi renseigner les variables d'environnement :
- `SECRET_KEY` = Clé secrète de l'application Django
- `DOCKER_USER` = Votre identifiant DOCKERHUB
- `DOCKER_PASS` = Votre mot de passe DOCKERHUB
- `HEROKU_API_KEY` = Clé de l'application HEROKU
- `HEROKU_APP_NAME` = Nom de l'application HEROKU

Dans le fichier config.yml remplacer:
- `tristanmn/opc-p13-lettings` par le nom de votre dépôt DockerHub

Dans le fichier .env renseigner :
- `SECRET_KEY`
- `ALLOWED_HOST`
- `DEBUG` = 0 pour False, 1 pour True
- `SENTRY_KEY` pour l'utilisation de l'application SENTRY

L'URL suivante : `https://oc-lettings-2022.herokuapp.com/sentry-debug/` soulève une exception pour tester le bon fonctionnement du suivi de problèmes sur Sentry
