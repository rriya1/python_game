# 2 parts of the game. one setup part and one loop. setup has logic and data. loop gives movement
import pygame, sys, random

#15. restarting the game when the ball hits the left or the right boundary
def restart_game():
    global ball_speed_x,ball_speed_y
    #teleporint the center of the ball to the middle 
    ball.center=(screen_width/2,screen_height/2)
    #also need to change the dorection in which the ball starts moving again or else it will always start in one same direction
    ball_speed_x *=random.choice((1,-1))
    ball_speed_y *=random.choice((1,-1))


#14.2. opponent movement logic
def opponent_ai():
    if opponent.top<ball.y:
        opponent.top+=opponent_speed
    if opponent.bottom>ball.y:
        opponent.bottom-=opponent_speed
    if opponent.top<=0:
        opponent.top=0
    if opponent.bottom>=screen_height:
        opponent.bottom=screen_height

#12. defining the function for animation to keep the setup and the looop seperate
def ball_animation():
    #making the x and y sppeds global as the ball_spped_x and y inside the function is different from the one initianalized outside the function
    global ball_speed_x,ball_speed_y

    #9. animation--> incrementing the positions using the ball speed variables
    ball.x +=ball_speed_x
    ball.y +=ball_speed_y

    #10. adding logic for bouncing the ball
    #this is for the y axis
    if ball.top <=0 or ball.bottom >= screen_height:
        ball_speed_y *= -1 #reversing th e ball speed
    #this is for the x axis  if the ball hits the left or right boundary
    if ball.left<=0 or ball.right>=screen_width:
        #ball_speed_x*=-1 --> this thing was used before when we wanted to reverse the speed only instead of restarting the game
        restart_game()
    
    #11. checking for collision with the player bars
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x*=-1 #reversing the x speed

#player animation function declaration and definition
def player_animation():
    #adding player speed to player rectangle
    player.y+=player_speed

    #avoid the player from moving outside the window
    #teleporting the player bar by such small numbers that it looks like there is no movement at all
    if player.top<=0:
        player.top=0
    if player.bottom>=screen_height:
        player.bottom=screen_height


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

#5. setting a rectangle for the ball.
#this function gives the width and the height of the rectangle with its x and y positions.
#x and y positions are at the top left corner of a rectangle and origin of the window is at top left corner of display surface.
#thse 3 are empty rectangles for now. to draw them we will use a loop and pygame.draw()
ball= pygame.Rect(screen_width/2-10,screen_height/2-10,20,20)#ball is 30x30 in dimensions with positioned at the center
player=pygame.Rect(screen_width-10,screen_height/2-50,10,100)#10x140 pixel rectangle at the right middle of the screen
opponent= pygame.Rect(10,screen_height/2-50,10,100)#rectangle for opponent
#defining color using color object
bg_color=pygame.Color('grey12')
#defining color usig a tuple
light_grey=(200,200,200)

#8. adding animation --> adding speed variables
ball_speed_x=7 * random.choice((1,-1))
ball_speed_y=7 * random.choice((1,-1))

#delcaring a player speed variable
player_speed=0

#declaring the opponent speed
opponent_speed=7

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

        #13. checking the arrow key's input/event for controlling bar movement
        #this statement will only check if ANY of the keys on the keyboard was pressed
        if event.type == pygame.KEYDOWN:
            #we need another if statement to check for which key was pressed specificlly
            if event.key== pygame.K_DOWN: #down arrow key is called K_DOWN it was pressed 
                #now we will specify what will happen when we press the down key
                #14. now adding player movement logic
                player_speed+=7
            if event.key==pygame.K_UP:
                player_speed-=7
            #now for when the key is released
        if event.type==pygame.KEYUP:
            #we will reverse the player movement logic
            if event.key== pygame.K_DOWN: 
                player_speed-=7
            if event.key==pygame.K_UP:
                 player_speed+=7
       
    #animation call inside the loop
    ball_animation()
    player_animation()
    #14. opponent movement with respect to the ball
    opponent_ai()
   
    #7. filling the background color and making the line in the middle
    #both of these things dont require a rect object 
    #filling the whole display screen
    screen.fill(bg_color)
    #making the middle line
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))#anti alias line, needs the surface to draw on, the color and the tuple of the start point and the tuple of the end point

    #6. visulas
    #drawing the shapes using a loop
    pygame.draw.rect(screen,light_grey,player)#drawing player rectangle on the display screen of color light_grey
    pygame.draw.rect(screen,light_grey,opponent)
    #using pygame.draw.ellipse() instead if filling a rectangle like pygame.draw.rect() this draws an ellips form the given wireframe
    pygame.draw.ellipse(screen,light_grey,ball) #ball has dimensions 30x30 so sllipse becomes a circle

    #4. updating the window
    pygame.display.flip() #draw picture from everything that came before the loop, will drawa black screen for now
    #the clock line will limit how fast the loop runs
    #the computer tries to run the loop as fast it can, if we dont control the speed it might even run the loop at 10K frames per second
    clock.tick(60) #60 frames per second.


