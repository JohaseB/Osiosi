screen mobile():
    imagebutton:
        align (1.0, 0.5)
        idle "mobile_idle"
        hover "mobile_hover"
        action Show("displayShowMobile")


screen displayShowMobile():
    imagemap:
        idle "sylvie_screen"
        hotspot(668, 457, 90, 68) action renpy.hide_screen("displayShowMobile")
