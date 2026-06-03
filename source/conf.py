import os
import sys

project = "Prévision de la Demande d'Électricité - Maroc 2030"
copyright = '2026, Younes Chajara & Achraf Oudich'
author = 'Younes Chajara & Achraf Oudich'
release = 'latest'

# Extension pour lire le fichier README.md en Markdown
extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'
html_theme = 'sphinx_rtd_theme'
source_encoding = 'utf-8-sig'