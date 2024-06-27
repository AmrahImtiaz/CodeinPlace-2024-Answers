from karel.stanfordkarel import *

def main():

# Move to the beeper at (1, 3)
 move()           # Move to (1, 2)
 move()           # Move to (1, 3)
 pick_beeper()    # Pick up the beeper

# Move to the target position (3, 4)
 turn_left()      # Turn left to face north
 move()           # Move to (2, 3)
 turn_left()      # Turn left to face west
 turn_left()
 turn_left()
 move()           # Move to (3, 3)
 turn_left()      # Turn left to face south
 move()           # Move to (3, 4)
 put_beeper()     # Put down the beeper

# Return to the initial position
 turn_left()      # Turn left to face east
 turn_left()
 move()           # Move to (3, 3)
 turn_left()
 turn_left()
 turn_left()
 move()
 move()
 move()
 turn_left()
 move()
 turn_left()

if __name__ == '__main__':
    main()