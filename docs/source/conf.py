# -*- coding: utf-8 -*-

# pythonUtility build configuration file

# -- Project information -----------------------------------------------------
# 

project = 'pythonUtility'
copyright = '2024, Lizzie'
author = 'Lizzie'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# -- pythonUtility Path configuration-------------------------------------------------------------
import sys
from pathlib import Path

def _fix_path():
    """Find the root of pythonUtility. """
    p = Path(__file__).resolve().parents[2]
    sys.path.insert(0, p.abspath('extensions'))

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
]


#master_doc = 'index.rst'
templates_path = ['_templates']
# add_function_parentheses = True
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']
