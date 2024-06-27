from karel.stanfordkarel import *

# Function to move Karel to the beeper
def move_to_package():
    move()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
# Function to return Karel to the starting point
def return_home():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
    move()
    turn_left()
    turn_left()
# Main function
def main():
    move_to_package()
    pick_beeper()
    return_home()

if __name__ == '__main__':
    main()
