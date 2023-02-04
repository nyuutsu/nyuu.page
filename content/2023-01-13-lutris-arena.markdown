title: Installing Magic: the Gathering Arena through Lutris
date: 2023-1-13 11:06
category: blog
tags: magic, wine

Magic: the Gathering Arena is a way to play Magic: the Gathering on your computer. It is designed in the way of a [gacha mobile game](https://en.wikipedia.org/wiki/Gacha_game), so, you probably shouldn't play it.

You could play on Cockatrice, for free. Which is a great option if you have a buddy to play with. But there aren't *that* many opponents available. And sometimes they play, but they throw chat tantrums about your deck or the game. The rules enforcement is manual, which I find charming overall but impractical when i'm not on a voice call against my opponent. You cannot just click "find me an opponent" and get handed an ISO-standard 'game of magic'.

You could play on Magic Online and you'll have all the formats, card rental and trade, actually good stops and yields, and strong opponents. If you can get it to run decently, which I was never able to on linux. The performance was bad and the text never looked quite right.

So maybe trying to run MTGA looks pretty appealing anyway, since maybe it'll run smoothly if you can get it to run at all.

<!-- more -->

Manually configuring Wine is a task unfit for humans. Helpers like Lutris are great. Enthusiasts write scripts to facilitate the installation. in the best case, the script will download and install a current, well-performing, self-updating program for you.

I went to Lutris' [MTGA page](https://lutris.net/games/magic-the-gathering-arena/), ran each of the installers, got cryptic error messages from all of them, and found nothing helpful about this on google. Here is what worked for me:

* [This page](https://mtgarena.downloads.wizards.com/Live/Windows64/version), under the "CurrentInstallerURL" key, links to the `.msi` installer. Copy this link.

e.g. it says

```json
"CurrentInstallerURL":  "[...]/4411.977745/MTGAInstaller_0.1.4411.977745.msi" 
```

what we want is

`https://mtgarena.downloads.wizards.com/Live/Windows64/versions/4411.977745/MTGAInstaller_0.1.4411.977745.msi`

* Create a [lutris.net](https://lutris.net/) account and log in. Now, go [here](https://lutris.net/games/magic-the-gathering-arena-manually-updated/installer/edit).

* In the `Content` box, change the script like so:

script says:
```yaml
...
- setup: [...]/3971.904583/MTGAInstaller_0.1.3971.904583.msi
...
- task:
...
    args: /i "$CACHE/mtg-arena/MTGAInstaller_0.1.3971.904583.msi" /q
...
```
change these blocks to:
```yaml
...
- setup: [...]/4411.977745/MTGAInstaller_0.1.4411.977745.msi
...
- task:
...
    args: /i "$CACHE/mtg-arena/MTGAInstaller_0.1.4411.977745.msi" /q
...
```
where the new link in `- setup` is the one from the "CurrentInstallerURL" field back in step 1, and the filename in `- task` is the filename at the end of that link.

* Click `Test this installer`. Click through the installer.
