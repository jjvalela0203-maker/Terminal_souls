import random
import config


def generar_dano(minimo, maximo):
    return random.randint(minimo, maximo)

def mostrar_estado(nombre_h, hp_h, nombre_e, hp_e):
    print("\n--- ESTADO ACTUAL ---")
    print(f"{nombre_h}: {hp_h} HP")
    print(f"{nombre_e}: {hp_e} HP")
    print("---------------------\n")

def turno_jugador(hp_enemigo, pociones, hp_heroe):
    print("1. Atacar")
    print("2. Curar")
    print("3. Habilidad Especial")

    opcion = input("Elige una acción: ")

    if opcion == "1":
        daño = generar_dano(config.DAÑO_HEROE_MIN, config.DAÑO_HEROE_MAX)
        hp_enemigo -= daño
        print(f"¡Atacaste e hiciste {daño} de daño!")

    elif opcion == "2":
        if pociones > 0:
            hp_heroe += config.CURACION
            pociones -= 1
            print("Te curaste 20 HP")
        else:
            print("No tienes pociones")
            return hp_enemigo, pociones, hp_heroe, False  # NO pierde turno