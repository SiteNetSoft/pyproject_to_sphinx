PyProject to Sphinx Parser
=============================

Why copy paste your project's details into your Sphinx documentation when you can just use the information that is already in your project `pyproject.toml` file?

Duplication of information problems:

* You have to remember to update your Sphinx documentation when you change your project's details and vice versa
* Human error when copying and pasting information between the two
* Time consuming to update both

This is why this very simple project exists. It parses your `pyproject.toml` file and populates the variables in your `Sphinx <http://sphinx-doc.org/>`__ `conf.py` file.

Why is the documentation also in French?
----------------------------------------

Our 127.0.0.1 is in Québec, Canada for this reason we have to provide our documentation in French.

Installation
------------

You can install this package using pip:

.. code-block:: bash

    pip install pyproject_to_sphinx

Or via poetry:

.. code-block:: bash

    poetry add pyproject_to_sphinx

Nothing to complicated.

Usage
-----

The usage is very simple. You just need to add the following lines to your `conf.py` file:

.. literalinclude:: ../global/code_example.py
   :language: python
   :linenos:
