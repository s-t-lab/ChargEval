#!/usr/bin/env python3
# -*- coding: utf-8 -*-\
import sys,os

pardir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(pardir)
sys.path.append(pardir)

from sphinx_materialdesign_theme  import __version__

source_suffix = '.rst'
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode', 
    'sphinx.figtable', 
    'sphinx.numfig'
    ]

mathjax_path="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# mathjax_config = {
#     'extensions': ['tex2jax.js'],
#     'jax': ['input/TeX', 'output/SVG'],
# }

version = __version__
release = __version__


project = 'EVI_DSS'
copyright = '2019, Chintan Pathak, Don MacKenzie'
author = 'Chintan Pathak, Don MacKenzie'

language = 'en'

templates_path = ['_templates']
html_sidebars = {
   '**': ['globaltoc.html']
}
html_favicon = '_static/favicon.ico'
html_logo = '_static/logo2.png'

html_theme = 'sphinx_materialdesign_theme'
html_theme_path = ['../']

html_theme_options = {
    # Specify a list of menu in Header.
    # Tuples forms:
    #  ('Name', 'external url or path of pages in the document', boolean, 'icon name')
    #
    # Third argument:
    # True indicates an external link.
    # False indicates path of pages in the document.
    #
    # Fourth argument:
    # Specify the icon name.
    # For details see link.
    # https://material.io/icons/
    'header_links' : [
       ('Home', 'index', False, 'home'),
       ("GitHub", " https://github.com/chintanp/wsdot_evse_docs", True, 'link')
    ],

    # Customize css colors.
    # For details see link.
    # https://getmdl.io/customize/index.html
    #
    # Values: amber, blue, brown, cyan deep_orange, deep_purple, green, grey, indigo, light_blue,
    #         light_green, lime, orange, pink, purple, red, teal, yellow(Default: indigo)
    'primary_color': 'indigo',
    # Values: Same as primary_color. (Default: pink)
    'accent_color': 'pink',

    # Customize layout.
    # For details see link.
    # https://getmdl.io/components/index.html#layout-section
    'fixed_drawer': True,
    'fixed_header': True,
    'header_waterfall': True,
    'header_scroll': False,

    # Render title in header.
    # Values: True, False (Default: False)
    'show_header_title': False,
    # Render title in drawer.
    # Values: True, False (Default: True)
    'show_drawer_title': True,
    # Render footer.
    # Values: True, False (Default: True)
    'show_footer': True
}

html_show_sourcelink = True

rst_prolog= u"""
    .. |project| replace:: Sphinx Material Design Theme
"""
numfig = True