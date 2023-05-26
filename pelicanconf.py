#!/usr/bin/env python

AUTHOR = 'nyuu'
SITENAME = 'nyuu dot page'
SITEURL = ''

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '%a %b %d, %Y'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# NOTE: These aren't called just LINKS and SOCIAL because those are assumed by
# the default theme to be 2-tuples, but I need more info.
LINKS_EX = (
(
  '⏎ posts',
  '/blog/',
  '#9966cc', 'category-blog.png',
  "「unlimited post works」",
), (
  '⏎ notes',
  '/notes/',
  '#9966cc', 'category-notes.png',
  "just the tips",
), (
  '⌥ everything (feed)',
  '/everything/',
  '#c57be6', 'category-everything.png',
  "both of the kinds of posts",
), (
  '⌥ everything (list)',
  '/everything/archives/',
  '#399ccd', 'category-archives.png',
  "walk the æons",
))

SOCIAL_EX = ((
  'email',
  'mailto:nyuutsu@protonmail.com',
  '#9966cc', 'logo-email.png',
  "the true name",
), (
  'twitter',
  'https://twitter.com/shroomwaview',
  '#55acee', 'logo-twitter.png',
  "realm of wind and ghosts",
), (
  'github',
  'https://github.com/nyuutsu',
  '#4183c4', 'logo-github.png',
  "attempts that have been made",
))
TWITTER_USERNAME = 'shroomwaview'
GITHUB_URL = 'https://github.com/nyuutsu'

DEFAULT_PAGINATION = 17
DEFAULT_ORPHANS = 4
PAGINATION_PATTERNS = (
  (1, '{base_name}/', '{base_name}/index.html'),
  (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

THEME = 'theme'

def sort_by_article_count(tags):
  return sorted(tags, key=lambda pairs: len(pairs[1]), reverse=True)

JINJA_FILTERS = dict(
  sort_by_article_count=sort_by_article_count,
)

# Smart quotes and other things
TYPOGRIFY = True
# Stop putting &nbsp; in the fucking article titles
TYPOGRIFY_IGNORE_TAGS = [
  'pre', 'code', 'header', 'h1', 'h2', 'h3', 'aside',
]

MARKDOWN = dict(
  extension_configs={
    'markdown.extensions.codehilite': dict(
      css_class='highlight',
      linenums=True,
    ),
    'markdown.extensions.extra': {},
    # GitHub-style fenced code blocks
    'markdown.extensions.fenced_code': {},
    # I don't actually care about a table of contents, but this turns headers
    # into self-links
    'markdown.extensions.toc': dict(anchorlink=True),
  },
)

PATH = 'content/'
PAGE_PATHS = ['../pages/']
PATH_METADATA = '../pages/(?P<fullpath>.+)[.].+'
STATIC_PATHS = ['favicon.png', 'media/']

# Leave .html alone; I only use it for static attachments, not posts
READERS = dict(html=None)

# For the landing page
TEMPLATE_PAGES = {
  '../theme/templates/home.html': 'index.html',
}

# URL schema; compatible with Octopress, but i happen to like it anyway
ARCHIVES_URL = 'everything/archives/'
ARCHIVES_SAVE_AS = 'everything/archives/index.html'
ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
CATEGORIES_URL = 'everything/categories/'
CATEGORIES_SAVE_AS = 'everything/categories/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
# This is the /blog/ index specifically
INDEX_SAVE_AS = 'everything/index.html'
INDEX_URL = 'everything/'
PAGE_URL = '{fullpath}/'
PAGE_SAVE_AS = '{fullpath}/index.html'
TAG_URL = 'everything/tags/{slug}/'
TAG_SAVE_AS = 'everything/tags/{slug}/index.html'
TAGS_URL = 'everything/tags/'
TAGS_SAVE_AS = 'everything/tags/index.html'

# Octopress-compatible filename metadata parsing
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

### Plugins
# Some minor hackery to have multiple PLUGIN_PATHs, since I want both canonical
# plugins and one of my own...
import os.path
import sys
sys.path.insert(0, os.path.dirname(__file__))
import eeveeblog.liquid_gallery
import eeveeblog.liquid_illus
import eeveeblog.liquid_photo
import nyuublog.liquid_card
import nyuublog.liquid_anchcard
import nyuublog.liquid_unicard
import nyuublog.liquid_prematter

# Add a Pygments lexer, which seems to require hacking Pygments guts?
from eeveeblog.rgbasm_lexer import RGBASMLexer
import pygments.lexers._mapping
pygments.lexers._mapping.LEXERS['RGBASMLexer'] = (
  'eeveeblog.rgbasm_lexer',
  RGBASMLexer.name,
  tuple(RGBASMLexer.aliases),
  tuple(RGBASMLexer.filenames),
  tuple(RGBASMLexer.mimetypes))

PLUGIN_PATHS = ["pelican-plugins.git"]
PLUGINS = [
  nyuublog.liquid_card,
  nyuublog.liquid_unicard,
  nyuublog.liquid_anchcard,
  nyuublog.liquid_prematter,
  eeveeblog.liquid_gallery,
  eeveeblog.liquid_illus,
  eeveeblog.liquid_photo,
  'summary',
  'custom_article_urls',
  'photos',
  'render_math',
  'thumbnailer',
  'simple_footnotes'
]

# Plugin config for summary
SUMMARY_BEGIN_MARKER = '<!-- just kidding i never use this -->'
SUMMARY_END_MARKER = '<!-- more -->'  # octopress compat
# This is actually a stock setting; I don't want an automatic summary if I
# don't use an explicit marker
SUMMARY_MAX_LENGTH = None

# Plugin config for custom article urls
# Preserve the old blog URL for blog stuff
CUSTOM_ARTICLE_URLS = {
  'blog': dict(
    URL='{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/',
    SAVE_AS='{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html',
  ),
}

# Plugin config for photos
PHOTO_LIBRARY = 'content/galleries/'
PHOTO_GALLERY = (1280, 1280, 95)
PHOTO_ARTICLE = (320, 320, 95)
PHOTO_THUMB = (224, 224, 95)
# The dumb fucking thing uses multiprocessing and passes along the ENTIRE
# SETTINGS DICT, which includes everything in this file, which includes
# PLUGINS, which (necessarily) includes a module reference, which is
# unpickleable, which causes the who dang thing to silently fail.  This puts it
# in "debug" mode and does the processing in-process.
PHOTO_RESIZE_JOBS = -1

# Plugin config for thumbnailer
IMAGE_PATH = 'media'
THUMBNAIL_DIR = 'media'
# this did work, but I'm not clear on what else is needed to get it to do so
# maybe manually removing the pycaches? absurd if true
THUMBNAIL_SIZES = dict(m='?x500')
THUMBNAIL_KEEP_NAME = False
THUMBNAIL_KEEP_TREE = True
