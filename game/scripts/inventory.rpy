screen inventory_button():
    imagebutton:
        align (0.0, 0.3)
        idle "bag_idle"
        hover "bag_hover"
        action Hide("say"), Show("inventory_screen")

screen inventory_screen():
    add "inventory.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    #use battle_frame(char=player, position=(.97,.20)) # we show characters stats (mp, hp) on the inv. screen
    #use battle_frame(char=dog, position=(.97,.50))
    hbox align (.95,.04) spacing 20:
        imagebutton:
            idle "close" 
            hover "close" 
            action  Hide("inventory_screen"), Show("inventory_button")
