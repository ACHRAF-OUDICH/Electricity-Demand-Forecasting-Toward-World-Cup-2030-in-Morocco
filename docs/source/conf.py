import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = "Prévision de la Demande d'Électricité - Maroc 2030"
copyright = '2026, Younes Chajara & Achraf Oudich'
author = 'Younes Chajara & Achraf Oudich'
release = 'latest'

# L'extension 'myst_parser' permet à Sphinx de compiler le Markdown (.md)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Forcer la lecture des fichiers source en UTF-8 pour éviter les '?' à la place des accents
source_encoding = 'utf-8-sig'