import sphinx_rtd_theme
from sphinx.util.docfields import TypedField
import os
from gnutools.utils import listfiles, replace_dir
# from autosphinx import patched_make_field, generate_rst, get_packages
from autosphinx import AutoSphinx
from gnutools.utils import parent
import time
# os.environ["ASPHINX_LIBROOT"] = "/media/jcadic/IYOProjects/IYO/iyo-python/iyo"
# os.environ["ASPHINX_NAMELIB"] = "iyo"
# os.environ["ASPHINX_VERSION"] = "1.0a28"
CURRENT_DIR = parent(os.path.abspath(__file__))
ASPHINX_NAMELIB = os.environ["ASPHINX_NAMELIB"]
ASPHINX_VERSION = os.environ["ASPHINX_VERSION"]
ASPHINX_LIBROOT = os.environ["ASPHINX_LIBROOT"]

if not os.environ["ASPHINX_LOGO"]=="":
    ASPHINX_LOGO = os.environ["ASPHINX_LOGO"].split("/")[-1]
    replace_dir("{current_dir}/img".format(current_dir=CURRENT_DIR))
    os.system("cp {img} {current_dir}/img".format(current_dir=CURRENT_DIR,
                                                  img= os.environ["ASPHINX_LOGO"]))
    # print(os.environ["ASPHINX_LOGO"],  "{current_dir}/img".format(current_dir=CURRENT_DIR))
    # time.sleep(10)

sphinx = AutoSphinx(lib_root=os.environ["ASPHINX_LIBROOT"],
                    version=os.environ["ASPHINX_VERSION"])
TypedField.make_field = sphinx.patched_make_field

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
]

napoleon_use_ivar = True
googleanalytics_enabled = False
add_module_names = False
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = ASPHINX_NAMELIB
copyright = '2019, {ASPHINX_NAMELIB} Contributors'.format(ASPHINX_NAMELIB=ASPHINX_NAMELIB)
author = '{ASPHINX_NAMELIB} Contributors'.format(ASPHINX_NAMELIB=ASPHINX_NAMELIB)

# The ASPHINX_VERSION info for the project you're documenting, acts as replacement for
# |ASPHINX_VERSION| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y ASPHINX_VERSION.
# TODO: change to [:2] at v1.0
ASPHINX_VERSION = ASPHINX_VERSION
# The full ASPHINX_VERSION, including alpha/beta/rc tags.
# TODO: verify this works as expected
release = ASPHINX_VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'logo_only': True,
}

html_logo = "img/{ASPHINX_LOGO}".format(ASPHINX_LOGO=ASPHINX_LOGO)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_style_path = 'css/pytorch_theme.css'
html_context = {
    'css_files': [
        'https://fonts.googleapis.com/css?family=Lato',
        '_static/css/pytorch_theme.css'
    ],
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = '{ASPHINX_NAMELIB}Doc'.format(ASPHINX_NAMELIB=ASPHINX_NAMELIB)


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pytorch.tex', '{ASPHINX_NAMELIB} Documentation'.format(ASPHINX_NAMELIB=ASPHINX_NAMELIB),
     'Torch Contributors', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, ASPHINX_NAMELIB, '{ASPHINX_NAMELIB} Documentation'.format(ASPHINX_NAMELIB=ASPHINX_NAMELIB),
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, '{ASPHINX_NAMELIB}'.format(ASPHINX_NAMELIB=ASPHINX_NAMELIB), '{ASPHINX_NAMELIB} Documentation'.format(ASPHINX_NAMELIB=ASPHINX_NAMELIB),
     author, ASPHINX_NAMELIB, 'One line description of project.',
     'Miscellaneous'),
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
}

# -- A patch that prevents Sphinx from cross-referencing ivar tags -------
# See http://stackoverflow.com/a/41184353/3343043

html_show_sourcelink = False

# ------------------ Generate the rst files ----------------------------


[os.system("rm {}".format(file)) for file in listfiles(root=CURRENT_DIR, patterns=[".rst"])]
pkgs = [pkg.replace("{ASPHINX_NAMELIB}.".format(ASPHINX_NAMELIB=ASPHINX_NAMELIB), "") for pkg in sphinx.get_packages(root=ASPHINX_LIBROOT, namelib=ASPHINX_NAMELIB)]
for pkg in [pkg for pkg in pkgs if not pkg==ASPHINX_NAMELIB]:
    sphinx.generate_rst(root="{ASPHINX_LIBROOT}/".format(ASPHINX_LIBROOT=ASPHINX_LIBROOT),
                        package="{ASPHINX_LIBROOT}/{pkg}".format(ASPHINX_LIBROOT=ASPHINX_LIBROOT,
                                                         pkg=pkg.replace(".", "/")),
                        pkg=pkg)


replace_dir("{}/html".format(CURRENT_DIR))
replace_dir("{}/doctrees".format(CURRENT_DIR))

prefixe =\
"{ASPHINX_NAMELIB}\n===========\n.. toctree::\n\t:maxdepth: 2\n\t:caption: Package Reference\n\n".format(ASPHINX_NAMELIB=ASPHINX_NAMELIB)

suffixe = \
".. automodule:: {ASPHINX_NAMELIB}\n\
   :members:\n".format(ASPHINX_NAMELIB=ASPHINX_NAMELIB)


middle =  "\n".join(["   {ASPHINX_NAMELIB}.{pkg}".format(ASPHINX_NAMELIB=ASPHINX_NAMELIB, pkg=pkg) for pkg in pkgs]) + "\n\n"

output = "{}{}{}".format(prefixe, middle, suffixe)

with open("index.rst", "w") as f:
    f.write(output)

