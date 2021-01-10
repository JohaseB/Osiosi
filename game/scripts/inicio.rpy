label inicio:

    #(escena, calle de la ciudad) 
    "Necesito un lugar donde descansar pero para eso necesito dinero…Puede que en este lugar 
    pueda encontrar un trabajo"

    #(escena, restaurante)
    "Este parece un buen sitio, preguntare si necesitan ayuda..."

    #Aquí el jugador ya puede ver el escenario y hacer click en el personaje
    # El primer personaje con el que se interactúe será nix 

    #(escena, nix)
    i "Bienvenido, ¿Qué quieres comer ? "
    j "Hola, en realidad busco un lugar donde ganar dinero, hace poco llegue a la ciudad y no tengo nada"
    i "Mmm… Cualquier otro dia te hubiera mandado a la mierda, pero hoy estoy de buen humor, bien... quien nos ayudaba renunció hace unos minutos y hay una vacante, aun asi contratarte no me corresponde, llamaré a la encargada"
    s "Bien… Necesitamos que nos ayudes a limpiar, cualquier pregunta se la haces a nix, tendrás tu pago cuando termines"

    # Aquí la escena termina y el tiempo corre desde temprano hasta la noche
    # El jugador será dejado en la calle y no podrá ingresar al restaurante de nuevo, el hotel será # ubicado en otra calle a la que se podrá acceder desde la actual 
    # Deberá ingresar al hotel y pedir una habitación 

    #Has ganado 15 monedas, puedes volver a trabajar aquí mañana, en cualquier hora distinta a la nocturna. 

    #(escena, recepción hotel)
    e "Bienvenido, tenemos sitios disponibles"
    j "El más barato por favor"
    e "Pagas aqui, despues subes las escaleras y la primera puerta a la izquierda"
    #Has perdido 10 monedas
    j "(Hay una máquina dispensadora ahí… supongo que compraré algo)"
    # Has perdido 5 monedas. 
    # Has obtenido un sandwich

        # Se deberá viajar de las misma forma que en la calle, hacer click en las escaleras y 
    # después en la puerta 

    j "Supongo que esta será mi habitación"
    #(escena, habitacion)
    j "Huele a vomito aquí... pero al menos no dormiré en la calle esta noche, 
    supongo… tengo que buscar la forma de cumplir mis objetivos, por el medio que sea necesario… "
    j "Lo primero será intentar encontrar a las personas correctas, 
    si tan solo tuviera la tarjeta que me robaron al llegar a la ciudad, ya tendría al 
    menos un indicio… lo único que recuerdo es el nombre, industrias munity"
    j "Planean abandonar..." 
    j "Es mi única esperanza… " 
    