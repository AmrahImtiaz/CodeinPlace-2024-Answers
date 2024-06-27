import random

def roll_dice(num_sides):
    """Simulates rolling a dice with the specified number of sides."""
    return random.randint(1, num_sides)

def main():
    print("Welcome to the Dice Roller!")
    try:
        num_sides = int(input("How many sides does your dice have? "))
        if num_sides <= 0:
            print("Invalid input. Please enter a positive integer.")
            return
        roll_result = roll_dice(num_sides)
        print(f"Your roll is {roll_result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    main()
