# liquid_tags plugin for generating "show on hover" html boilerplate
# requires "tcg css-only card preview thing" from all.scss

# syntax: {% unicard filename [linkurl] text %}
# example {% unicard /media/sample-post/thals.png Thalia, Guardian of Thraben! %}
# example {% unicard /media/sample-post/thals.png https://scryfall.com/card/dka/24/thalia-guardian-of-thraben Thalia, Guardian of Thraben! %}

import os.path
import re
import sys

sys.path.insert(0, 'pelican-plugins.git')

from liquid_tags.mdx_liquid_tags import LiquidTags

@LiquidTags.register('unicard')
def unicard(preprocessor, tag, markup):

  naive_parser = markup.split(None, 2)
  
  if '/' not in naive_parser[1]:
    regex = re.fullmatch(r'(\S+) (.+)', markup, re.VERBOSE)
    return f'<span class="showhim">{regex.groups()[1]}<img src="{regex.groups()[0]}" class="showme"></span>'
  
  regex = re.split(r'\s+', markup, 2, re.VERBOSE)
  return f'<span class="showhim"><a href="{regex[1]}">{regex[2]}<img src="{regex[0]}" class="showme"></a></span>'

# this import makes pelican registration work
from liquid_tags import register
