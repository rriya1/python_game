# 2 parts of the game. one setup part and one loop. setup has logic and data. loop gives movement
import pygame, sys, random
player_score=0
opponent_score=0

#17 timer variables
score_time= None 


#15. restarting the game when the ball hits the left or the right boundary
def restart_game():
    global ball_speed_x,ball_speed_y, score_time
    #17.3 we want to measure the current time and aslo we want to ensure that everything runes only after 3 seconds of restrting the game
    #putting the ball at the center of the scrren
    #teleporint the center of the ball to the middle
    ball.center=(screen_width/2,screen_height/2-25)
    # we also wanna ensure that we change the score_time back to None or else the condition ill always be true
    current_time= pygame.time.get_ticks() #this will keep running again and again
    
    #18. adding timer for 3 2 1 text
    if current_time-score_time<1000:
        number3= game_text.render("3",False,light_grey)
        screen.blit(number3,(screen_width/2-4,screen_height/2+3))
    if current_time-score_time>1000 and current_time-score_time<2000:
        number2= game_text.render("2",False,light_grey)
        screen.blit(number2,(screen_width/2-4,screen_height/2+3))
    if current_time-score_time>2000 and current_time-score_time<3000:
        number1= game_text.render("1",False,light_grey)
        screen.blit(number1,(screen_width/2-4,screen_height/2+3))
        
    #timer, when the time is less than the specified time then the ball wont move
    if current_time-score_time<3000:
        ball_speed_x,ball_speed_y=0,0
    else:
        #also need to change the dorection in which the ball starts moving again or else it will always start in one same direction
        ball_speed_x = 4*random.choice((1,-1))
        ball_speed_y = 4*random.choice((1,-1))
        #setting the score time to none so that function does not run again
        score_time=None

    

  
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
    global ball_speed_x,ball_speed_y,player_score,opponent_score, score_time

    #9. animation--> incrementing the positions using the ball speed variables
    ball.x +=ball_speed_x
    ball.y +=ball_speed_y

    #10. adding logic for bouncing the ball
    #this is for the y axis
    if ball.top <=0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1 #reversing th e ball speed
    #this is for the x axis  if the ball hits the left or right boundary
    if ball.left<=0:
         pygame.mixer.Sound.play(score_sound)
         player_score += 1
         #restart_game()
         score_time= pygame.time.get_ticks() #this will tell hpw long it has been since the game got started, this wll be point 1 whch only checks the time once.
       
    if ball.right>=screen_width:
        pygame.mixer.Sound.play(score_sound)
        #ball_speed_x*=-1 --> this thing was used before when we wanted to reverse the speed only instead of restarting the game
        ##restart_game() #getting rid of the resart function from here so that it dosent get called just once, but gets called multiple times because we want to measure current time 
        opponent_score += 1 #16. updating the game score
        score_time= pygame.time.get_ticks()

    #11. checking for collision with the player bars
    #19 turning the collision if's into 2 different if statements , onr for each peddle
    if ball.colliderect(player) and ball_speed_x>0: #collision has happened with player and ball is moving in the direction of player
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right-player.left)<10:
            ball_speed_x*=-1 #reversing the x speed
        elif abs(ball.bottom-player.top)<10 and ball.y>0:
            ball_speed_y*=-1
        elif abs(ball.top-player.bottom)<10 and ball.y<0:
            ball_speed_y*=-1
    if ball.colliderect(opponent) and ball_speed_y<0:
        if abs(ball.left-opponent.right)<10:
            ball_speed_x*=-1
        elif abs(ball.bottom-opponent.top)<10 and ball.y>0:
            ball_speed_y*=-1
        elif abs(ball.top-opponent.bottom)<10 and ball.y<0:
            ball_speed_y*=-1

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


#1. general  setup 
#these lines are important for the general setup
# pygame.init() initiates all the pygame modules and is required to run any pygame code
pygame.init() 
pygame.mixer.pre_init(44100,-16,2,500)
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
ball_speed_x=4 * random.choice((1,-1))
ball_speed_y=4 * random.choice((1,-1))

#delcaring a player speed variable
player_speed=0

#declaring the opponent speed
opponent_speed=4

#20. sound importing 
pong_sound=pygame.mixer.Sound("pong.ogg")
score_sound=pygame.mixer.Sound("score.ogg")

# we want to get the time whenever someone scores because thats when the person needs to start the timer, aftre this moment we need to halt for 3 seconds

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
                player_speed+=4
            if event.key==pygame.K_UP:
                player_speed-=4
            #now for when the key is released
        if event.type==pygame.KEYUP:
            #we will reverse the player movement logic
            if event.key== pygame.K_DOWN: 
                player_speed-=4
            if event.key==pygame.K_UP:
                 player_speed+=4

    #game logic   
    #animation call inside the loop
    ball_animation()
    player_animation()
    #14. opponent movement with respect to the ball
    opponent_ai()
    #game logic end

    #15.text variables
   
    game_text= pygame.font.Font("freesansbold.ttf", 15)

    #viulas 
    #7. filling the background color and making the line in the middle
    #both of these things dont require a rect object 
    #filling the whole display screen
    screen.fill(bg_color)
    #making the middle line
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))#anti alias line, needs the surface to draw on, the color and the tuple of the start point and the tuple of the end point

    #6.  shape visulas
    #drawing the shapes using a loop
    pygame.draw.rect(screen,light_grey,player)#drawing player rectangle on the display screen of color light_grey
    pygame.draw.rect(screen,light_grey,opponent)
    #using pygame.draw.ellipse() instead if filling a rectangle like pygame.draw.rect() this draws an ellips form the given wireframe
    pygame.draw.ellipse(screen,light_grey,ball) #ball has dimensions 30x30 so sllipse becomes a circle

    #17.2 adding the restrt_game() function. it will run only when the condition of score_time is satisfird
    if score_time:
        restart_game()
    #16. making the surface for the text
    #for the player
    player_text= game_text.render(f"{player_score}",False,light_grey)
    #putting that surface on our main display surface
    screen.blit(player_text,(327,230))
    #for the opponent
    opponent_text= game_text.render(f"{opponent_score}",False,light_grey)
    screen.blit(opponent_text,(308,230))

    #4. updating the window
    pygame.display.flip() #draw picture from everything that came before the loop, will drawa black screen for now
    #the clock line will limit how fast the loop runs
    #the computer tries to run the loop as fast it can, if we dont control the speed it might even run the loop at 10K frames per second
    clock.tick(60) #60 frames per second.


