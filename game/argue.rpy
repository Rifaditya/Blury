label start_dream:
    $ _window_during_transitions = False
    $ renpy.block_rollback()
    $ _window_hide(trans=ccirclewipe)
    scene bg black
    scene room_blink
    pause 1
    play sound_loud alarm
    $ renpy.pause(10, hard=True)
    player "Test"
    return
label cancel_dream:
    $ renpy.block_rollback()
    question1 "Anyone can make mistake you know."
    question "Now there's nothing we can do."
    question1 "There is..."
    question "What?"
    question1 "Put it to the dream machine."
    question "No! We can't."
    question1 "Then just start over."
    return
