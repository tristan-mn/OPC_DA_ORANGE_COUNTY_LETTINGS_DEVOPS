.. ocr-p13-lettings documentation master file, created by
   sphinx-quickstart on Mon Aug 21 13:05:24 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ocr-p13-lettings's documentation!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Guide de Développement Local pour Orange County Lettings
========================================================

.. contents:: Table des matières

Résumé
======

Ce guide explique le processus de configuration et de développement local du site web Orange County Lettings.

Développement local
===================

Prérequis
---------

- Compte GitHub avec accès en lecture à ce dépôt
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

.. note::
   Dans la suite de la documentation sur le développement local, nous supposerons que la commande ``python`` de votre shell OS exécute l'interpréteur Python susmentionné, à moins qu'un environnement virtuel ne soit activé.

macOS / Linux
--------------

Cloner le dépôt
~~~~~~~~~~~~~~~

.. code-block:: shell

   cd /chemin/vers/projet/
   git clone https://github.com/tristan-mn/OPC_DA_P13_ORANGE_COUNTY_LETTINGS_DEVOPS.git

Créer l'environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   cd /chemin/vers/Python-OC-Lettings-FR
   python -m venv venv
   apt-get install python3-venv (Si des erreurs surviennent avec un paquet non trouvé sur Ubuntu)

Activer l'environnement
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   source venv/bin/activate

Confirmer les versions de Python et Pip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   which python
   python --version
   which pip

Désactiver l'environnement
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   deactivate

Exécuter le site
~~~~~~~~~~~~~~~~~

.. code-block:: shell

   cd /chemin/vers/Python-OC-Lettings-FR
   source venv/bin/activate
   pip install --requirement requirements.txt
   python manage.py runserver

- Ouvrez http://localhost:8000 dans un navigateur pour vérifier que le site fonctionne correctement.

Linting
-------

- Exécutez le linter flake8 :

.. code-block:: shell

   cd /chemin/vers/Python-OC-Lettings-FR
   source venv/bin/activate
   flake8

Tests unitaires
---------------

- Exécutez les tests unitaires avec pytest :

.. code-block:: shell

   cd /chemin/vers/Python-OC-Lettings-FR
   source venv/bin/activate
   pytest

Base de données
---------------

- Ouvrez une session shell SQLite3 :

.. code-block:: shell

   cd /chemin/vers/Python-OC-Lettings-FR
   sqlite3

- Connectez-vous à la base de données :

.. code-block:: sql

   .open oc-lettings-site.sqlite3

- Affichez les tables dans la base de données :

.. code-block:: sql

   .tables

- Affichez les colonnes dans le tableau des profils :

.. code-block:: sql

   pragma table_info(Python-OC-Lettings-FR_profile);

- Exécutez une requête sur la table des profils (exemple avec un filtre sur la ville) :

.. code-block:: sql

   select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';

- Pour quitter la session SQLite3 :

.. code-block:: sql

   .quit

Panel d'administration
----------------------

- Accédez au panel d'administration en ouvrant http://localhost:8000/admin dans un navigateur.
- Connectez-vous avec l'utilisateur admin et le mot de passe Abc1234!

Windows
-------

L'utilisation de PowerShell est similaire à ce qui a été décrit précédemment, avec quelques différences :

- Pour activer l'environnement virtuel :

.. code-block:: shell

   .\venv\Scripts\Activate.ps1

- Remplacez ``which <ma-commande>`` par ``(Get-Command <ma-commande>).Path``

Déploiement
===========

Le déploiement nécessite :

- Compte CircleCi
- Compte Docker
- Compte Heroku
- Compte Sentry

Le déploiement est géré par le fichier ``config.yml`` présent dans le dossier ``./.circleci``.  
Ce fichier est déclenché lors d'un push vers le dépôt GitHub. Un push sur la branche ``main`` déclenche les tests pytest et flake8.  
Ensuite, l'application est conteneurisée avec Docker et déployée en ligne via Heroku.  

URL de l'application en ligne : https://lettings-2f52c82babb6.herokuapp.com/

Pour les pushes sur des branches autres que "main", seuls les tests pytest et flake8 sont réalisés.

Dans le dépôt CircleCi, configurez les variables d'environnement :

- ``SECRET_KEY`` : Clé secrète de l'application Django
- ``DOCKER_USER`` : Votre identifiant DOCKERHUB
- ``DOCKER_PASS`` : Votre mot de passe DOCKERHUB
- ``HEROKU_API_KEY`` : Clé de l'application HEROKU
- ``HEROKU_APP_NAME`` : Nom de l'application HEROKU
- ``SENTRY_KEY`` pour l'utilisation de l'application SENTRY

Dans le fichier ``config.yml``, remplacez :

- ``tristanmn/opc-p13-lettings`` par le nom de votre dépôt DockerHub

Dans le fichier ``.env``, renseignez :

- ``SECRET_KEY``
- ``ALLOWED_HOST``
- ``DEBUG`` : 0 pour False, 1 pour True
- ``SENTRY_KEY`` pour l'utilisation de l'application SENTRY

L'URL suivante : https://lettings-2f52c82babb6.herokuapp.com/rezgrzgegter/ génère une exception pour tester le suivi des problèmes sur Sentry.
