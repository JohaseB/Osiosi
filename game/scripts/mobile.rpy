screen mobile():
    imagebutton:
        align (1.0, 0.5)
        idle "mobile_idle"
        hover "mobile_hover"
        action Hide("say"), Show("displayShowMobile")

screen displayShowMobile():
    imagemap:
        idle "mobile_iscreen"
        hover "mobile_hscreen"
        hotspot(476, 98, 76, 81) action Hide("say"), Show("screenStats")
        hotspot(592, 614, 96, 35) action Hide("displayShowMobile")

screen screenStats():
        imagemap:
            idle "stats_idle"
            hover "stats_hover"
            hotspot(588, 611, 102, 41) action Hide("screenStats")
