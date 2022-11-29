
import pgzrun
from random import randint

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():

     apple.x = randint(10, 800)
     apple.y = randint(10, 600)


def on_mouse_down(pos):

    if apple.collidepoint(pos):
        
        print("Good Shooting!")
        place_apple()
        score = 0
        print(score + 1)

    else:

        print("Missed it!")
        quit()



place_apple()
pgzrun.go()


 
