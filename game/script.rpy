include "scripts/globalvars.rpy"

label start:
    call intro
    call inicio
    call firstmeet_ai
    call nextDay
    show screen cash_screen()
    show screen clock_screen()
    show screen buttonMapGo()
    show screen mobile()

    call hotelRoom
