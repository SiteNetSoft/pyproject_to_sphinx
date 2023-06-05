PyProject to Sphinx Parser
=============================

Why copy paste your project's details into your Sphinx documentation when you can just use the information that is already in your project `pyproject.toml` file?

Duplication of information problems:

* You have to remember to update your Sphinx documentation when you change your project's details and vice versa
* Human error when copying and pasting information between the two
* Time consuming to update both

This is why this very simple project exists. It parses your `pyproject.toml` file and populates the variables in your `Sphinx <http://sphinx-doc.org/>`__ `conf.py` file.

.. note::

    The copyright information is taken from the LICENSE file of your project.

    If it is not found there it will be taken from the `pyproject.toml` file license type name.

    Not all license types have been tested for.

.. note::

    **Why is the documentation also in French?**

    Our 127.0.0.1 is in Québec, Canada for this reason we have to provide our documentation in French.

Version vs Release
------------------

* **version:** This is a shorter, "quick reference" version of your project,
  which usually omits smaller point-level details. For example, if your project's full version is '1.3.4',
  the version might just be '1.3'.
* **release:** This is the full version string of your project, including alpha/beta/rc tags.
  Continuing the previous example, the release would be '1.3.4'.

In the `pyproject.toml` file, the `[tool.poetry]` section only has a version field,
which corresponds to the full version of your project, similar to the release field in Sphinx's `conf.py`.
The version in `pyproject.toml` typically follows the format of `MAJOR.MINOR.PATCH`, for example '1.3.4',
and can also include identifiers for pre-release and build metadata.

For more information about `Sphinx versioning <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-version>`__.

Installation
------------

You can install this package using pip:

.. code-block:: bash

    pip install pyproject_to_sphinx

Or via poetry:

.. code-block:: bash

    poetry add pyproject_to_sphinx

.. tip::

    When you install with Poetry it might just hang there so you might need to use this environment variable:

    .. code-block:: bash

        export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring

.. tip::

    If you are having issues (`ModuleNotFoundError: No module named 'toml'`) with the installation you can try to force reinstall the toml package:

    ``pip install --upgrade --force-reinstall toml``

    If it still does not work make sure you are using the right version of python (``python --version``) it should be 3.10 or higher.

Nothing to complicated.

Usage
-----

The usage is very simple. You just need to add the following lines to your `conf.py` file:

.. literalinclude:: ../global/code_example.py
   :language: python
   :linenos:
