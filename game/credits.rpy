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
        yalign 0.5 xalign 0.5
    with dissolve
    with Pause(3)
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
    credits = ('Backgrounds', "uncle Mugen's BG {a=https://twitter.com/unclemugen}Twitter{/a}"), ('Backgrounds', '...'), ('Sprites', 'neko-niki  {a=https://www.deviantart.com/neko-niki}Deviantart{/a} {a=https://www.neko-niki.tumblr.com}Tumblr{/a} {a=https://www.twitter.com/nekoniki_}Twitter{/a}'), ('GUI', 'Rifaditya Fadillah'), ('Writing', 'Rifaditya Fadillah'), ('Writing', '...'), ('Programming', 'Rifaditya Fadillah'), ('Music', 'Grumblemuck'), ('Music', 'Headwookum')
    credits_s = "{size=80}Blury\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()
