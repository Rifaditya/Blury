label start_dream:
    $ renpy.block_rollback()
    $ _window_hide(trans=ccirclewipe)
    scene bg black
    play sound_loud alarm
    scene room_blink
    $ renpy.pause(12, hard=True)
    player "Uggh..."
    player "What?"
    return
label cancel_dream:
    $ renpy.block_rollback()
    quesion1 "Anyone can make mistake you know."
    question "Now there's nothing we can do."
    question1 "There is..."
    question "What?"
    question1 "Put it to the dream machine."
    question "No! We can't."
    question1 "Then just start over."
    return
