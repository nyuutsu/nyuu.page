This is the source for (most of) my website [nyuu.page](https://nyuu.page). It's powered by [Pelican][], a Python static blog system. I cribbed a bunch from [eevee's site](https://github.com/eevee/eev.ee).

If you want to use this, you may want the following: `git`, `python`, `pelican`, `markdown`, `rsync`, `sass`, a server…

  If you want a *server*: I'm a fan of [Caddy](https://caddyserver.com/). The relevant part of my caddyfile can be found [here](https://gist.github.com/nyuutsu/5b11bce0e7c415926934caa08994ab4c)

All that said, if you want to use this as-is for some reason:

1. You'll need the pelican plugins

`git submodule update --init`

2. Alias i'm using to generate and deploy is very silly, and is listed below

`alias nyuu.page='cd ~/repos/nyuu.page && sass theme/static/sass/all.scss theme/static/sass/all.css && pelican content && rsync -avc --delete output/ nyuu.page:/var/www/html/ && rm theme/static/sass/all.css & rm theme/static/sass/all.css.map'`

Whereas if you want to make changes then you should probably set up something to recompile the css every time you make changes, and run `make devserver` to make observing the changes easy.

[Pelican]: http://docs.getpelican.com/
