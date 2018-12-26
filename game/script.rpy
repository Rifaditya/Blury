label call_naming:

    call screen input_player_name(name_action=Function(FinishName))

    if pname == "":
        "Please give your character a name that is between 2-20's characters long."
        jump call_naming
    if pname is not None:
        $ check_name = len(pname)
        if check_name == 1:
            "You must name your character a minimum of 2 letters."
            jump call_naming

    return
label start:

    python:

        gen = GENERATOR()
        gen1 = GENERATOR1()

    $ gen.malename()
    $ gen1.femalename()

    if persistent.play == True:
        jump start_dream
    if persistent.play == False:
        call screen input_player_name(name_action=Function(FinishName))

    if pname == "":
        "Please give your character a name that is between 2-20's characters long."
        call call_naming
    if pname is not None:
        $ check_name = len(pname)
        if check_name == 1:
            "You must name your character a minimum of 2 letters."
            jump call_naming

    $ _window_during_transitions = True
    scene bg black
    $ allocate_screen("Name It!")

    n1 "Dark room. A dark room no one can see."
    n1 "There'two people in that dark room, and they are the only one can see there."
    question1 "Hmmmm... shaa shhh shssa tch."
    n1 "rubbing his chin while muttering something."
    n1 "came a question from the second person"
    question "What is it?"
    n1 "A long pause from him, the he turn his head toward the second person."
    question1 "Nothing."
    n1 "Ok... I'm too lazy to narrator everything here."
    questions "What?!"
    extend "thats your job!"
    n1 "Ok Ok"
    n1 "The second guy, he feel concerned about it. so he ask."
    question "Is it fail again?"
    n1 "The other guy answer with a very calm tune of his"
    question1"No. It's not, "
    extend "but it seems i make a mistake."
    n1 "Ok i quit just let the animations do the works I'm not good with narrations..."
    questions "Whatever man."
    question "What?! "
    extend "Again?"
    question1 "Yeah.."
    question1 "Lets just put him into a generated dream."

    $ renpy.block_rollback()

    menu:
        "Should we?"
        "Yes":
            question "It's better than nothing"
            $ _window_hide(trans=ccirclewipe)
            jump start_dream #file argue
        "No":
            question "NO! Why you make a mistake in the first place!?"
            jump cancel_dream #file argue

    return
