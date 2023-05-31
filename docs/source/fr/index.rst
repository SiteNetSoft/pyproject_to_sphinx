PyProject to Sphinx
=============================

Pourquoi copier-coller les détails de votre projet dans votre documentation Sphinx lorsque vous pouvez simplement utiliser les informations déjà présentes dans votre fichier pyproject.toml ?

Problèmes de duplication d'information :

* Vous devez vous rappeler de mettre à jour votre documentation Sphinx lorsque vous modifiez les détails de votre projet, et vice versa
* Erreur humaine lors de la copie et du collage d'informations entre les deux fichiers
* Il est chronophage de mettre à jour les deux fichiers

C'est pourquoi ce projet très simple existe. Il analyse votre fichier `pyproject.toml` et peuple les variables de votre fichier `conf.py` [Sphinx](http://sphinx-doc.org/).

Pourquoi la documentation est-elle également en français ?
----------------------------------------

Notre 127.0.0.1 est au Québec, Canada, c'est pour cette raison que nous devons fournir notre documentation en français.

Installation
------------

Vous pouvez installer ce paquet à l'aide de pip :

.. code-block:: bash

    pip install pyproject_to_sphinx

Ou via poetry :

.. code-block:: bash

    poetry add pyproject_to_sphinx

Rien de trop compliqué.

Usage
-----

L'utilisation est très simple. Vous avez juste besoin d'ajouter les lignes suivantes à votre fichier `conf.py` :

.. literalinclude:: ../global/code_example.py
   :language: python
   :linenos:
