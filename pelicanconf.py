#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Teng Long'
SITENAME = u"Teng Long's Homepage"
SITEURL = 'http://ilab.rutgers.edu/~tl505'

RELATIVE_URLS = True

THEME = "themes/pelican-svbhack/"

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About', 'http://ilab.rutgers.edu/~tl505/about.html'),
         ('Notes', 'http://ilab.rutgers.edu/~tl505'),
         ('Projects', 'http://ilab.rutgers.edu/~tl505'),
         ('Resume', 'http://ilab.rutgers.edu/~tl505'),)

# Social widget
#  SOCIAL = (('You can add links in your config file', '#'),
          #  ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
