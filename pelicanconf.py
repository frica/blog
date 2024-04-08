SITENAME = "Blog like it's 2002"
SITESUBTITLE = 'tech and stuff'
SITEURL = ""
TIMEZONE = 'Europe/Brussels'
DEFAULT_LANG = 'en'

# Path to content directory to be processed by Pelican
PATH = "content"
# Path to static resources
STATIC_PATHS = ['images', 'extra', 'pages/assets']
PLUGIN_PATHS = ['pelican-plugins']
PAGE_PATHS = ['pages']

# overly complex config for a simple favicon but ok
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
}

# Main Menu
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Home', 'index.html'),
    ('Tech', 'category/tech.html'),
    ('Books', 'category/books.html'),
    ('Misc', 'category/misc.html'),
    ('Notes', 'category/notes.html'),
    ('About', 'pages/about.html')
)

# European date format
DEFAULT_DATE_FORMAT = '%d-%m-%Y'

# provide a list of paths to overrides files in original template
# THEME_TEMPLATES_OVERRIDES = ['./themes/templates/overrides']
THEME = 'themes/mytheme'

# post_stats only works if you update the template
PLUGINS = ['liquid_tags',
           'sitemap']

SITEMAP = {
    'format': 'xml',
    'exclude': ['tag/', 'category/'],
    'changefreqs': {
        'articles': 'daily',
        'pages': 'monthly',
        'indexes': 'daily'
    }
}

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

# Default code highlighting in the theme - replaced by Pygments
# MARKDOWN = {
#     'extension_configs': {
#         'markdown.extensions.meta': {},
#         'markdown.extensions.extra': {},
#         'markdown.extensions.codehilite': {'css_class': 'codehilite'},
#     },
#     'output_format': 'html5',
# }

HIDE_AUTHORS = True

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

# BOOTSTRAP_CSS = 'http://bootswatch.com/3/united/bootstrap.min.css'