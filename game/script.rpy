# The game starts here, but you probably won't have to edit anything until the script stuff below
label start:

    # this just sets the colour of the pick option
    $ pick = "{color=#000000}>{/color}"

    # this makes the mini menu not visible
    $ quick_menu = False

    # If you want to have multiple volumes, just add more of these, and then update the screens.rpy accordingly
    $ volume1 = True
    $ volume2 = True

    jump start2

label start2:

    stop music fadeout 1.5

    show image "gui/main_menu.png"

    window hide

    scene black with Dissolve(1.5)

    $ main_menu = True

    # Use this if you want to jump to the screen with 2 trolls.
    call screen vol_select()

    # Use this if you don't want to go to the volume select screen but instead just wanna go straight to startVolume
    # jump startVolume

    stop music fadeout 1.5

##################################################################
########## THIS IS THE SCRIPT STUFF YOU HAVE TO EDIT #############
##################################################################

label startVolumeOne:

    $ renpy.block_rollback()

    $ main_menu = False

    $ quick_menu = True

    show image "gui/game_menu.png"

    window hide

    scene black with Dissolve(1.5)

    ### This is where friendsim starts ###

    op "Initial text."

    call screen troll_select1

    with Pause(0.25)

    return

label trollOne:

    # Don't worry about this stuff!
    $ renpy.block_rollback()
    $ main_menu = False

    # initialise tagora's starting bill as 0
    $ bill = 0
    # initialise tagora's quirk so you can use it again without typing it out. you can see this as [tdone] at the end of his lines
    $ tdone = "\n\n*__________"
    # Initialise galekh's footnotes
    $ fndict = dict(
    note1="1 This is a sample footnote, like the kind galekh uses.\nAnd you can click this too.{a=footnote:note2}{b}¹{/b}{/a}",
    note2="1 This is a footnote inside a footnote.",
    note3="1 Another footnote.",
    )

    show image "gui/game_menu.png"

    window hide

    # Here is where the friendsim volume really starts
    scene black with Dissolve(1.5)

    op "Right now the screen is black and this text by the speaker is being shown."

    op "Once the person clicks, they get to this new speaking line. Now let's go to Tagora's house."

    scene bg tagora_int with dissolve

    $ quick_menu = True

    narrator "Oh look it's the best friendsim character."

    play music "music/sample.mp3" loop

    show tagora neutral with moveinbottom

    show screen billcount

    "Which is Tagora of course."

    tagora "..."

    show tagora ew at shudder

    tagora "Why am I in another friendsim tutorial."

    tspk "Get out of my house." (amt = 5000, stmt="They aren't even paying me for this")

    show bg tagora_ext with CropMove(1.0, "wipeleft")

    show tagora ew at shoveleft

    galekh "Here is an example of how the footnotes work.{a=footnote:note1}{b}¹{/b}{/a} Example 2.{a=footnote:note3}{b}²{/b}{/a}"

    hide screen billcount

    show knife0

    lynera "-this is me speaking to show you how my knife quirk works"

    hide knife0

    show knife5

    lynera "-notice that I had to !!! hide !!! Gor-gor's billcount screen to show my knives. you'll have to take this into consideration when you make your friendsims!"

    hide knife5

    show knife3

    lynera "-or maybe you can find a workaround if you put in the effort probably"

    menu:
        "This is a menu?"

        "[pick] Yes and this is an option":

            show tagora ew at bounce

            tspk "Please leave my house. [tdone]" (amt = 420)

            "Guess that's all we have time for. Hopefully this is an adequate example script!"

            $ renpy.pause(0.5)

            $ quick_menu = False

            play music "music/game_over.mp3" fadeout 1.0 noloop

            scene sample_ending with Dissolve(1.0)

            $ renpy.pause()

            stop music fadeout 1.0

            scene black with Dissolve(1.0)

            return

        "[pick] Nice":

            show tagora neutral at shovecenter

            tspk "Nice." (amt = 69, stmt="Nice")

            $ quick_menu = False

            play music "music/victory_jingle.mp3" fadeout 1.0 noloop

            scene sample_ending with Dissolve(1.0)

            $ renpy.pause()

            stop music fadeout 1.0

            scene black with Dissolve(1.0)

            return

label trollTwo:

    $ renpy.block_rollback()

    $ main_menu = False

    show image "gui/game_menu.png"

    window hide

    scene black with Dissolve(1.5)

    op "You could put the script for a second volume here."

label startVolumeTwo:

    $ renpy.block_rollback()

    $ main_menu = False

    $ quick_menu = True

    show image "gui/game_menu.png"

    window hide

    scene black with Dissolve(1.5)

    ### This is where friendsim starts ###

    op "This one doesn't jump to the troll select screen; instead, the volume starts straight away."

    op "If you look at the screens.rpy, you can see troll_select2 is commented out because it's not needed as there is no trollThree or trollFour label in this file"

    op "You can add those if you wish!"

    return
