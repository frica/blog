AUTHOR = ''
SITENAME = "Blog like it's 2002"
SITESUBTITLE = 'Tech and stuff'
SITEURL = ""
TIMEZONE = 'Europe/Brussels'
DEFAULT_LANG = 'en'

# Path to content directory to be processed by Pelican
PATH = "content"

STATIC_PATHS = ['images', 'pages/assets']
PLUGIN_PATHS = ['pelican-plugins']
PAGE_PATHS = ['pages']

# Main Menu
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Home', 'index.html'),
    ('About', 'pages/about.html'),
    ('Tech', 'category/tech.html'),
    ('Books', 'category/books.html'),
    ('Notes', 'category/notes.html'),
    ('Archives', 'archives'),
    ('Tags', 'tags')
)

# European date format
DEFAULT_DATE_FORMAT = '%d-%m-%Y'

# provide a list of paths to overrides files in original template
THEME_TEMPLATES_OVERRIDES = ['./themes/templates/overrides']

# doesn't work :(
CSS_STYLE = "./themes/css/custom.css"

# post_stats only works if you update the template
PLUGINS = ['post_stats', 
           'liquid_tags']

LIQUID_TAGS = ["img", "literal", "video", "youtube",
               "vimeo"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Code highlighting the theme
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.meta': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {'css_class': 'codehilite'},
    },
    'output_format': 'html5',
}

# deprecated
#MD_EXTENSIONS = ['codehilite(noclasses=True, pygments_style=native)', 'extra']  # enable MD options
#PYGMENTS_STYLE = 'monokai'

HIDE_AUTHORS = True

# Blogroll
# LINKS = (
#    ("Pelican", "https://getpelican.com/"),
# )

# Social widget
#SOCIAL = (
#    ("linkedin", "https://www.linkedin.com/in/fabien-rica/"),
#    ("github", "https://github.com/frica"),
#)

# customized to make admonition work but it doesn't
#MARKDOWN = {
#    'extension_configs': {
#        'markdown.extensions.codehilite': {'css_class': 'highlight'},
#        'markdown.extensions.extra': {},
#        'markdown.extensions.meta': {},
#        'markdown.extensions.admonition':{}
#    },
#    'output_format': 'html5',
#}

# for Flex
#SITELOGO = 'images/profile.png'
#FAVICON = 'images/favicon.ico'

# Alchemy
# SITEIMAGE = 'images/test.jpg width=200 height=200'

# ICONS = (
#     ("linkedin", "https://www.linkedin.com/in/fabien-rica/"),
#    ("github", "https://github.com/frica"),
#)

#THEME = 'themes/pelican-alchemy/alchemy'
# BOOTSTRAP_CSS = 'http://bootswatch.com/3/united/bootstrap.min.css'