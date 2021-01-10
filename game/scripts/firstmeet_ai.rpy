label firstmeet_ai:
    "toc toc"
    j"Un momento"
    j "Mi primera noche, y ya vinieron enfermos a fastidiarme"
    j"¿ Quién es? ¿Qué quiere?"
    i "Puedes abrir  ?"
    j"Carajo..."
    i "¿Dijiste algo ? "
    j"No, ya voy"
    #(escena, ai en la puerta)
    j "..."
    i "..."
    
    i "Tienes algo de comer? "
    j "no puedo creer que le pregunte eso a alguien que acabar de llegar al hotel, no tiene sentido de la verguenza quisa?"
    j "(risas)"
    j "............... que haces tu aqui? es ella, no puedo creer que la encontre en este lugar"
    j "No te basto con lo que encontraste en mi maleta justo despues de que me la arrebataste, y ahora quieres mas?"
    i "..... y tu quien eres?, podrias ser?, eres el sujeto de antes"
    j "Si, quiero que me devuelvas mis cosas en este instante, ire con la recepcionista y talvez logre que te saquen del hotel y"
    i"GGGGGGGGGGGGGRRRRRRRRRRRRRRRRRRRRRRRR"
    j"...."
    i"..."

    menu:
        "Alimentarla":
            jump feed

        "Nop":
            jump nop

label feed:
    j "al menos esa parte no era mentira"
    i "....."
    j "pasa, buscare las latas de reserva que conseguí antes de venir aquí"
    j"entonces,.. me vas a contar con que necesidad robaste mis cosas?"
    i "trabajo"
    j "desde cuando robar se considera trabajo"
    i "no lose, solo llevo las cosas de la gente a un lugar, y luego de un tiempo, me dan dinero por ellas"
    j "esta bien no me importara si me ayudas a recuperarla, tengo algo muy importante en mi mochila y lo necesito devuelta"
    i"esta bien, te llevare al lugar, solo deja de quejarte"
    j "‘debo decir que eso ha sido muy facil, de verda me entragara mis cosas que tanto esfuerzo le tomo tomarlas asi como asi?’"
    i "vendrás entonces?, si tardas mucho ire a mi habitacion?"
    j"esta bien alla voy, recuerda que soy yo el que mas desea sus cosas devuelta"
    jump badEnd_one

    # // Aqui estaba pensando soltar al jugador en el mapa para que ocurran 2 cosas, ir a la ubicacion designada por ai o pasear alrededor de la ciudad

    # ir directamente al punto designado
