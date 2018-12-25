init:
    
    default _list = ["McCartney", "Lennon", "Harrison", "Starr", "Paul", "John", "George", "Ringo"]
    default persistent.pname = ""
init python:
    def FinishGuess():
        persistent.pname = pname
screen input_name(Put_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _("Whats Your Name?"):
                style "confirm_prompt"
                xalign 0.5
            input default "None" value VariableInputValue("pname") length 20 allow " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Name It!") action Return()
