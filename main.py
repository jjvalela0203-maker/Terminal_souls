"""
File: main.py

Description:
This is the main entry point of the "Terminal Souls" game.
It controls the game loop, manages the flow of turns between
the player and the enemy, and determines when the game ends.

The program repeatedly executes player and enemy turns until
one of them reaches 0 HP. It also displays the current game
status and the final result.

Authors: Juan Jose Varela and Carlos Aponte
"""

import config
from funciones import *


def main():
    # Initialize game variables
    hp_heroe = config.HP_HEROE
    hp_enemigo = config.HP_ENEMIGO
    pociones = config.POCIONES
    turno = 1  # Turn counter

    # Main game loop
    while not verificar_ganador(hp_heroe, hp_enemigo):
        print(f"\n--- TURN {turno} ---")

        # Show current status
        mostrar_estado("Hero", hp_heroe, "Enemy", hp_enemigo)

        # Player turn
        hp_enemigo, pociones, hp_heroe, turno_valido = turno_jugador(
            hp_enemigo, pociones, hp_heroe
        )

        # If the action was invalid, repeat the turn
        if not turno_valido:
            continue

        # Check if the game ended after player's turn
        if verificar_ganador(hp_heroe, hp_enemigo):
            break

        # Enemy turn
        hp_heroe = turno_enemigo(hp_heroe)

        # Increase turn counter
        turno += 1

    # Final result
    if hp_heroe > 0:
        print("🎉 You Win!")
    else:
        print("💀 You Lose...")


# Entry point of the program
if __name__ == "__main__":
    main()
