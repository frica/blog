SITENAME = "Blog like it's 2002"
SITESUBTITLE = 'tech and stuff'
SITEURL = ""
TIMEZONE = 'Europe/Brussels'
DEFAULT_LANG = 'en'
AUTHOR = "Fabien Rica"
SITEDESCRIPTION = "Fabien Rica's homepage"
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<title>.*)'

# Path to content directory to be processed by Pelican
PATH = "content"
# Path to static resources
STATIC_PATHS = ['images', 'extra', 'pages/assets']
PLUGIN_PATHS = ['plugins/']
PAGE_PATHS = ['pages']

# overly complex config for a simple favicon but ok
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/robots.txt": {"path": "robots.txt"}
}

# Main Menu
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('/home',  'index.html'),
    ('/tech',  'category/tech.html'),
    ('/books', 'category/books.html'),
    ('/misc',  'category/misc.html'),
    ('/notes', 'category/notes.html'),
    ('/links', 'category/links.html'),
    ('/uses',  'pages/uses.html'),
    ('/now',   'pages/now.html'),
    ('/about', 'pages/about.html')
)

# European date format
DEFAULT_DATE_FORMAT = '%d-%m-%Y'

# provide a list of paths to overrides files in original template
# THEME_TEMPLATES_OVERRIDES = ['./themes/templates/overrides']
THEME = 'themes/mytheme'

# post_stats only works if you update the template
PLUGINS = ['liquid_tags',
           'sitemap', 
           'goodreads_activity']

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

GOODREADS_ACTIVITY_FEED='https://www.goodreads.com/review/list_rss/46395244?key=shzYOrsCNAprl60arNukkE7UkBNWcsHDeuOzUIZynvqOlRdy&shelf=currently-reading'
