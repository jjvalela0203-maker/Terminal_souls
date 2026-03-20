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

Authors: Juan Jose Varela and Carlos Aponte
"""

import random
import config

def generate_damage(minimum, maximum):
    """
    Generates a random damage value between a minimum and maximum range.
    """
    return random.randint(minimum, maximum)


def hero_hp_bar(hero_hp):
    """
    Generates a visual health bar for the hero.

    It calculates the proportion of the hero's current HP relative to
    the maximum HP and represents it using a fixed-size bar composed
    of filled (#) and empty (-) blocks.

    Returns:
    A string representing the hero's health bar.
    """
    size_bar=20
    percent= hero_hp/config.HERO_HP
    blocks= int(percent*size_bar)
    void=size_bar-blocks
    bar_h="#"*blocks + "-"*void
    return bar_h

def enemy_hp_bar(enemy_hp):
    """
    Generates a visual health bar for the enemy.

    It calculates the proportion of the enemy's current HP relative to
    the maximum HP and represents it using a fixed-size bar composed
    of filled (#) and empty (-) blocks.

    Returns:
    A string representing the enemy's health bar.
    """
    size_bar=20
    percent= enemy_hp/config.ENEMY_HP
    blocks= int(percent*size_bar)
    void=size_bar-blocks
    bar_e="#"*blocks + "-"*void
    return bar_e

def show_status(hero_name, hero_hp, enemy_name, enemy_hp):
    """
    Displays the current health points (HP) of both the hero and the enemy.
    """
    print("\n--- CURRENT STATUS ---")
    print(f"{hero_name}: [{hero_hp_bar(hero_hp)}] {hero_hp} HP")
    print(f"{enemy_name}: [{enemy_hp_bar(enemy_hp)}] {enemy_hp} HP")
    print("---------------------\n")


def player_turn(enemy_hp, potions, hero_hp):
    """
    Handles the player's turn.
    """

    print("1. Attack")
    print("2. Heal")
    print("3. Special Ability")

    option = input("Choose an action: ")

    if option == "1":
        damage = generate_damage(config.HERO_DAMAGE_MIN, config.HERO_DAMAGE_MAX)
        enemy_hp -= damage
        print(f"You attacked and dealt {damage} damage!")

    elif option == "2":
        if hero_hp == 100:
            print("You are already at full health")
            return enemy_hp, potions, hero_hp, False
        if potions > 0:
            hero_hp += config.HEAL_AMOUNT
            potions -= 1
            print("You healed 20 HP")
            print(f"You have {potions} potions left")
        else:
            print("No potions left")
            return enemy_hp, potions, hero_hp, False

    elif option == "3":
        if random.random() < 0.5:
            damage = generate_damage(config.SPECIAL_DAMAGE_MIN, config.SPECIAL_DAMAGE_MAX)
            enemy_hp -= damage
            print(f"Special attack successful! {damage} damage")
        else:
            print("Special attack failed")

    else:
        print("Invalid option")
        return enemy_hp, potions, hero_hp, False

    return enemy_hp, potions, hero_hp, True


def enemy_turn(hero_hp):
    """
    Handles the enemy's turn.
    """
    damage = generate_damage(config.ENEMY_DAMAGE_MIN, config.ENEMY_DAMAGE_MAX)
    hero_hp -= damage
    print(f"The enemy dealt {damage} damage")
    return hero_hp


def check_winner(hero_hp, enemy_hp):
    """
    Checks if the game has ended.
    """
    return hero_hp <= 0 or enemy_hp <= 0
