#Ejercicio 1

print("=== CAJA DEL KIOSCO ===")

# Validar nombre
nombre = input("Nombre del cliente: ")

while nombre == "" or not nombre.isalpha():
    print("Error: ingrese solo letras.")
    nombre = input("Nombre del cliente: ")

# Validar cantidad de productos
cantidad = input("Cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese un número entero positivo.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0

# Cargar productos
for i in range(1, cantidad + 1):

    precio = input(f"Producto {i} - Precio: ")

    while not precio.isdigit():
        print("Error: ingrese un precio válido.")
        precio = input(f"Producto {i} - Precio: ")

    precio = int(precio)

    descuento = input("Descuento (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("Error: ingrese S o N.")
        descuento = input("Descuento (S/N): ").lower()

    total_sin_descuentos += precio

    if descuento == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_con_descuentos += precio_final

ahorro = total_sin_descuentos - total_con_descuentos
promedio = float(total_con_descuentos) / cantidad

print()
print("=== RESULTADO ===")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#ejercicio 2

print("=== ACCESO AL CAMPUS ===")

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and not acceso:
    usuario = input(f"Intento {intentos + 1}/3 - Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

    intentos += 1

if not acceso:
    print("Cuenta bloqueada.")
else:

    opcion = ""

    while opcion != "4":
        print()
        print("1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        if int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
        else:
            if opcion == "1":
                print("Estado: Inscripto")

            elif opcion == "2":
                nueva_clave = input("Nueva clave: ")

                while len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                    nueva_clave = input("Nueva clave: ")

                confirmacion = input("Confirmar nueva clave: ")

                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada correctamente.")
                else:
                    print("Error: las claves no coinciden.")

            elif opcion == "3":
                print("¡Seguí adelante, cada esfuerzo te acerca a tu objetivo!")

            elif opcion == "4":
                print("Sesión finalizada.")


#ejercicio 3

print("=== AGENDA DE TURNOS ===")

# Validar nombre del operador
operador = input("Nombre del operador: ")

while operador == "" or not operador.isalpha():
    print("Error: ingrese solo letras.")
    operador = input("Nombre del operador: ")

# Variables de los turnos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = ""

while opcion != "5":

    print()
    print("=== MENÚ ===")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Opción: ")

    if int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción fuera de rango.")

    elif opcion == "1":

        # Elegir día
        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: seleccione 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente: ")

        while paciente == "" or not paciente.isalpha():
            print("Error: ingrese solo letras.")
            paciente = input("Nombre del paciente: ")

        if dia == "1":

            # Verificar repetido
            if (paciente == lunes1 or paciente == lunes2 or
                    paciente == lunes3 or paciente == lunes4):
                print("Error: el paciente ya tiene un turno ese día.")

            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado: Lunes - Turno 1")

            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado: Lunes - Turno 2")

            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado: Lunes - Turno 3")

            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado: Lunes - Turno 4")

            else:
                print("No hay turnos disponibles para el lunes.")

        else:

            if (paciente == martes1 or paciente == martes2 or
                    paciente == martes3):
                print("Error: el paciente ya tiene un turno ese día.")

            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado: Martes - Turno 1")

            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado: Martes - Turno 2")

            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado: Martes - Turno 3")

            else:
                print("No hay turnos disponibles para el martes.")

    elif opcion == "2":

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: seleccione 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente a cancelar: ")

        while paciente == "" or not paciente.isalpha():
            print("Error: ingrese solo letras.")
            paciente = input("Nombre del paciente a cancelar: ")

        encontrado = False

        if dia == "1":

            if paciente == lunes1:
                lunes1 = ""
                encontrado = True

            elif paciente == lunes2:
                lunes2 = ""
                encontrado = True

            elif paciente == lunes3:
                lunes3 = ""
                encontrado = True

            elif paciente == lunes4:
                lunes4 = ""
                encontrado = True

        else:

            if paciente == martes1:
                martes1 = ""
                encontrado = True

            elif paciente == martes2:
                martes2 = ""
                encontrado = True

            elif paciente == martes3:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado correctamente.")
        else:
            print("No se encontró ese paciente.")

    elif opcion == "3":

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: seleccione 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print()
            print("=== AGENDA DEL LUNES ===")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")

        else:
            print()
            print("=== AGENDA DEL MARTES ===")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")

    elif opcion == "4":

        # Contar ocupados
        ocupados_lunes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        ocupados_martes = 0

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print()
        print("=== RESUMEN GENERAL ===")
        print(f"Lunes: {ocupados_lunes} ocupados, {disponibles_lunes} disponibles.")
        print(f"Martes: {ocupados_martes} ocupados, {disponibles_martes} disponibles.")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Hay empate entre Lunes y Martes.")

print("Sistema cerrado.")


#ejercicio 4

print("=== ESCAPE ROOM: LA BÓVEDA ===")

# Nombre del agente
agente = input("Nombre del agente: ")

while agente == "" or not agente.isalpha():
    print("Error: ingrese solo letras.")
    agente = input("Nombre del agente: ")

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0

print()
print(f"Agente: {agente}")
print("La misión comienza.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

    print()
    print("=== ESTADO ===")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {alarma}")

    print()
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Opción: ")

    while int(opcion) < 1 or int(opcion) > 3:
        print("Error: opción fuera de rango.")
        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

    # OPCIÓN 1
    if opcion == "1":

        forzar_seguidas += 1

        energia -= 20
        tiempo -= 2

        if forzar_seguidas == 3:
            print("La cerradura se trabó.")
            print("¡ALARMA ACTIVADA!")
            alarma = True

        elif energia < 40:
            riesgo = input("Riesgo de alarma. Elija un número del 1 al 3: ")

            while not riesgo.isdigit():
                print("Error: ingrese un número válido.")
                riesgo = input("Riesgo de alarma. Elija un número del 1 al 3: ")

            while int(riesgo) < 1 or int(riesgo) > 3:
                print("Error: el número debe estar entre 1 y 3.")
                riesgo = input("Riesgo de alarma. Elija un número del 1 al 3: ")

                while not riesgo.isdigit():
                    print("Error: ingrese un número válido.")
                    riesgo = input("Riesgo de alarma. Elija un número del 1 al 3: ")

            if riesgo == "3":
                alarma = True
                print("¡ALARMA ACTIVADA!")

            else:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

        else:
            cerraduras_abiertas += 1
            print("¡Cerradura abierta!")

    # OPCIÓN 2
    elif opcion == "2":

        forzar_seguidas = 0

        energia -= 10
        tiempo -= 3

        print("Hackeando panel...")

        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 - Código: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print("¡El código permitió abrir una cerradura!")

    # OPCIÓN 3
    elif opcion == "3":

        forzar_seguidas = 0

        energia += 15

        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            energia -= 10

        print("Has descansado.")
        print(f"Energía actual: {energia}")

    # Bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print()
        print("La alarma bloqueó el sistema.")
        break

# Resultado final
print()
print("=== RESULTADO ===")

if cerraduras_abiertas == 3:
    print("¡VICTORIA! La bóveda fue abierta.")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("DERROTA. El sistema se bloqueó por la alarma.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA. Te quedaste sin energía o tiempo.")
elif alarma:
    print("DERROTA. La alarma fue activada.")

#ejercicio 5

print("--- BIENVENIDO A LA ARENA ---")

# Nombre del gladiador
nombre = input("Nombre del Gladiador: ")

while nombre == "" or not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# Estadísticas iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3

ataque_pesado = 15
danio_enemigo = 12

turno_gladiador = True

print()
print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:

    if turno_gladiador:

        print()
        print(f"{nombre} (HP: {vida_jugador}) vs Enemigo "
              f"(HP: {vida_enemigo}) | Pociones: {pociones}")

        print()
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        while int(opcion) < 1 or int(opcion) > 3:
            print("Error: la opción debe ser 1, 2 o 3.")
            opcion = input("Opción: ")

            while not opcion.isdigit():
                print("Error: Ingrese un número válido.")
                opcion = input("Opción: ")

        # ATAQUE PESADO
        if opcion == "1":

            if vida_enemigo < 20:
                danio = ataque_pesado * 1.5
                print("¡Golpe Crítico!")
            else:
                danio = float(ataque_pesado)

            vida_enemigo -= danio

            print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

        # RÁFAGA VELOZ
        elif opcion == "2":

            print(">> ¡Inicias una ráfaga de golpes!")

            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        # CURAR
        elif opcion == "3":

            if pociones > 0:
                vida_jugador += 30
                pociones -= 1

                print("¡Usaste una poción de vida!")

            else:
                print("¡No quedan pociones!")

        # Verificar si el enemigo sigue vivo
        if vida_enemigo > 0:
            vida_jugador -= danio_enemigo

            print()
            print(">> ¡El enemigo contraataca!")
            print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

        turno_gladiador = True

print()
print("=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
