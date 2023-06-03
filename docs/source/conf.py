# Configuration file for the Sphinx documentation builder.

# -- Project information

from pyproject_to_sphinx.pyproject_parser import PyProjectParser

pyproject_parser = PyProjectParser()

# -- Set project information for Sphinx --
project = pyproject_parser.metadata["name"]
author = pyproject_parser.authors
release = pyproject_parser.release
version = pyproject_parser.version

language = 'en'
languages = ['en', 'fr']

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
