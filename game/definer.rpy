init python:
    renpy.music.register_channel("sound_loud", mixer="sfx", loop=False)
    renpy.music.set_volume(1, delay=0, channel='sound_loud')
init -1 python:

    def say_blocking(): #allow dismissing only if can_cont
            global can_cont
            return can_cont
    config.say_allow_dismiss = say_blocking

    def no_inter(event, **kwargs):
        global can_cont
        if event == "show" or event == "begin":
            can_cont = False
        if event == "slow_done" or event == "end":
            can_cont = True
            renpy.restart_interaction()
init -2:
    define pname = ""
    default persistent.play = False
    default delay_done = True
    default can_cont = True
    default persistent.warning = True
    image warning:
        "warning.png"
        size(1280, 720)
init -3:
    define persistent.pname = ""
init:
    transform my_pos:
        yanchor -1 yalign -1
        xanchor .5 xalign .5
    transform transform_logo:
        on show:
            alpha 0 xalign 0.5 yalign 0.5
            linear 1.5 alpha 1
        on hide:
            linear .9 alpha 0
    transform transform_white:
        on show:
            alpha 0
            linear 2.0 alpha 1
        on hide:
            linear 2.0 alpha 0
    transform coming_corner_down_left:
        on show:
            xalign 0.0 yalign 1.0
            zoom 0
            linear 2.0 zoom 1 xalign 0.5 yalign 0.5

        on hide:
            xalign 0.5 yalign 0.5
            zoom 1
            linear 2.0 zoom 0 xalign 0.0 yalign 1.0

    define slow_dissolve = Dissolve(3.0)
    define eyeseffect = Image("eyeopen.png")
    define eye_open = ImageDissolve( eyeseffect, 1.5, 100)
    define eye_shut = ImageDissolve( eyeseffect, 1.5, 100, reverse=True)
    define bgtext = Image("gui/textbox_noname.png", xalign=0.5, yalign=1.0,)
    define shatter = ImageDissolve("wipes/shatter.png", 1.0, 8)
    define ccirclewipe = ImageDissolve("wipes/circlewipe-ccw.jpg", 1.0, 8)
    define audio.mallmusic = "musics/music/m4.ogg"
    image splash = "wagu_white.png"
    image bg black = "#000000"
    image white = "#ffffff"
    image logo = "wagu_white.png"
    image logo1 = "wagu_black.png"
    image phone = "phone_screenshot.jpg"
    define audio.alarm = "musics/sfx/alarm.mp3"
    define audio.pick_up = "musics/sfx/pick_up.mp3"
    define audio.put_down = "musics/sfx/put_down.mp3"
init 1:
    image room:
        "room_morning_light_off.jpg"
        size(1280, 720)

    image room_blink:
        "#000" with eye_shut
        1.5
        "room_morning_light_off.jpg" with eye_open
        size(1280, 720)
        2
        "#000" with eye_shut
        size(1280, 720)
        2
        "room_morning_light_off.jpg" with eye_open
        size(1280, 720)
        2
        "#000" with eye_shut
        size(1280, 720)
        2
        "room_morning_light_off.jpg" with eye_open
        size(1280, 720)
    image room_blink_continue:
        "#000" with eye_shut
        1.5
        "room_morning_light_off.jpg" with eye_open
        size(1280, 720)
        2
        "#000" with eye_shut
        size(1280, 720)
        2
        "room_morning_light_off.jpg" with eye_open
        size(1280, 720)
        2
        "#000" with eye_shut
        size(1280, 720)
        2
        "room_morning_light_off.jpg" with eye_open
        size(1280, 720)
        repeat
    image ctc_blink:
        "arrow.png"
        linear 0.75 alpha 1.0
        linear 0.75 alpha 0.0
        repeat

    define maya = Character(_('Maya'),
        color="#ff69b4",
        what_slow_abortable=False,
        callback=no_inter,
        ctc="ctc_blink",
        ctc_position="nestled")
    define n1 = Character(None,
        ctc="ctc_blink",
        ctc_position="nestled",)
    define player = DynamicCharacter("persistent.pname",
        color="#4286f4",
        ctc="ctc_blink",
        ctc_position="nestled")
    define question = Character("???",
        who_color="#009178",
        ctc="ctc_blink",
        ctc_position="nestled")
    define question1 = Character("???",
        who_color="#001891",
        ctc="ctc_blink",
        ctc_position="nestled")
    define questions = Character("{color=#001891}???{/color}{color=#000} & {/color}{color=#009178}???{/color}",
        ctc="ctc_blink",
        ctc_position="nestled")
