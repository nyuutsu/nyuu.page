title: Lengthen your web browser!
date: 2023-3-24 00:00
category: blog
tags: tutorial, ui

<aside class="aside" markdown="1">
This post may be *culturally specific*: my primary language is English; I am thinking about UIs for English speakers. Many languages read right-to-left or vertically; perhaps their needs are better served by horizontal tab bars? If you know, tell me in the comments.
</aside>

Vertical space is better than horizontal space and you should guard it jealously.

Why it is better:

* Most experiences people have on computers aren't very needy for horizontal space

* Most experiences people have on computers are *infinitely tall*.

What you can do about it:

* Get [treestyletab] **and** hide the horizontal tab bar.

I shall explain how[ref]Rather, I'll give the tl;dr of how. If I write a detailed tutorial it'll be another in post.[/ref]and why.

<!-- more -->

### ⏰🔥💯 on configuration🔥👴🤏

I have spent many hours using computers. It's possible you're *reading this* and I have spent more hours *staring at a screen* than you have spent *being alive*. In that time I have become rather picky. Over enough repetitions of basic tasks ("open a program", "load a webpage", "faff around in a directory") I bristle at the prospect of the task being *slow* or *ugly*. Towards the end of making "using a computer" work exactly how I'd like it to, I'm running linux with my hands on lots of the [knobs and switches].

I don't recommend digging through or copying my choices, though. There mostly aren't right or wrong choices and your preferences will be different from mine.

But if your job is, approximately, "using a computer", you owe it to yourself to spend some time whipping your workspace into *your* ideal shape. If you routinely get annoyed at something in your workflow that you plausibly could configure your way into eliminating, you really should do that. Make computers do "tasks fit for computers"; don't do them yourself on the computer's behalf.

### on browser tabs

The browser tab was invented in 1998 by [SimulBrowse][ref]Installer found courtesy of [Evolt][/ref] (later renamed NetCaptor) and their behavior and presentation is nearly unchanged. SimulBrowse looked like this:

{% gallery /media/vertical-space
  simulbrowse-3.png several tabs on http://gnu.org/ open in SimulBrowse 3.0.1 
%}

The only significant difference is, the tab screen overflow behavior is "the tabs spill off of the side of the screen". They don't compress horizontally as you open more of them. You can look at different parts of the tab bar by clicking the <kbd>◂</kbd> and <kbd>▸</kbd> arrows found to the right of the tab bar: {% illus /media/vertical-space/simulbrowse-3-zoom.png several tabs on http://gnu.org/ the tab navigation arrows in SimulBrowse 3.0.1 %}

No later than 2004[ref]Which is way before most people started using tabs. the typical person probably started sometime around Firefox 2-3 (late 2006-early 2008) if they were ahead of the curve, or with the launch of Chrome (mid 2008) if they weren't Into Browsers enough to have tried early Firefox. In other words, in short, for the overwhelming majority of people, tabs have never changed at all.[/ref], the "tabs compress as you open more of them" behavior was invented. Firefox 1.0 (2004) has this; some earlier browser might also. "No later than 2004" is the last time the tab user experience has meaningfully changed, and what we have is pretty bad. It has two flaws:

1. Browsing is *hierarchical*; you start in one place and you carve a path through hyperlinks, possibly opening a few additional tabs from each page you visit. "Where you accessed something *from*" is a natural, useful signpost in keeping track of what you're up to. The tab bar is flat, so it can't capture this information.

2. Browsing is about *abundance*; you'll probably open dozens of tabs in the course of doing anything deeper than cursory research. Doing so squishes the tabs or drives them offscreen or both; it's difficult to have a decent quick reference of "what do I have open" onhand even though screen space is nominally being allocated to giving you this.

Some examples:

{% gallery /media/vertical-space
  horiz-30ish.png thirtyish google chrome tabs
%}

*Thirty tabs open in chrome: perhaps in the moment you can mostly keep track of what each thing is based on the favicon and first two letters and relative location on the bar?*

{% gallery /media/vertical-space
  horiz-lots.png fortyish google chrome tabs
%}

*Forty tabs: you get favicons and relative locations. nothing else*

**Lemma**: the horizontal browser tab bar is a historical accident and doesn't scale well with heavy use.

### on horizontal and vertical space

Vertical space is nearly arbitrarily valuable. Most of what people do on computers is browse endless feeds. How much feed you can be skimming at once is mostly bounded by how tall the viewport can be, which is bounded by the screen resolution minus any operating system and browser cruft.

The activities that *aren't* browsing endless feeds are still mostly vertically constrained. Programmers generally limit themselves to 80ish characters per line, so any one item in their text editor or IDE doesn't benefit from being larger than that. File/project explorers and in-window terminals/debugger consoles can generally be moved to the sides if they aren't already there by default.

Regardless of what you're up to, giving yourself more vertical space to do it in will probably make the experience better.

**Lemma**: getting rid of the horizontal tab bar and replacing it with something else might be nice.

Horizontal space is considerably less valuable. There are two reasons for this:

* Many activities are chat apps. Chat apps are thirsty for vertical space and are borderline indifferent to horizontal space.

Each message in a typical chat app is allocated at least one vertical "line" regardless of its length. The horizontal space of that line is filled with the message. If the message is too short to use up the entire line, the rest of the line left empty. If the message is too long to fit on one line, it gets word-wrapped across however many lines it requires.

Most chat conversations word-wrap very well. Most of the messages are way shorter than one "typical screen-length line", so there's lots of unused space after the lines. Consider the following anonymized discord conversations, presented in portrait and landscape view.

One of these screenshots was taken on my landscape-oriented 1920x1200 monitor:

{% illus /media/vertical-space/discord-horizontal.png discord viewed in a horizontal window %}

The other on my (identical but rotated 90°) portrait-oriented 1200x1920 monitor:

{% illus /media/vertical-space/discord-vertical.png discord viewed in a vertical window %}

The latter is able to show about twice as many lines (use the black box present in both images as a landmark if you'd like to check) despite having the same pixel count. This is because it doesn't have to spend tons of screen space on "the non-content between the end of the message and the right edge of the screen"

 There usually won't be a minimum message size, so some of the messages are quite short.

Arranging things in columns and then giving those columns lots of room to use is great since that is how people are used to seeing lists of things in English. Each thing goes on its own line; you can tell 

Doing so is a matter of personal taste, but it unquestionably *works* since writing *lists of items in english with the items on different lines* works great in a way that writing every item on one line wouldn't.

* Activities that aren't chat apps often limit themselves to relatively narrow widths and that's probably for the best.

If you have an ultrawide monitor you probably never open up a plaintext document in fullscreen with no wordwrap and then read the document using the entire monitor. However useful that monitor is for multitasking and for individual tasks that use the entire monitor as broken out into zones of interest: it isn't suited for "read from left to right, then at the end go all the way back to the left and down by one, then repeat". The distance between the start and the end of the lines is too large for this to be a good experience so people don't do it.

Websites figure you don't want to do that and won't let you. Below is a (once again, anonymized, since the content isn't the point) screenshot, this time of what I see when I visit twitter. This is as viewed on a typical 1920x1080 monitor:

{% illus /media/vertical-space/twitter-horizontal-padding.png twitter viewed in my web browser with the padding indicated in red and the content indicated in blue %}

*two-fifths-ish of the viewport is dedicated to horizontal padding!*

Twitter doesn't *want* you to view it in ultrawide. It responds to being fed more space by wasting more of it. It is pretty typical in this regard.

Reddit is an endless feed. Adding more horizontal resolution to the viewport doesn't allow it to show you more posts since it can only show one post per row. Nor does it allow you to view more comments at once since reddit also softwraps the commments to ~100 characters per line. Reddit is, in effect, a SPA designed for very tiny screens. Most websites, static or not, follow similar design principles.

**Lemma**: a lot of people have vertical regions of screen space that usually aren't being used for anything in particular.

### thus: 🌲 treestyletab 🌲

Check out my UI; it makes such elegant use of space by putting a tab *tree* in a sidebar and not having a tab bar at all[ref]Eschewing an address bar is a *bit* too radical for my tastes so "just browse in fullscreen mode" isn't quite right. If I really want to hide the tree, <kbd>F1</kbd> toggles showing/hiding it.[/ref]:

{% gallery /media/vertical-space
  my-ui.png firefox open to one of my reddit comments with the stock tab bar hidden and the treestyletab addon enabled
%}

Giving a *robust* tutorial for replicating this arrangement would involve writing *way* more, but the bullet point version can be written pretty concisely. To get this UI, use [Firefox], with:

* the [treestyletab] extension (provides the tree)

    
* the `toolkit.legacyUserProfileCustomizations.stylesheets` flag enabled in `about:config` (makes it possible to hide the tab bar)[ref]You'll need to restart Firefox for this change to take effect. You'll also need to restart for any changes in userChrome to take effect.
    
* the following rules in `{FirefoxProfileFolder}/chrome/userChrome.css`[ref]If you're following along and can't *find* the folder: go to `about:support` and check the entry for "Profile directory" for its location.[/ref] (actually hide the bar):

```css
#main-window[tabsintitlebar="true"]:not([extradragspace="true"]) #TabsToolbar > .toolbar-items {
  opacity: 0;
  pointer-events: none;
}
#main-window:not([tabsintitlebar="true"]) #TabsToolbar {
    visibility: collapse !important;
}

#sidebar-box[sidebarcommand="treestyletab_piro_sakura_ne_jp-sidebar-action"] #sidebar-header {
  display: none;
}
```

Most people use Chrome, which so far as I can tell doesn't allow modifying the UI to hide the original tab bar. People have made [Chrome extensions] that supplement the bar with a shortcut-invokable tree [popup], which isn't what I'm used to, but has its own kind of charm. Regardless: consider demanding a better tab experience from your favorite browser. We can do better than The Bar.

---

[treestyletab]: https://addons.mozilla.org/en-US/firefox/addon/tree-style-tab/
[knobs and switches]: https://github.com/nyuutsu/dotfiles/tree/main/nyuu
[SimulBrowse]: https://en.wikipedia.org/wiki/NetCaptor
[Evolt]: https://browsers.evolt.org/
[Chrome extensions]: https://chrome.google.com/webstore/detail/tree-style-tab/oicakdoenlelpjnkoljnaakdofplkgnd?hl=en
[popup]: /media/vertical-space/chrome-tst.png
[Firefox]: https://www.mozilla.org/en-US/firefox/new/