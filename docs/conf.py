project = "iPSC Corpus Kit"
author = "iPSC Corpus Kit contributors"
copyright = "2026, iPSC Corpus Kit contributors"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

html_theme = "furo"
html_title = "iPSC Corpus Kit"
html_logo = "_static/ipsc-corpus-kit-logo.png"
html_static_path = ["_static"]
html_theme_options = {
    "sidebar_hide_name": False,
}
