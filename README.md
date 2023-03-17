This is the source for (the static parts of) my website [nyuu.page](https://nyuu.page). The relevant part of my caddyfile can be found [here](https://gist.github.com/nyuutsu/5b11bce0e7c415926934caa08994ab4c)

### how do I do this

* clone it somewhere (`git`, `ssh`…)

* you'll need the pelican plugins (`python`, `pip`, `pelican`)

`git submodule update --init`

* you'll need the stuff listed in the requirements file

`pip install -r requirements.txt` (old `markdown`, etc)

### how do I put this online

what *i'm* doing is using this alias:

`alias nyuu.page='cd ~/repos/nyuu.page && sass theme/static/sass/all.scss theme/static/sass/all.css && make publish && rsync -avc --delete output/ nyuu.page:/var/www/ && rm theme/static/sass/all.css & rm theme/static/sass/all.css.map'` (`sass, rsync`)

### how do I test changes

You'll want to set up live sass recompilation, and run `make devserver`

[Pelican]: http://docs.getpelican.com/
