import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'Prediction de la Demande d\\'Electricite - Objectif Coupe du Monde 2030'
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

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
