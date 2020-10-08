# The script of the game goes in this file.

default cash = 0
screen cash_screen():
    frame:
        align(1.0, 0.0)
        text "Dinero : [cash]"
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define s = Character("Sylvie")

label start:
    scene bg lecturehall
    with dissolve
    show sylvie green normal
    with dissolve
    show screen cash_screen()
    s"Viniste a trabajar verdad?"

label sylvie_menu:
    menu:
        "Si, vengo a trabajar":
            jump trabajo

        "Nop":
            jump nop

label trabajo:
    $ cash += 10
    "Has  ganado diez monedas!"
    jump sylvie_menu

label nop:
    return
