title: GIMP stroke/outline text
date: 2023-02-17 00:00
category: notes
tags: GIMP, tutorial

GIMP is sick as hell and is completely free. No fees, no piracy, no wrangling with "cracks" or "activation". GIMP has a lot of rough edges. It has a case of "1990s haphazard overstuffed menus syndrome" and "stuff gets moves around amongst those menus sometimes". I like putting outlines or "strokes" on text & due to my choice of OS and what software I'm familiar with, doing it in GIMP is pretty appealing. But I keep forgetting how, and guides online can be *wrong*; giving instructions to use now-removed menu options.

"GIMP text stroke outline 2023" described below.

<!-- more -->

0. Have a project/canvas to draw on.

1. Use the `text tool` to write some text

    * The text tool is fine for this. As you use it, you might be thinking "this text tool feels really clunky. am I using it wrong?". You aren't using it wrong; that's just what the GIMP text tool is like.

2. Create an outline of the text you just wrote by <kbd>Alt</kbd>[ref]if you have an extremely cool keyboard, this might have a "⎇" symbol on it[/ref]-clicking on the layer preview

    * Identify the layers panel
    
    * In the entry for the text layer, there is a zone for a "graphical preview" of the layer. Text layers don't get a real preview; they just get a placeholder graphic of the letter `A`. You're looking for one of those - for the `Graphical Preview` of the text layer.
    
    * Hold <kbd>Alt</kbd>, then click on text's "`Graphical Preview`" (that is: the placeholder `A`)

    * There should now be a dashed line outlining the text. The dashed line represents a "selection". You've created "a selection that is an exact copy of the text".

3. `Select` menu ⇒ `Grow`; `Grow` the selection by any amount

    * Enter any amount. Most of mine use 1, 2, or 3px.

    * Your selection is now a transformation of the original one: you've expanded it in all directions by whatever amount you chose. This will form the outline.

4. Create a layer to store the outline on. Put this new layer *under* the text layer. Switch to the new layer.

5. Set the foreground or background color to your desired outline color

    * You could use a pattern instead of a color, in which case you don't need to set either of these.

6. `Edit` menu ⇒ `Fill with FG Color` or `Fill with BG Color`

    * This fills the selection you created. The parts of the selection that aren't shadowed by the text form your outline

Now you're done! If you like, you can `Merge Down` the text layer to combine it with the outline layer. This will make it practical to move the text around while mantaining its outline. It won't be editable via the text editor.[ref]So, part of the `Merge Down` is GIMP running `Discard Text Information` on the text layer.[/ref] It will be editable via the other gimp tools: selecting and cutting, erasing, drawing, stamps, filters, and more.