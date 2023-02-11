title: Improving "fandom.com" usability via ublock filters
date: 2023-2-10 14:12
category: notes
tags: ui, web

tl;dr: put this in your ublock filter list if you want to have an easy life:

```
! fandom.com
fandom.com##.global-navigation
fandom.com##.WikiaRail.right-rail-wrapper
fandom.com##.mcf-wrapper
fandom.com##.global-footer
fandom.com##.page__right-rail
fandom.com##.render-wiki-recommendations > div
```

See gallery below for a "before" and "after". Later today I'll elaborate.

{% gallery /media/fandom-note
  before.png no filters
  after.png filters
%}