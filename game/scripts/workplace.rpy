label workplace:
    scene bg lecturehall with dissolve
    show sylvie green normal with dissolve
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
        call nextDay
        jump sylvie_menu

    label nop:
        "Ok!"
        call nextDay
        jump sylvie_menu
