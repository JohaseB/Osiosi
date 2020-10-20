default cash = 0
default sylviePoints = 0
define s = Character("Sylvie")
define week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
define dayTime = ["morning","afternoon","evening","night"]
define actualTime = 4
define actualDay = 7
define displayTextTime = ""

label nextDay:
    $ actualTime += 1

    if actualTime >= 4 :
        $ actualTime = 0
        $ actualDay += 1
    if actualDay >= 7 :
        $ actualDay = 0
    $ displayTextTime = week[ actualDay ] + ", " + dayTime[ actualTime ]
