# we have to build our own timers from tools in pygame.
# after initiating pygame, the timer starts to count up miliseconds ans we can measure how much timehas passed since that point.
# we initialize a static point as a point of reference and a current time, the time between these two is the lenth of the timer.
# we only measure the time on every single frame and not every millisecond.
# because of the above point it is not important that we end up at an exact time at every frame. so use > or < to measure time and not = as we might not get the exact time.
# timer starts running when we call pygame.init

import pygame, sys

pygame.init() #initiate pygame
screen= pygame.display.set_mode((640,640)) #creating the screen
clock=pygame.time.Clock() #creating clock

current_time=0 #to measure timer at every frame.
#game loop-->
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time=pygame.time.get_ticks() #to get what millisecond we are right now
    
    pygame.display.flip()
    clock.tick(60) #60 frames per sec
