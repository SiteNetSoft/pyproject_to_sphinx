PyProject to Sphinx
=============================

Pourquoi copier-coller les détails de votre projet dans votre documentation Sphinx lorsque vous pouvez simplement utiliser les informations déjà présentes dans votre fichier `pyproject.toml` ?

Problèmes de duplication d'information :

* Vous devez vous rappeler de mettre à jour votre documentation Sphinx lorsque vous modifiez les détails de votre projet, et vice versa
* Erreur humaine lors de la copie et du collage d'informations entre les deux fichiers
* Il est chronophage de mettre à jour les deux fichiers

C'est pourquoi ce projet très simple existe. Il analyse votre fichier `pyproject.toml` et peuple les variables de votre fichier `conf.py` `Sphinx <http://sphinx-doc.org/fr/master/>`__.

.. note::

    Les informations sur les droits d'auteur sont extraites du fichier LICENSE de votre projet.

    Si elles ne sont pas trouvées là, elles seront extraites du nom du type de licence dans le fichier pyproject.toml.

    Tous les types de licences n'ont pas été testés.

.. note::

    **Pourquoi la documentation est-elle également en français ?**

    Notre 127.0.0.1 est au Québec, Canada, c'est pour cette raison que nous devons fournir notre documentation en français.

Version vs. Versioning
----------------------

* **version:** Il s'agit d'une version plus courte, une "référence rapide" de votre projet, qui omet généralement des détails de niveau de point plus petits. Par exemple, si la version complète de votre projet est '1.3.4', la version pourrait être juste '1.3'.
* **release:** Il s'agit de la chaîne de version complète de votre projet, y compris les tags alpha/beta/rc. Poursuivant l'exemple précédent, la publication serait '1.3.4'.

Dans le fichier `pyproject.toml`, la section `[tool.poetry]` n'a qu'un champ de version,
qui correspond à la version complète de votre projet, similaire au champ de release dans `conf.py` de Sphinx.
La version dans `pyproject.toml` suit généralement le format `MAJOR.MINOR.PATCH`, par exemple '1.3.4',
et peut également inclure des identifiants pour la préversion et des métadonnées de build.

Pour plus d'informations sur la `version de Sphinx <https://www.sphinx-doc.org/fr/master/usage/configuration.html#confval-version>`__.

Installation
------------

Vous pouvez installer ce paquet à l'aide de pip :

.. code-block:: bash

    pip install pyproject_to_sphinx

Ou via poetry :

.. code-block:: bash

    poetry add pyproject_to_sphinx

.. tip::

    Lorsque vous installez avec Poetry, il se peut qu'il reste bloqué à cet endroit, vous devrez donc utiliser cette variable d'environnement :

    .. code-block:: bash

        export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring

Rien de trop compliqué.

Usage
-----

L'utilisation est très simple. Vous avez juste besoin d'ajouter les lignes suivantes à votre fichier `conf.py` :

.. literalinclude:: ../global/code_example.py
   :language: python
   :linenos:
