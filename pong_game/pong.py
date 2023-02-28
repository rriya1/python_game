# 2 parts of the game. one setup part and one loop. setup has logic and data. loop gives movement
import pygame, sys

#1. general setup
#these lines are important for the general setup
# pygame.init() initiates all the pygame modules and is required to run any pygame code
pygame.init() 
clock=pygame.time.Clock()

#2. setting up the main window
screen_width=640
screen_height=480
#returns a display surface object
screen=pygame.display.set_mode((screen_width,screen_height)) 
#this line is to give the window a title
pygame.display.set_caption('Pong')

#4. setting a rectangle for the ball.
#this function gives the width and the height of the rectangle with its x and y positions.
#x and y positions are at the top left corner of a rectangle and origin of the window is at top left corner of display surface.
#thse 3 are empty rectangles. to draw them we will use a loop and pygame.draw()
ball= pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)#ball is 30x30 in dimensions with positioned at the center
player=pygame.Rect(screen_width-20,screen_height/2-70,10,140)#10x140 pixel rectangle at the right middle of the screen
opponent= pygame.Rect(10,screen_height/2-70,10,140)#rectangle for opponent

#3. loop
#this loop will check if the user has pressed the close button at the top of the window
#this  while loop is for updating the game
while True:
    #handling input
    #at every cycle of this loop pygame calls all user events
    #pygame.event.get calls all user events (click of a button, moving mouse, closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user clicked x button that closes game
            #both of these commands combined close the game reliably
            pygame.quit() #uninitialyze the pygame module
            sys.exit() #will close the entire program

        #4. updating the window
        pygame.display.flip() #draw picture from everything that came before the loop, will drawa black screen for now
        #the clock line will limit how fast the loop runs
        #the computer tries to run the loop as fast it can, if we dont control the speed it might even run the loop at 10K frames per second
        clock.tick(60) #60 frames per second.


