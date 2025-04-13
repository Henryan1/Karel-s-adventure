"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses seven hurdles with different height in a 12x12 world
    """
    pass
    for i in range(11):
        if front_is_clear():
            move()
        else:
            climb_up()
            land()



def turn_right():
    """
    Pre-condition:Karel is facing a direction
    Post-condition:Karel turns right
    """
    for i in range(3):
        turn_left()


def climb_up():
    """
    Pre-condition:Karel is next to the hurdle
    Post-condition:Karel is on the hurdle
    """
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()


def land():
    """
    Post-condition:Karel is on the hurdle
    Pre-condition:Karel is next to the hurdle
    """
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()






# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
