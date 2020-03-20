# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_rtd_theme

from datetime import datetime

# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath(".."))

# read from file
with open("../version.txt", "r") as filein:
    version = filein.read()

# -- Project information -----------------------------------------------------
project = 'argo-models'
copyright = f'{datetime.now().year}, eterna2 <eterna2@hotmail.com>'
author = 'eterna2 <eterna2@hotmail.com>'


# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["autoapi.extension", "m2r", "sphinx_rtd_theme"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['**/*_test.py']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# location of source code for autoapi
autoapi_type = "python"
autoapi_dirs = ["../argo"]
autoapi_options = ["members", "undoc-members"]
autoapi_generate_api_docs = True
autoapi_add_toctree_entry = True
autoapi_include_summaries = True
autoapi_keep_files = False
autoapi_ignore = ["*_test.py"]
autoapi_python_class_content = "both"

# for m2r extension
source_suffix = [".rst", ".md"]