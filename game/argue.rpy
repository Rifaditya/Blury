label start_dream:
    $ persistent.play = True
    $ _window_during_transitions = False
    $ renpy.block_rollback()
    $ _window_hide(trans=ccirclewipe)
    scene bg black
    scene room_blink
    pause 1
    play sound_loud alarm
    $ renpy.pause(10, hard=True)
    n1 "Morning alarm [player] just wake up in his bedroom."
    n1 "A sleepy face Looking across the room. lonelyness are the only friend.
    A messy spiky hair like a hegdehog feeling in danger."
    n1 "{i}Seriously I'm still not good with narrator i need to read some novel.{w}
    {p}For real this is suck{/i}"
    player "Ugghh..."
    $ _window_hide(trans=Dissolve(1.5))
    play sound_loud pick_up
    show phone at coming_corner_down_left
    $ renpy.pause(2, hard=True)
    player "Huh?{w} It's already 12:30?"
    player "It's Holiday so i don't have to go to school i guess."
    
    return
label cancel_dream:
    $ persistent.play = True
    $ renpy.block_rollback()
    question1 "Anyone can make mistake you know."
    question "Now there's nothing we can do."
    question1 "There is..."
    question "What?"
    question1 "Put it to the dream machine."
    question "No! We can't."
    question1 "Then just start over."
    return
