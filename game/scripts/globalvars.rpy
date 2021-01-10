default cash = 0
default sylviePoints = 0
define s = Character("Sylvie")
define e = Character("Eileen")
define j = Character("joe")
define i = Character("??")
define week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
define dayTime = ["morning","afternoon","evening","night"]
define actualTime = 4
define actualDay = 7
define displayTextTime = ""
define strength = 0
define dexterity = 0
define intellect = 0
define charisma = 0

screen cash_screen():
    frame:
        align(1.0, 0.0)
        text "Dinero : [cash]"
screen clock_screen():
    frame:
        align(0.5, 0.0)
        text "Fecha : [displayTextTime]"

label nextDay:
    $ actualTime += 1

    if actualTime >= 4 :
        $ actualTime = 0
        $ actualDay += 1
    if actualDay >= 7 :
        $ actualDay = 0
    $ displayTextTime = week[ actualDay ] + ", " + dayTime[ actualTime ]
