title: Magic has a linkrot problem
date: 2023-2-14 00:00
category: blog
tags: trading card games, magic, web

*[Magic]* has a [linkrot] problem. What should we do about it?

<!-- more -->

Magic and Magic-related websites have a problem: a lot of their links don't work! In some cases, this is understandable. For example, "[the dojo]" has been defunct for twenty years, so it is perhaps unreasonable to be mad at them for the original link to "[who's the beatdown]" breaking.

Other cases are harder to understand.

* In Magic Arena, in the shop, until *very recently*, the in-app link to the page on Wizards of the Coast's site about pack droprates, was broken, and had been wrong for months. The link provided in Arena was [this one][broken mtx link]; the information on the website was actualy [over here][fixed mtx link]. *These days, the in-app link works and points [here][new mtx link]*

* On the Wizards of the Coast's website, links  to *other parts of the Wizards's of the Cost website* sometimes don't work. This [list of articles] has an entry named `Week #397 (August 4, 2009) – "Designing for Johnny"`. The link points to [here][johnny404] which 404s. Searching for a working link via google didn't go turn up anything. Searching via DuckDuckGo worked and turned up [this][johnnycanonical]. So, at some point wotc changed their article url pattern from `/articles/archive/foo` to `/news/making-magic/foo`, but also changed the article publish date? 🤔

That article is pretty old, but, it's not like its dead content or anything. Mark Rosewater's posts link extensively to his older posts, which is why I ended up finding the above oddity. The big vendors do these site reorganizations that change the location (or remove entirely) older articles and then don't update the links to those articles to match the new location. It's pretty hit or miss whether the on-hover card images in a given article will work five years down the line.

It'd be nice if the community would stop migrating all its strategy discussions and resources into the unindexable Discord walled garden, too. I figure doing so is at least partially a response to "stuff on Magic websites is too impermanent", but, Discord-hosted content can be fragile too and there's less recourse if something goes wrong.

I'm not really sure what the solution here is. Maybe there could be a browser extension, where you give it a whitelist of websites, and on those sites if you try to access 404ed content, the extension Googles or DDGs for terms that *ought* to find a working link to the content, and serves up the search results, or seamlessly takes you to the first result.

---

[magic]: https://en.wikipedia.org/wiki/Magic:_The_Gathering
[linkrot]: https://en.wikipedia.org/wiki/Link_rot
[the dojo]: https://mtg.fandom.com/wiki/The_Dojo
[who's the beatdown]: https://articles.starcitygames.com/articles/whos-the-beatdown/
[broken mtx link]: https://magic.wizards.com/en/promotions/drop-rates
[fixed mtx link]: https://magic.wizards.com/en/mtgarena/drop-rates 
[new mtx link]: https://magic.wizards.com/en/mtgarena/drop-rates?utm_medium=product&utm_source=arena
[list of articles]: https://magic.wizards.com/en/news/making-magic/four-hundred-and-counting-2009-09-25
[johnny404]: https://magic.wizards.com/en/articles/archive/designing-johnny-2009-08-03
[johnnycanonical]: https://magic.wizards.com/en/news/making-magic/designing-johnny-2009-07-31