This is the source for (the static parts of) my website [nyuu.page](https://nyuu.page).

### How do I set this up

* Clone the project (prerequisites: `git`, `ssh`…)

`git clone https://github.com/nyuutsu/nyuu.page.git`

* Get pelican plugins

`git submodule update --init`

* Get requirements listed in the requirements file (prerequisites: `python`, shell compatible with the activation script (or willingness to modify the script?))

`python -m venv site_venv`

`source ./site_venv/bin/activate`

*coming back later and having problems? rerun this ↑*

`pip install -r requirements.txt`

### How do I put this online

You'll need a *server* and a *domain name*. You'll then need to use `pelican` to generate the site content by running `make publish`, and then you'll need to put that content onto your server.

###### How do I get a server

1. Set up a droplet (or, get a physical computer if you feel like figuring out getting it a static IP address on a residential connection 😩) → connect to the droplet → install server software e.g. caddy

2. Get a domain name → set up DNS records to point to the droplet

3. Configure the server to map a location on the drive (of the droplet) to the domain & to serve files from it → put some stuff in that location → run the server (ideally, run it in tmux, then detatch while it's running)

*[Caddy] handles getting your ssl cert automatically through "let's encrypt". let's encrypt allows five attempts per hour, and if your config is wrong you'll blow through these attempts without realizing it.*

*The relevant part of my caddyfile can be found [here](https://gist.github.com/nyuutsu/5b11bce0e7c415926934caa08994ab4c)*

###### How do I put it on my server

The bare minimum:

1. Run `make publish` to generate the site files in `/output`.

2. Copy the contents of `/output` onto the "served" location on your server using somegthing like `scp` or `rsync`

What *I* do is I put this very silly statement…

```
alias nyuu.page='cd ~/repos/nyuu.page && sass theme/static/sass/all.scss theme/static/sass/all.css && make publish && rsync -avc --delete output/ nyuu.page:/var/www/ && rm theme/static/sass/all.css & rm theme/static/sass/all.css.map'
```

…in my `.zshrc`, such that when run (» `nyuu.page`), I:

1. Change to my project's directory

2. Generate the css from the `.scss` file (download sass → stick it somewhere → add that somewhere, to your PATH)

3. Run `make publish`

4. Copy the relevant things over to the correct location on my server

5. Clean up locally by removing the generated css and the output directory

### how do I test changes

Set up live sass recompilation (left as an exercise to the reader), run `make devserver`, and then go to whatever it tells you to. In my case it's [127.0.0.1:8000/](127.0.0.1:8000/).

[Pelican]: https://docs.getpelican.com/
[Digital Ocean]: https://digitalocean.com/
[Caddy]: https://caddyserver.com/