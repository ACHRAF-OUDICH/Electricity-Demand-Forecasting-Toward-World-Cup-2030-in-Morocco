import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = "Prediction de la Demande d'Electricite - Maroc 2030"
copyright = '2026, Younes Chajara & Achraf Oudich'
author = 'Younes Chajara & Achraf Oudich'
release = 'latest'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []

# Forcer la langue en français pour s'aligner avec les paramètres du build
language = 'fr'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
