#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Teng Long'
SITENAME = u"Teng Long's Homepage"
SITEURL = 'http://longtengz.github.io'

RELATIVE_URLS = True

THEME = "themes/pelican-svbhack/"

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'


# Personal Info 

GITHUB_URL = 'https://github.com/longtengz'

# Google analytics
GOOGLE_ANALYTICS = u'UA-40460783-2'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About', 'http://longtengz.github.io/about.html'),
        ('Notes', 'http://longtengz.github.io'),
        ('Projects', 'http://longtengz.github.io'),
        ('Resume', 'http://longtengz.github.io'),)

# Social widget
#  SOCIAL = (('You can add links in your config file', '#'),
          #  ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
