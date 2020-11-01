include "scripts/globalvars.rpy"

label start:
    call nextDay
    screen cash_screen():
        frame:
            align(1.0, 0.0)
            text "Dinero : [cash]"
    screen clock_screen():
        frame:
            align(0.5, 0.0)
            text "Fecha : [displayTextTime]"
    show screen cash_screen()
    show screen clock_screen()
    show screen buttonMapGo()
    show screen mobile()

    call hotelRoom
