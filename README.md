This is the source for (the static parts of) my website [nyuu.page](https://nyuu.page).

### first, you'll need to have the project, and pelican, and necessary plugins

* clone this project somewhere (`git`, `ssh`…)

* you'll need the pelican plugins (`python`, `pip`, `pelican`)

`git submodule update --init`

* you'll need the stuff listed in the requirements file

*You should probably use a virtual environment for this. I don't, but, you should try to be better than me.*

`pip install -r requirements.txt` (old `markdown`, etc)

### how do I put this online

You'll need a *server* and a *domain name*. You'll then need to use `pelican` to generate the site content, and then you'll need to put that content onto your server.

###### getting a server

in short: get a computer of some sort, connect it to the internet, and install on it a web server software package (e.g. apache, or nginx, or caddy). Set up DNS records. Configure the software to create a mapping between your domain and a location on the drive of that server. Now, actually run the server software.

*I'm a fan of [Caddy]. The configuration is succinct. It'll even handle getting your https cert automatically. (for better or worse: it will do this automatically; you may not even notice this unless you go looking at logs or systemd service statuses. you may accidentally blow through "Let's Encrypt"'s five-ssl-cert-request-attempts-per-hour cap without even knowing you'd done anything, which means having to wait a bit before trying with new settings)*

*The relevant part of my caddyfile can be found [here](https://gist.github.com/nyuutsu/5b11bce0e7c415926934caa08994ab4c)*

###### putting stuff on the server

the bare minimum:

1. run `make publish` to generate the site files in `/output`.

2. copy the contents of `/output` onto the "served" location on your server using e.g. `rsync -avc your.domain.or.ip.address:/the/served/location/`

what *I* do, however, is I put this very silly statement…

````alias nyuu.page='cd ~/repos/nyuu.page && sass theme/static/sass/all.scss theme/static/sass/all.css && make publish && rsync -avc --delete output/ nyuu.page:/var/www/ && rm theme/static/sass/all.css & rm theme/static/sass/all.css.map'` (`sass, rsync`)```

…in my `.zshrc`, such that when run (» `nyuu.page`), will:

1. changes to my project's directory

2. generates the css from the `.scss` file (you'll need *sass*. don't forget to add it to your PATH after!)

3. runs `make publish`

4. copies the relevant things over to the correct location on my server

5. cleans up after itself locally by removing the generated css and the output directory


### how do I test changes

You'll want to set up live sass recompilation, run `make devserver`, and then go to whatever it tells you to. in my case it's [127.0.0.1:8000/](127.0.0.1:8000/).

[Pelican]: https://docs.getpelican.com/
[Digital Ocean]: https://digitalocean.com/
[Caddy]: https://caddyserver.com/