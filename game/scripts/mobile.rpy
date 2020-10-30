screen mobile():
    imagebutton:
        align (1.0, 0.5)
        idle "mobile_idle"
        hover "mobile_hover"
        action Show("displayShowMobile")


screen displayShowMobile():
    imagemap:
        idle "mobile_iscreen"
        hover "mobile_hscreen"
        hotspot(592, 614, 96, 35) action Hide("displayShowMobile")
