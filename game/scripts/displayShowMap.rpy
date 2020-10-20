screen buttonMapGo():
    frame:
        align(0.0, 0.0)
        button:
            action Jump("displayShowMap")
            text "MAP" style "button_text"

label displayShowMap:
    screen showMap():
        imagemap:
            idle "imagemap ground"
            hover "imagemap hover"

            hotspot (44, 238, 93, 93) action Jump("hotel") alt "hotel"
            hotspot (360, 62, 93, 93) action Jump("work") alt "work"

    label showMap:
        call screen showMap

    label hotel:
        jump hotelRoom

    label work:
        jump workplace
