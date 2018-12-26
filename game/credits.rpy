label credits:
    $ persistent.credits = True
    $ _game_menu_screen = None
    $ _dismiss_pause = False
    $ _skipping = False
    $ _rollback = False
    image splash = "wagu_black.png"
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(5)
    hide theend
    with dissolve
    with Pause(credits_speed - 1)
    show splash:
        yalign .5 subpixel True

        parallel:
            xalign .5
            linear 3.0 xalign .75
            linear 6.0 xalign .25
            linear 3.0 xalign .5
            repeat

        parallel:
            alpha 1.0 zoom 1.0
            linear .75 alpha .5 zoom .9
            linear .75 alpha 1.0 zoom 1.0
            repeat

        parallel:
            rotate 0
            linear 5 rotate 360
            repeat

    with dissolve
    with Pause(10)
    hide splash
    with dissolve
    with Pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve
    return

init python:
    credits = ('Backgrounds', "uncle Mugen's BG {a=https://twitter.com/unclemugen}Twitter{/a}"), ('Backgrounds', '...'), ('Sprites', 'neko-niki  {a=https://www.deviantart.com/neko-niki}Deviantart{/a} {a=https://www.neko-niki.tumblr.com}Tumblr{/a} {a=https://www.twitter.com/nekoniki_}Twitter{/a}'), ('GUI', 'Rifaditya Fadillah'), ('Writing', 'Rifaditya Fadillah'), ('Writing', '...'), ('Programming', 'Rifaditya Fadillah'), ('Music', '...'), ('Music', '...'), ('SFX', 'Pick up by freesfx.co.uk {a=https://www.freesfx.co.uk/Default.aspx} Website {/a}'), ('SFX','Put Down by freesfx.co.uk {a=https://www.freesfx.co.uk/Default.aspx} Website {/a}'), ('SFX','Alarm by "I FORGOT"')
    credits_s = "{size=80}Blury\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()
