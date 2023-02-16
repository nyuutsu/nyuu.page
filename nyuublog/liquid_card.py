# liquid_tags plugin for generating "show on hover" html boilerplate w/o a link
# liquid_anchard's sibling
# requires "tcg css-only card preview thing" from all.scss

# syntax: {% card filename text with spaces %}
# example: {% card /media/sample-post/thals.png Thalia, Guardian of Thraben! %} 

import os.path
import re
import sys

sys.path.insert(0, 'pelican-plugins.git')

from liquid_tags.mdx_liquid_tags import LiquidTags

@LiquidTags.register('card')
def card(preprocessor, tag, markup):

  naive_regex = re.fullmatch(r'(\S+) (.+)', markup, re.VERBOSE)
  
  return f'<span class="showhim">{naive_regex.groups()[1]}<img src="{naive_regex.groups()[0]}" class="showme"></span>'
  
# this import makes pelican registration work
from liquid_tags import register