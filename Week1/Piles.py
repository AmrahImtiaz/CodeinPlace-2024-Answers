from karel.stanfordkarel import *
def pick_up_beepers():
  while front_is_clear():
    if beepers_present():
        for i in range(10):
            pick_beeper()
    move()

def main():
  
  pick_up_beepers()

if __name__ == '__main__':
    main()
