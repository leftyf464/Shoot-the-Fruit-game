
import pgzrun
import os
from random import randint

apple = Actor("apple")
score = 0
time_remaining = 60 # in seconds

def draw():
    screen.clear()
    apple.draw()
    screen.draw.text(f"Score: {score}", color="white", topleft=(10, 10))
    screen.draw.text(f"Time remaining: {time_remaining}", color="white", topright=(790, 10))

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        print("Good Shooting!")
        place_apple()
        score += 1
        print(score)
    else:
        print("Missed it!")
        if time_remaining > 0:
            score -= 1
        print(score)

def countdown():
    global time_remaining
    time_remaining -= 1
    if time_remaining == 0:
        game_over()

def game_over():
    final_score = score
    print(f"Time's up! Your score is {final_score}")
    screen.draw.text(f"Final Score: {final_score}", color="white", center=(400, 300))
    clock.schedule_unique(close_game_window, 5.0)

def close_game_window():
    exit()

place_apple()
clock.schedule_interval(countdown, 1.0)

pgzrun.go()
