############# SPECIAL SPEAKING QUIRKS ############

##jumpsec######## billcount ################

init -1 python:

    def tspk(what, amt=0, stmt=None, **kwargs):

        tagora(what, **kwargs)

        global amount
        amount = amt

        global bill

        portion = int(amt/10)

        if amt != 0:

            renpy.hide_screen("moneyadd", layer=None)
            renpy.show_screen("moneyadd", moneyadded=amt)

        if stmt != None:

            renpy.hide_screen("moneystmt", layer=None)
            renpy.show_screen("moneystmt", statement=stmt)

        i = 10

        while i > 0:

            renpy.pause(0.02)

            bill += portion
            amt -= portion

            i -= 1

##jumpsec######## footnotes ################

    def show_footnote(note):

        renpy.show_screen("footnote", fndict[note], _layer="screens", _transient=False)
        renpy.restart_interaction()

define config.hyperlink_handlers = { 'footnote' : show_footnote }

##############  CHARACTERS  ######################

define narrator = Character(window_background="gui/textbox/textbox_narration.png", what_font='font/courbd.ttf', what_size=22,  color='#000000', what_color='#000000')
define op = Character(window_background="gui/textbox/textbox_blank.png", what_font='font/courbd.ttf', what_size=28,  color='#FFFFFF', what_color='#FFFFFF', what_xalign=0.5, what_text_align=0.5)

define tagora = Character("TAGORA", color='#FFFFFF', image="tagora", window_background="gui/textbox/textbox_teal.png", who_outlines=[ (4, "#008282") ],)
define galekh = Character("GALEKH", color='#FFFFFF', image="galekh", window_background="gui/textbox/textbox_blue.png", who_outlines=[ (4, "#005682") ],)
define lynera = Character("LYNERA", color='#FFFFFF', image="lynera", window_background="gui/textbox/textbox_jade.png", who_outlines=[ (4, "#0aa85b") ],)

##############  IMAGES  ######################

# Example character sprites
image tagora ew = Image("images/sprites/tagora/Tagora_Ew.png", ypos=730, xanchor=640, yanchor=720)
image tagora neutral = Image("images/sprites/tagora/Tagora_Neutral.png", ypos=730, xanchor=640, yanchor=720)
# image tagora clasp = Image("images/sprites/tagora/Tagora_Clasp.png", ypos=730, xanchor=640, yanchor=720)
# image tagora doc = Image("images/sprites/tagora/Tagora_Document.png", ypos=730, xanchor=640, yanchor=720)
# image tagora help = Image("images/sprites/tagora/Tagora_Helpful.png", ypos=730, xanchor=640, yanchor=720)
# image tagora mad = Image("images/sprites/tagora/Tagora_Hollering.png", ypos=730, xanchor=640, yanchor=720)
# image tagora judge = Image("images/sprites/tagora/Tagora_Judging.png", ypos=730, xanchor=640, yanchor=720)
# image tagora nervous = Image("images/sprites/tagora/Tagora_Nervous.png", ypos=730, xanchor=640, yanchor=720)
# image tagora neutral2 = Image("images/sprites/tagora/Tagora_Neutral2.png", ypos=730, xanchor=640, yanchor=720)

#############  BACKGROUNDS  ##################
image bg tagora_int = "images/bgs/tagorainterior.png"
image bg tagora_ext = "images/bgs/tagoraexterior.png"

############### ENDINGS ########################
image sample_ending = "images/bgs/ending.jpg"

################# MISC IMAGES #################
# tagora's money
image money = "images/-money/cashmoney.png"

# lynera's knives
image knife0 = Image("images/-knife/knifemeter.png")
image knife1 = Image("images/-knife/knifemeter1.png")
image knife2 = Image("images/-knife/knifemeter2.png")
image knife3 = Image("images/-knife/knifemeter3.png")
image knife4 = Image("images/-knife/knifemeter4.png")
image knife5 = Image("images/-knife/knifemeter5.png")

## COMMON TRANSFORMS ##
#these are all transforms to make your sprite bounce around a little! it's super useful for making your game more dynamic

transform bounce:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform nod:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730

transform twitch:
    ypos 730 xpos 640
    easein 0.06 ypos 736 xpos 644
    linear 0.06 ypos 730 xpos 640

transform shudder:
    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat 4

transform lowered:
    ypos 730
    linear 0.75 ypos 765

transform bouncing:
    ypos 730
    linear 0.1 ypos 720
    linear 0.1 ypos 730
    repeat

transform shaking:
    ypos 730
    linear 0.07 ypos 732
    linear 0.07 ypos 730
    repeat

transform shuddering:
    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat

transform speaking:
    easein 0.1 zoom 1.01

transform stopspeaking:
    easein 0.1 zoom 1

transform shoveright:
    linear 0.1 xpos 960

transform shoveleft:
    xpos 640
    linear 0.1 xpos 320

transform shovecenter:
    linear 0.1 xpos 640

transform shoveoffleft:
    linear 0.1 xpos -320

transform moneybounce:
    parallel:
        alpha 0.0
        linear 0.1 alpha 1.0
        pause 1.8
        easeout 2.0 alpha 0.0
    parallel:
        xpos 910 ypos 80
        easein 1 ypos 65
        pause 1.8
        easeout 1 ypos 80

transform statementbounce:
    parallel:
        alpha 0.0
        linear 0.1 alpha 1.0
        pause 1.8
        easeout 2 alpha 0.0
    parallel:
        xpos 910 ypos 110
        easein 1 ypos 95
        pause 1.8
        easeout 1 ypos 110

#Quickly push sprite to default position, from offscreen bottom
transform shoveup:
    xpos 640 ypos 1440
    linear 0.1 ypos 730

# title menu options move
transform menumove:
    xpos 20
    on hover:
        linear .25 xpos 50
    on idle:
        linear .25 xpos 20

# title logo wiggle
transform wiggle:
    rotate 0
    ypos -250
    on hover:
        linear .1 rotate -2
        linear .1 rotate 0
        linear .1 rotate 2
        linear .1 rotate 0
