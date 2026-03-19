"""
File: funciones.py

Description:
This module contains all the core functions used in the "Terminal Souls" game.
It handles the main mechanics of the turn-based combat system between the hero 
and the enemy.

The functions defined here are responsible for:
- Generating random damage values
- Displaying the current game state
- Managing the player's turn and actions
- Simulating the enemy's behavior
- Checking win/lose conditions

Authors: Juan Jose Varela and Carlos Aponte"""



import random
import config


def generar_dano(minimo, maximo):
    """
    Generates a random damage value between a minimum and maximum range.
    """
    return random.randint(minimo, maximo)

def mostrar_estado(nombre_h, hp_h, nombre_e, hp_e):
    """
    Displays the current health points (HP) of both the hero and the enemy.
    """
    print("\n--- CURRENT STATUS ---")
    print(f"{nombre_h}: {hp_h} HP")
    print(f"{nombre_e}: {hp_e} HP")
    print("---------------------\n")

def turno_jugador(hp_enemigo, pociones, hp_heroe):
    """
    Handles the player's turn.
    
    The player can choose between:
    1. Attack
    2. Heal
    3. Special ability

    Returns updated values of:
    - Enemy HP
    - Remaining potions
    - Hero HP
    - A boolean indicating if the turn was valid
    """

    print("1. Attack")
    print("2. Heal")
    print("3. Ultimate")

    opcion = input("Choose an action: ")

    # Option 1: Normal attack
    if opcion == "1":
        daño = generar_dano(config.DAÑO_HEROE_MIN, config.DAÑO_HEROE_MAX)
        hp_enemigo -= daño
        print(f"You attacked and dealt {daño} damage!")
    # Option 2: Heal
    elif opcion == "2":
        if pociones > 0:
            hp_heroe += config.CURACION
            pociones -= 1
            print("You healed 20 HP")
            print(f"You have {pociones} potions")
        else:
            print("No potions left")
            return hp_enemigo, pociones, hp_heroe, False
    # Option 3: Special ability (50% chance to fail)
    elif opcion == "3":
        if random.random() < 0.5:
            daño = generar_dano(config.DAÑO_ESPECIAL_MIN, config.DAÑO_ESPECIAL_MAX)
            hp_enemigo -= daño
            print(f"Special attack successful! {daño} damage")
        else:
            print("You fail the ultimate ")
    # Invalid option
    else:
        print("Invalid option")
        return hp_enemigo, pociones, hp_heroe, False

    return hp_enemigo, pociones, hp_heroe, True


def turno_enemigo(hp_heroe):
    """
    Handles the enemy's turn.
    
    The enemy automatically attacks the hero and deals random damage.
    
    Returns updated hero HP.
    """
    daño = generar_dano(config.DAÑO_ENEMIGO_MIN, config.DAÑO_ENEMIGO_MAX)
    hp_heroe -= daño
    print(f"The enemy dealt {daño} damage ")
    return hp_heroe


def verificar_ganador(hp_h, hp_e):
    """
    Checks if the game has ended.
    
    Returns True if either the hero or the enemy has 0 or less HP.
    """
    return hp_h <= 0 or hp_e <= 0
