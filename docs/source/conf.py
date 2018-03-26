# -*- coding: utf-8 -*-
DESCRIPTION = (
    'pyecharts map extension - china counties - python package' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'echarts-china-counties-pypkg'
copyright = u'2018 pyecharts dev team'
version = '0.0.0'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'echarts-china-counties-pypkgdoc'
latex_elements = {}
latex_documents = [
    ('index', 'echarts-china-counties-pypkg.tex',
     'echarts-china-counties-pypkg Documentation',
     'pyecharts dev team', 'manual'),
]
man_pages = [
    ('index', 'echarts-china-counties-pypkg',
     'echarts-china-counties-pypkg Documentation',
     [u'pyecharts dev team'], 1)
]
texinfo_documents = [
    ('index', 'echarts-china-counties-pypkg',
     'echarts-china-counties-pypkg Documentation',
     'pyecharts dev team', 'echarts-china-counties-pypkg',
     DESCRIPTION,
     'Miscellaneous'),
]
