"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *

def jumpin():
    """
    pre-condition: Karel is on the platform which is on the upper-left side of the pothole, facing east
    post-condition:Karel is in the pothole, facing south
    """
    move()
    turn_r()
    move()

def leapout():
    """
        pre-condition: Karel is in the pothole, facing south
        post-condition:Karel is on the platform which is on the upper-left side of the pothole, facing east
    """
    turn_left()
    turn_left()
    move()
    turn_r()
    move()


def main():
    """
    TODO:
    """
    pass
    for i in range(3):
        jumpin()
        putx99()
        leapout()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
