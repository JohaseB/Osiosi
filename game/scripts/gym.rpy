label gym:
    scene bg gym with dissolve
    show eileen concerned with dissolve
    e"Viniste a entrenar pedazo de mierda?"
    label gym_menu:
        menu:
            "Jaja si":
                jump stats_menu

            "Nel prra":
                jump hotelRoom

    label stats_menu:
        e"Elige puto"
        menu:
            "Fuerza":
                jump fuerza

            "Agilidad":
                jump agilidad

            "Inteligencia":
                jump inteligencia

            "Carisma":
                jump carisma

            "Chao":
                jump hotelRoom

    label fuerza:
        "Has subido 1 de fuerza"
        $ strength += 1
        call nextDay
        jump stats_menu

    label agilidad:
        "Has subido 1 de agilidad"
        $ dexterity += 1
        call nextDay
        jump stats_menu

    label inteligencia:
        "Has subido 1 de inteligencia"
        $ intellect += 1
        call nextDay
        jump stats_menu

    label carisma:
        "Has subido 1 de carisma"
        $ charisma += 1
        call nextDay
        jump stats_menu
