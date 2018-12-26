init python:

    def disappear(screen_name):
        renpy.hide_screen(screen_name)
        global available_screens
        available_screens.append(screen_name)

    def allocate_screen(notice_text):
        global available_screens
        global delay_done
        allocated = False
        while not allocated:
            if delay_done and len(available_screens) > 0:
                screen_name = available_screens[0]
                available_screens.remove(screen_name)
                renpy.show_screen(screen_name, notice_text)
                allocated = True
                delay_done = False
            else:
                renpy.pause(delay=0.1)

screen notify1(notice_text):
    frame:
        style "my_style"
        at notice
        text notice_text size 20
    timer 4.0 action Function(disappear, "notify1")
    timer 0.5 action SetVariable("delay_done", True)

screen notify2(notice_text):
    frame:
        style "my_style"
        at notice
        text notice_text size 20
    timer 4.0 action Function(disappear, "notify2")
    timer 0.5 action SetVariable("delay_done", True)

screen notify3(notice_text):
    frame:
        style "my_style"
        at notice
        text notice_text size 20
    timer 4.0 action Function(disappear, "notify3")
    timer 0.5 action SetVariable("delay_done", True)


style my_style:
    background Frame("gui/notify1.png", 10, 10)
    xpadding 9
    ypadding 9


transform notice:
    xalign 1.0 yalign 0.7 alpha 1.0
    linear 3.0 yalign 0.0
    linear 1.0 alpha 0.0
