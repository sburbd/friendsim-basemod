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

#note: to edit the starting labels, you have to go into screens, under trollselect1. there might be some old gunk in there btw.
label trollOne:

    # Don't worry about this stuff!
    $ renpy.block_rollback()

    $ main_menu = False

    $ bill = 0

    $ tdone = "\n\n*__________"

    show image "gui/game_menu.png"

    window hide

    # Here is where the friendsim volume really starts
    scene black with Dissolve(1.5)

    op "Right now the screen is black and this text by the speaker is being shown."

    op "Once the person clicks, they get to this new speaking line. Now let's go to Tagora's house"

    scene bg tagora_int with dissolve

    $ quick_menu = True

    narrator "We are now in Tagora's house."

    play music "music/tagora_theme.mp3" loop

    show robegor neutral with moveinbottom

    show screen billcount

    "And now Tagora has noticed us."

    tspk "..."

    show robegor disgust at shudder

    tspk "Why am I in another friendsim." (amt = 5000, stmt="Unsolicited visitation")

    menu:
        "Well? Why is he in another friendsim?"

        "[pick] I have no idea":

            show robegor disgust at bounce

            tspk "This wasn't in my contract. [tdone]" (amt = 20)

            "You can feel his friendship slipping away."

            hide screen billcount

            $ renpy.pause(0.5)

            $ quick_menu = False

            play music "music/game_over.mp3" fadeout 1.0 noloop

            scene tagora_bad_ending with Dissolve(1.0)

            $ renpy.pause()

            stop music fadeout 1.0

            scene black with Dissolve(1.0)

            return

        "[pick] Banavalope is making a friendsim!":

            show robegor neutral at default

            tspk "Sounds interesting." (amt = 220, stmt="Ego boosted")

            hide screen billcount

            $ quick_menu = False

            play music "music/victory_jingle.mp3" fadeout 1.0 noloop

            scene tagora_good_ending with Dissolve(1.0)

            $ renpy.pause()

            stop music fadeout 1.0

            scene black with Dissolve(1.0)

            return

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
