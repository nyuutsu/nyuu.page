title: How to make browsing fandom.com not suck
date: 2023-2-10 15:00
category: blog
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

See gallery below for a "before" and "after". See below the fold for elaboration.

{% gallery /media/fandom-note
  before.png no filters
  after.png filters
%}

<!-- more -->

## eHow

[Content farming] is as old as dirt. Getting on lots of high-ranking search results at low cost is a winning strategy for getting lots of ad views. So, the thinking is, users might *like* it if you spend lots on making the site great, but their liking it doesn't bring in ad money commesurate to the effort. So, the farmer wants to make their content as cheaply as possible; the content being *useful* is but unnecessary. So you pay people [$15 an article] to write articles like "[How to Put on a Speedo]" and Google dutifully rewards you with the top result for `🔎 » "how to put on speedo"`.

In this way, for a few years, eHow took over google search results, and mass-producing content-for-eHow became a semi-popular form of online menial labor. This was until [about a decade ago]. Today's search result quality problems are a bit more subtle than yesteryear's "Google=eHow". Drowning the world in content nobody wanted to read or to write *might work* but it's a lot harder to make it work when your host is trying to discourage that sort of thing.

## Fandom dot inc

[Fandom][fandom] (né-wikia) is a wiki hosting service. It was cofounded by Jimmy Wales (of *Wikipedia* fame). It has been *aggressive* about acquiring other wiki hosting services. You've probably seen one of their holdings in the results if you've ever searched about a popular media franchise.

I think their overall strategy is shaped pretty similarly to eHow's: as cheaply as possible be the top search result for as many questions as possible. Though these questions are trivia like `🔎 » "what country is bandit keith from"`¹ rather than tutoral questions like the aforementioned `🔎 » "how to put on speedo"`. The content is even made for free by enthusiasts, which is a pretty sick deal. None of this is a *problem*²; it's a pretty clever business to be in!

The thing is, Fandom uses *hella* advertising on its pages. The user experience on their pages is *terrible*. Look at this nonsense:

{% gallery /media/fandom-post
  full-nofilter.png no adblock whatsoever
  full-nofilter-emphasis.png the green areas are the content
%}

The first image is a full-page screenshot of a page on a fandom wiki as its owners intend it to be seen. The second image is a map (is there a better word for this?) of the *content* on that page. The green is content, the black is advertisements and cruft. You really should use an adblocker. Even [the FBI]'s position on this is "you, the user, should use an adblocker when going online".

If you install [ublock origin] and turn on the top one or two default filters, and try again: there's *less* advertising, but half of the vertical length is still intrawiki advertisements, a lot of the horizontal length is cruft and more advertisements, and there's an autoplay video advertisement down in the lower right corner. It's really not a good scene and I'd strongly recommend filtering out the crap as discussed in "[this note]".

Here is a comparison, of what the page looks like with no filtering, with "standard filters", and with the additional filters I'm using:

{% gallery /media/fandom-post
  full-nofilter.png no adblock
  full-yesfilter-basic.png some adblock
  full-yesfilter-custom.png more adblock
%}

This could surely be improved on; I don't even remove the padding allocated to the orange bar on the left. There is so much space on these pages just waiting to be put to useful purpose.

## benchmarking

There isn't much of a page size or load speed difference between the "some adblock" and "more adblock" views. The results for each are shown here³:

{% gallery /media/fandom-post
  yesfilter-basic.png some adblock
  yesfilter-custom.png more adblock
%}

The "more adblock" view pulls in about 2/3 as much stuff as "some adblock", but both decompress to being of roughly equal size anyway. They finish loading at roughly the same time. Both blow the unfiltered version out of the water, in the sense that without adblock, the page continues loading more advertisements in the background forever. Below are two screenshots taken at arbitrarily-selected points after the visible content was finished loading.

{% illus /media/fandom-post/nofilter-a.png after a few seconds %}

{% illus /media/fandom-post/nofilter-b.png a bit later and it's still going %}

¹ the google infobox currently gets this [wrong] due to how the "abridged series" fanwork gets this wrong as a joke, and that fanwork has a wiki

² actually, it might be rent-seeking, which would be a problem

³ If you'd like to try it yourself: probably every browser's dev tools allow this; in Firefox: `f12` → network → ☑ 'disable cache' → `f5`

---

[this note]: https://nyuu.page/notes/2023/02/10/fandom%20ublock%20gist/
[Content farming]: https://en.wikipedia.org/wiki/Content_farm
[about a decade ago]: https://en.wikipedia.org/wiki/Google_Panda
[$15 an article]: https://server.moneysavingmom.com/how-to-make-money-writing-for-ehow-com/
[How to Put on a Speedo]: https://worstofehow.wordpress.com/2011/01/01/how-to-put-on-a-speedo/
[fandom]: https://www.fandom.com/
[google infobox]: https://www.google.com/search?client=firefox-b-1-d&q=what+country+is+bandit+keith+from
[the FBI]: https://www.ic3.gov/Media/Y2022/PSA221221?=8324278624
[ublock origin]: https://ublockorigin.com/
[wrong]: https://nyuu.page/media/fandom-footnote/bandit-keith.png