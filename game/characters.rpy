############# SPECIAL SPEAKING QUIRKS ############

##jumpsec######## billcount ################

init -1 python:

    def tspk(what, amt=0, stmt=None, **kwargs):

        t(what, **kwargs)

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

#this is just to show you what a default character would look like. the colo*Ur is the text colour of the box, not of the textbox ^-^
define daraya = Character("DARAYA", color='#FFFFFF', image="daraya", window_background="gui/textbox/textbox_jade.png", who_outlines=[ (4, "#008141") ],)
define t = Character("TAGORA", color='#FFFFFF', image="tagora", window_background="gui/textbox/textbox_teal.png", who_outlines=[ (4, "#008282") ],)
define g = Character("GALEKH", color='#FFFFFF', image="galekh", window_background="gui/textbox/textbox_blue.png", who_outlines=[ (4, "#005682") ],)

##############  IMAGES  ######################
# Daraya

# Amisia
image amisia pull = Image("images/sprites/amisia/amisia_hairpull.png", ypos=730, xanchor=640, yanchor=720)
image amisia doubt = Image("images/sprites/amisia/amisia_doubt.png", ypos=730, xanchor=640, yanchor=720)
image amisia fingers = Image("images/sprites/amisia/amisia_frame.png", ypos=730, xanchor=640, yanchor=720)
image amisia growl = Image("images/sprites/amisia/amisia_growl.png", ypos=730, xanchor=640, yanchor=720)
image amisia jumping = Image("images/sprites/amisia/amisia_jump.png", ypos=730, xanchor=640, yanchor=720)
image amisia nya = Image("images/sprites/amisia/amisia_nya.png", ypos=730, xanchor=640, yanchor=720)
image amisia ponder = Image("images/sprites/amisia/amisia_ponder.png", ypos=730, xanchor=640, yanchor=720)
image amisia smile = Image("images/sprites/amisia/amisia_smile.png", ypos=730, xanchor=640, yanchor=720)
image amisia happy = Image("images/sprites/amisia/amisia_smile2.png", ypos=730, xanchor=640, yanchor=720)
image amisia smug = Image("images/sprites/amisia/amisia_smug.png", ypos=730, xanchor=640, yanchor=720)
image amisia axe = Image("images/sprites/amisia/amisia_axe.png", ypos=730, xanchor=640, yanchor=720)
image amisia confess = Image("images/sprites/amisia/amisia_confess.png", ypos=730, xanchor=640, yanchor=720)

# Skylla
image skylla anger = Image("images/sprites/skylla/skylla_anger.png", ypos=730, xanchor=640, yanchor=720)
image skylla concern = Image("images/sprites/skylla/skylla_concern.png", ypos=730, xanchor=640, yanchor=720)
image skylla depressed = Image("images/sprites/skylla/skylla_depressed.png", ypos=730, xanchor=640, yanchor=720)
image skylla distress = Image("images/sprites/skylla/skylla_distress.png", ypos=730, xanchor=640, yanchor=720)
image skylla happy = Image("images/sprites/skylla/skylla_happy.png", ypos=730, xanchor=640, yanchor=720)
image skylla kickass = Image("images/sprites/skylla/skylla_kickass.png", ypos=730, xanchor=640, yanchor=720)
image skylla numb = Image("images/sprites/skylla/skylla_numb.png", ypos=730, xanchor=640, yanchor=720)
image skylla numb2 = Image("images/sprites/skylla/skylla_numb2.png", ypos=730, xanchor=640, yanchor=720)
image skylla stand = Image("images/sprites/skylla/skylla_stand.png", ypos=730, xanchor=640, yanchor=720)
image skylla talk = Image("images/sprites/skylla/skylla_talk.png", ypos=730, xanchor=640, yanchor=720)
image skylla upset = Image("images/sprites/skylla/skylla_upset.png", ypos=730, xanchor=640, yanchor=720)

# Polypa
image polypa dejected = Image("images/sprites/polypa/polypa_dejected.png", ypos=730, xanchor=640, yanchor=720)
image polypa neutral = Image("images/sprites/polypa/polypa_neutral.png", ypos=730, xanchor=640, yanchor=720)
image polypa pleased = Image("images/sprites/polypa/polypa_pleased.png", ypos=730, xanchor=640, yanchor=720)
image polypa scuffle = Image("images/sprites/polypa/polypa_scuffle.png", ypos=730, xanchor=640, yanchor=720)
image polypa serious = Image("images/sprites/polypa/polypa_serious.png", ypos=730, xanchor=640, yanchor=720)
image polypa shocked = Image("images/sprites/polypa/polypa_shocked.png", ypos=730, xanchor=640, yanchor=720)

# Zebruh
image zebruh disgust = Image("images/sprites/zebruh/zebruh_disgust.png", ypos=730, xanchor=640, yanchor=720)
image zebruh displeased = Image("images/sprites/zebruh/zebruh_displeased.png", ypos=730, xanchor=640, yanchor=720)
image zebruh excited = Image("images/sprites/zebruh/zebruh_excited.png", ypos=730, xanchor=640, yanchor=720)
image zebruh huh = Image("images/sprites/zebruh/zebruh_huh.png", ypos=730, xanchor=640, yanchor=720)
image zebruh showoff = Image("images/sprites/zebruh/zebruh_showoff.png", ypos=730, xanchor=640, yanchor=720)
image zebruh stand = Image("images/sprites/zebruh/zebruh_stand.png", ypos=730, xanchor=640, yanchor=720)
image zebruh talk = Image("images/sprites/zebruh/zebruh_talk.png", ypos=730, xanchor=640, yanchor=720)
image zebruh upset = Image("images/sprites/zebruh/zebruh_upset.png", ypos=730, xanchor=640, yanchor=720)
image zebruh wink = Image("images/sprites/zebruh/zebruh_wink.png", ypos=730, xanchor=640, yanchor=720)

# Konyyl
image konyyl ask = Image("images/sprites/konyyl/Konyyl_ask.png", ypos=730, xanchor=640, yanchor=720)
image konyyl attack = Image("images/sprites/konyyl/Konyyl_attack.png", ypos=730, xanchor=640, yanchor=720)
image konyyl defeated = Image("images/sprites/konyyl/Konyyl_defeated.png", ypos=730, xanchor=640, yanchor=720)
image konyyl laugh = Image("images/sprites/konyyl/Konyyl_laugh.png", ypos=730, xanchor=640, yanchor=720)
image konyyl menacing = Image("images/sprites/konyyl/Konyyl_menacing.png", ypos=730, xanchor=640, yanchor=720)
image konyyl neutral = Image("images/sprites/konyyl/Konyyl_neutral.png", ypos=730, xanchor=640, yanchor=720)
image konyyl sad = Image("images/sprites/konyyl/Konyyl_sad.png", ypos=730, xanchor=640, yanchor=720)
image konyyl surprised = Image("images/sprites/konyyl/Konyyl_surprised.png", ypos=730, xanchor=640, yanchor=720)
image konyyl thinking = Image("images/sprites/konyyl/Konyyl_thinking.png", ypos=730, xanchor=640, yanchor=720)
image konyyl why = Image("images/sprites/konyyl/Konyyl_why.png", ypos=730, xanchor=640, yanchor=720)

# Tyzias
image tyzias grimace = Image("images/sprites/tyzias/Tyzias_grimace.png", ypos=730, xanchor=640, yanchor=720)
image tyzias irritated = Image("images/sprites/tyzias/Tyzias_irritated.png", ypos=730, xanchor=640, yanchor=720)
image tyzias irritatedtalk = Image("images/sprites/tyzias/Tyzias_irritatedtalk.png", ypos=730, xanchor=640, yanchor=720)
image tyzias laugh = Image("images/sprites/tyzias/Tyzias_laugh.png", ypos=730, xanchor=640, yanchor=720)
image tyzias miserable = Image("images/sprites/tyzias/Tyzias_miserable.png", ypos=730, xanchor=640, yanchor=720)
image tyzias mugglare = Image("images/sprites/tyzias/Tyzias_mugglare.png", ypos=730, xanchor=640, yanchor=720)
image tyzias sad = Image("images/sprites/tyzias/Tyzias_sad.png", ypos=730, xanchor=640, yanchor=720)
image tyzias sip = Image("images/sprites/tyzias/Tyzias_sip.png", ypos=730, xanchor=640, yanchor=720)
image tyzias siplook = Image("images/sprites/tyzias/Tyzias_siplook.png", ypos=730, xanchor=640, yanchor=720)
image tyzias talk = Image("images/sprites/tyzias/Tyzias_talk.png", ypos=730, xanchor=640, yanchor=720)
image tyzias weary = Image("images/sprites/tyzias/Tyzias_weary.png", ypos=730, xanchor=640, yanchor=720)
image tyzias workedup = Image("images/sprites/tyzias/Tyzias_workedup.png", ypos=730, xanchor=640, yanchor=720)
image tyzias workedup2 = Image("images/sprites/tyzias/Tyzias_workedup2.png", ypos=730, xanchor=640, yanchor=720)

# Mallek
image mallek down = Image("images/sprites/mallek/mallek_down.png", ypos=730, xanchor=640, yanchor=720)
image mallek drones = Image("images/sprites/mallek/mallek_drones.png", ypos=730, xanchor=640, yanchor=720)
image mallek grin = Image("images/sprites/mallek/mallek_grin.png", ypos=730, xanchor=640, yanchor=720)
image mallek interest = Image("images/sprites/mallek/mallek_interest.png", ypos=730, xanchor=640, yanchor=720)
image mallek laugh = Image("images/sprites/mallek/mallek_laugh.png", ypos=730, xanchor=640, yanchor=720)
image mallek neutral = Image("images/sprites/mallek/mallek_neutral.png", ypos=730, xanchor=640, yanchor=720)
image mallek pissed = Image("images/sprites/mallek/mallek_pissed.png", ypos=730, xanchor=640, yanchor=720)
image mallek really = Image("images/sprites/mallek/mallek_really.png", ypos=730, xanchor=640, yanchor=720)
image mallek unsure = Image("images/sprites/mallek/mallek_scrutinyannoyance.png", ypos=730, xanchor=640, yanchor=720)

#############  BACKGROUNDS  ##################
image bg mc_hideout = "images/bgs/mc_hideout.png"
image bg alternia3 = "images/bgs/background3.png"

image bg tagora_bath = "images/bgs/tagorabath.png"
image bg tagora_int = "images/bgs/tagorainterior.png"
image bg tagora_ext = "images/bgs/tagoraexterior.png"

################# MISC IMAGES #################
image money = "images/-money/cashmoney.png"

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
