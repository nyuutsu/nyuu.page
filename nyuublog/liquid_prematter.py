# liquid_tags plugin for generating "show on hover" explainer text
# requires "tcg css-only card preview thing" from all.scss

# syntax: {% prematter %}

import os.path
import sys

sys.path.insert(0, 'pelican-plugins.git')

from liquid_tags.mdx_liquid_tags import LiquidTags

@LiquidTags.register('prematter')
def prematter(preprocessor, tag, markup):
  return '<p class="prematter">This post contains ✨on-hover card images✨, indicated by the <a href="https://en.wikipedia.org/wiki/Hanafuda">hanafuda card symbol, "🎴"</a>, like so:<span class="showhim"><a href="https://scryfall.com/card/dka/24/thalia-guardian-of-thraben">Thalia!<img src="/media/prematter/thals.png" class="showme"></a></span></p>'

# this import makes pelican registration work
from liquid_tags import register
