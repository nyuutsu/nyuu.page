# liquid_tags plugin for generating "show on hover" html boilerplate w/ a link
# liquid_card's sibling
# requires "tcg css-only card preview thing" from all.scss

# syntax: {% anchcard filename linkurl text %}
# example {% anchcard /media/sample-post/thals.png https://scryfall.com/card/dka/24/thalia-guardian-of-thraben Thalia, Guardian of Thraben! %}

import os.path
import re
import sys

sys.path.insert(0, 'pelican-plugins.git')

from liquid_tags.mdx_liquid_tags import LiquidTags

@LiquidTags.register('anchcard')
def anchcard(preprocessor, tag, markup):
  
  naive_regex = re.split(r'\s+', markup, 2, re.VERBOSE)
  
  return f'<span class="showhim"><a href="{naive_regex[1]}">{naive_regex[2]}<img src="{naive_regex[0]}" class="showme"></a></span>'

# this import makes pelican registration work
from liquid_tags import register
