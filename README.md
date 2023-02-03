This is the source for (most of) my website [nyuu.page](https://nyuu.page).

It's powered by [Pelican][], a Python static blog system. The [theme was developed by eevee](https://github.com/eevee/eev.ee) and changed from there.

If you want to use this, you may want the following: `git`, `python`, `pelican`, `markdown`, `rsync`, `sass`, a server…

  If you want a *server*: I'm a fan of [Caddy](https://caddyserver.com/). The relevant part of my caddyfile can be found [here](https://gist.github.com/nyuutsu/5b11bce0e7c415926934caa08994ab4c1)

All that said, if you want to use this:

* You'll probably want the pelican plugins, so get those

`git submodule update --init`

* The css is written in sass, so the actual `.css` is pretty gnarly. If you want to make changes, make them to the `.scss` file and regenerate the css like so

`sass /theme/static/sass/all.scss /theme/static/css/all.css`

* Alias i'm using to generate and deploy is listed below. Probably change the url in the command unless you're trying to become me.

`alias nyuu.page='cd ~/repos/nyuu.page && pelican content && rsync -avc --delete output/ nyuu.page:/var/www/html/'`

[Pelican]: http://docs.getpelican.com/
