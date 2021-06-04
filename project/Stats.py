import random


def dice_type(min, max):
    int(min)
    int(max)
    return random.randint(min, max)


# TODO: add in mods from racial passives when chosen.
def ability_roll():
    total = []
    # Simulates rolling 4 1d6 dice
    roll_one = dice_type(1, 6)
    roll_two = dice_type(1, 6)
    roll_three = dice_type(1, 6)
    roll_four = dice_type(1, 6)
    # Places 4 rolls in list and removes lowest before totaling
    total.append(roll_one)
    total.append(roll_two)
    total.append(roll_three)
    total.append(roll_four)
    total.remove(min(total))

    return sum(total)


def hp_roll(char_class):
    if char_class.lower() == "barbarian":
        hit_points = dice_type(1, 12)
    if char_class.lower() == "fighter" or char_class == "paladin" or char_class == "ranger":
        hit_points = dice_type(1, 10)
    if char_class.lower() == "bard" or char_class == "cleric" or char_class == "druid" or char_class == "monk" or char_class == "rogue" or char_class == "warlock":
        hit_points = dice_type(1, 8)
    if char_class.lower() == "sorcerer" or char_class == "wizard":
        hit_points = dice_type(1, 6)

    return hit_points


def strength(race):
    if race == "dragonborn" or race == "half-orc":
        str_total = ability_roll() + 2
    elif race == "human":
        str_total = ability_roll() + 1
    else:
        str_total = ability_roll()
    return str_total


def dexterity(race):
    if race == "elf" or race == "human" or race == "halfling":
        dex_total = ability_roll() + 2
    elif race == "human":
        dex_total = ability_roll() + 1
    else:
        dex_total = ability_roll()
    return dex_total


def constitution(race):
    if race == "dwarf":
        cons_total = ability_roll() + 2
    elif race == "human" or race == "half-orc":
        cons_total = ability_roll() + 1
    else:
        cons_total = ability_roll()
    return cons_total


def intelligence(race):
    if race == "gnome":
        int_total = ability_roll() + 2
    elif race == "human" or race == "tiefling":
        int_total = ability_roll() + 1
    else:
        int_total = ability_roll()
    return int_total


def wisdom(race):
    if race == "human":
        wis_total = ability_roll() + 1
    else:
        wis_total = ability_roll()
    return wis_total


def charisma(race):
    if race == "half-elf" or race == "tiefling":
        char_total = ability_roll() + 2
    elif race == "human" or race == "dragonborn":
        char_total = ability_roll() + 1
    else:
        char_total = ability_roll()
    return char_total
