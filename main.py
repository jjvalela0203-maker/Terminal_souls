"""
File: main.py

Description:
This is the main entry point of the "Terminal Souls" game.
It controls the game loop, manages the flow of turns between
the player and the enemy, and determines when the game ends.

Authors: Juan Jose Varela and Carlos Aponte
"""

import config
from funciones import *


def main():
    """
    Main function of the program.
    """

    hero_hp = config.HERO_HP
    enemy_hp = config.ENEMY_HP
    potions = config.POTIONS
    turn = 1

    while not check_winner(hero_hp, enemy_hp):
        print(f"\n--- TURN {turn} ---")

        show_status("Hero", hero_hp, "Enemy", enemy_hp)

        enemy_hp, potions, hero_hp, valid_turn = player_turn(
            enemy_hp, potions, hero_hp
        )

        if not valid_turn:
            continue

        if check_winner(hero_hp, enemy_hp):
            break

        hero_hp = enemy_turn(hero_hp)

        turn += 1

    if hero_hp > 0:
        print("🎉 You Win!")
    else:
        print("💀 You Lose...")


if __name__ == "__main__":
    main()
