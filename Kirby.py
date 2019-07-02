# Kendra Tam
# A1_Kendra.py
# October 5, 2016
# This program is an orginal game based on the characters from Kirby

#Importing
import pygame, sys
from pygame.locals import *
import random

#Start creating a graphical program
pygame.init()

#Set Screen Dimensions
WIDTH = 650
HEIGHT = 520
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#Name of Window Opened
pygame.display.set_caption('Kirby')

#Define Colour Values (R,G,B)
WHITE = (255, 255, 255)
PINK = (255,105,180)
BLACK = (0, 0, 0)
LIGHTBLUE = (99, 221, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Defining Global Variables
start = False
done = False
win = False
fall = False
jump = False
kAttack = False
delayAttack = False
sCollide = False
kCollide = True

kx = 34
ky = 373
kDir = "right"
jumpNum = 0
attackNum = 0

enemies = []
enemiesX = []
enemiesY = []
enemiesIndex = []
eDir = []
enemiesCollide = []
rand = 90

platX = [333, 450, 225, 111]
platY = [190, 240, 320, 355]
structureX = [336, 149, 37]
structureY = [287, 137, 100]
lengthX = [313, 182, 109]
sideX = [37, 150, 337]
sideY = [0, 120, 150]
sideLengthY = [100, 137, 100]

icX = [307, 601, 195]
icY = [387, 275, 128]
icNum = random.randint(0, len(icX)-1)
icTotal = 0

rocketX = [506, 530, 555, 577, 600]
move = 0

space = 0
scoreNum = 0
scoreStr = "SCORE: " + str(scoreNum)

result = "YOU LOSE"

#Define Images
game = pygame.image.load("background.png")
title = pygame.image.load("title.png")
back = title

walkL1 = pygame.image.load("l_walk1.png")
walkL2 = pygame.image.load("l_still.png")
walkL3 = pygame.image.load("l_walk2.png")
walkR1 = pygame.image.load("r_walk1.png")
walkR2 = pygame.image.load("r_still.png")
walkR3 = pygame.image.load("r_walk2.png")
jumpL1 = pygame.image.load("l_jump1.png")
jumpL2 = pygame.image.load("l_jump2.png")
jumpR1 = pygame.image.load("r_jump1.png")
jumpR2 = pygame.image.load("r_jump2.png")
hitL1 = pygame.image.load("l_hit1.png")
hitL2 = pygame.image.load("l_hit2.png")
hitL3 = pygame.image.load("l_hit3.png")
hitR1 = pygame.image.load("r_hit1.png")
hitR2 = pygame.image.load("r_hit2.png")
hitR3 = pygame.image.load("r_hit3.png")
left = [walkL1, walkL2, walkL3, walkL2]
right = [walkR1, walkR2, walkR3, walkR2]
hitL = [hitL1, hitL2, hitL3]
hitR = [hitR1, hitR2, hitR3]
k = walkR2
kIndex = 0

enemyL1 = pygame.image.load("l_enemy1.png")
enemyL2 = pygame.image.load("l_enemy2.png")
enemyL3 = pygame.image.load("l_enemy3.png")
enemyL = [enemyL1, enemyL2, enemyL3]
enemyR1 = pygame.image.load("r_enemy1.png")
enemyR2 = pygame.image.load("r_enemy2.png")
enemyR3 = pygame.image.load("r_enemy3.png")
enemyR = [enemyR1, enemyR2, enemyR3]

icIcon = pygame.image.load("ice_cream.png")

stage1 = pygame.image.load("stage1.png")
stage2 = pygame.image.load("stage2.png")
stage3 = pygame.image.load("stage3.png")
stage4 = pygame.image.load("stage4.png")
stage5 = pygame.image.load("stage5.png")
rocketFull = pygame.image.load("rocket.png")
rocketStages = [stage1, stage2, stage3, stage4, stage5]

plat = pygame.image.load("platform.png")

#Defining Fonts
tfont = pygame.font.SysFont("Kirby Classic", 70, False, False)
pfont = pygame.font.SysFont("Rockwell", 20, False, False)
sfont = pygame.font.SysFont("Kirby Classic", 30, False, False)
sefont = pygame.font.SysFont("Rockwell", 40, False, False)
endFont = pygame.font.SysFont("Rockwell", 30, False, False)

#Rendering Text
ttext1 = tfont.render("KIRBY'S ICE CREAM", False, PINK)
ttext2 = tfont.render("ESCAPE", False, PINK)
ptext1 = pfont.render("Purpose: Collect 5 ice creams to build your", False, WHITE)
ptext2 = pfont.render("rocket to escape. Avoid or attack the", False, WHITE)
ptext3 = pfont.render("knights trying to stop you. More and", False, WHITE)
ptext4 = pfont.render("more knights will come out, so collect", False, WHITE)
ptext5 = pfont.render("all the ice creams as fast as you can", False, WHITE)
ptext6 = pfont.render("then get back to the rocket before the", False, WHITE)
ptext7 = pfont.render("whole calvary comes.", False, WHITE)
ktext1 = pfont.render("Keys:", False, WHITE)
ktext2 = pfont.render("Left/Right Arrow - Walk", False, WHITE)
ktext3 = pfont.render("Up Arrow - Jump", False, WHITE)
ktext4 = pfont.render("Space Bar - Attack", False, WHITE)
stext = sfont.render("PRESS SPACE TO START", False, PINK)
scoreText = sefont.render(scoreStr, False, WHITE)
endText = sefont.render(result, False, PINK)

# background - outputs the background image and platforms on the screen
# @param: none
# @return: none
def background():
    #blit image
    screen.blit(back, (0, 0))

# titleScreen - outputs all the text on the title screen
# @param: none
# @return: none
def titleScreen():
    #blit rectangle under text
    pygame.draw.rect(screen, BLACK, (100, 175, 450, 275))
    pygame.draw.rect(screen, LIGHTBLUE, (100, 175, 450, 275), 2)
    
    #blit title text
    screen.blit(ttext1, (24, 10))
    screen.blit(ttext2, (210, 90))
    
    #blit purpose text
    screen.blit(ptext1, (105, 180))
    screen.blit(ptext2, (190, 205))
    screen.blit(ptext3, (190, 230))
    screen.blit(ptext4, (190, 255))
    screen.blit(ptext5, (190, 280))
    screen.blit(ptext6, (190, 305))
    screen.blit(ptext7, (190, 330))
    
    #blit keys text
    screen.blit(ktext1, (105, 370))
    screen.blit(ktext2, (190, 370))
    screen.blit(ktext3, (190, 395))
    screen.blit(ktext4, (190, 420))
    
    #blit start text
    screen.blit(stext, (163, 470))

# platforms - outputs all the platforms on to the screen
# @param: none
# @return: none
def platforms():
    #goes through all the platform's x and y coordinates
    for i in range(0, len(platX)):
        #blits the coressponding platform
        screen.blit(plat, (platX[i], platY[i]))

# kirby - outputs kirby on to the screen
# @param: none
# @return: none
def kirby():
    #blit image
    screen.blit(k, (kx, ky))

# enemy - outputs the enemies on to the screen
# @param: none
# @return: none
def enemy():
    #goes through all the enemies to blit the coressponding images at the right coordinates
    for i in range(len(enemies)):
        screen.blit(enemies[i], (enemiesX[i], enemiesY[i]))

# collide - checks if the person has collided with a platform
# @param: person (str), x (int), y(int)
# @return: hit (boolean)
def collide(person, x, y):
    #set variable
    hit = False
    
    #checks if kirby use these checking variables
    if person == "kirby":
        checkX = 28
        checkY = 35
    #otherwise use these checking variables
    else:
        checkX = 50
        checkY = 38
    
    #goes through all the platforms
    for i in range(0, len(platX)):
        #if the person is in range of the platforms, stay on the platform and stop falling 
        if (x + checkX >= platX[i] and x <= platX[i] + 114 and y + checkY >= platY[i] + 8 and y + checkY <= platY[i] + 15):
            #reset variable
            hit = True
    
    #goes through all the structure floors
    for i in range(0, len(structureX)):
        #if the person is in range of the structure floor, stay on the structure and stop falling
        if (x + checkX >= structureX[i] and x <= structureX[i] + lengthX[i] and y + checkY >= structureY[i] + 10 and y + checkY <= structureY[i] + 17):
            #reset variable
            hit = True
    
    return hit


# sideCollide - checks if Kirby has collided with the side of the structure
# @param: none
# @return: lCollide (boolean)
def sideCollide():
    #set variable
    lCollide = False
    
    #goes through all the places kirby can hit the side of the structure
    for i in range(0, len(sideX)):
        #if kirby has hit the side of the structure, he can't move left more
        if ky <= sideY[i] + sideLengthY[i] and ky + 35 >= sideY[i] and kx <= sideX[i]:
            #reset variable
            lCollide = True
            
    return lCollide

# attack - checks if the enemy has attacked kirby or vice versa
# @param: none
# @return: none
def attack():
    global done
    global scoreNum
    global scoreStr
    global scoreText
    
    #goes through all the enemies
    for i in range(0, len(enemies)):
        #if kirby gets in contact with an enemy, check if kirby is attacking
        if kx <= enemiesX[i] + 45 and kx + 23 >= enemiesX[i] and ky <= enemiesY[i] + 33 and ky + 31 >= enemiesY[i]:
            #if kirby is attacking, add to score, update score, and make the enemy disappear
            if kAttack:
                scoreNum = scoreNum + 20
                scoreStr = "SCORE: " + str(scoreNum)
                scoreText = sefont.render(scoreStr, False, WHITE)
                enemiesY[i] = 800
            #otherwise end the game
            else:
                done = True

# iceCream - outputs the ice cream icons
# @param: none
# @return: none
def iceCream():
    #blit image
    screen.blit(icIcon, (icX[icNum], icY[icNum]))

# rocketShip - outputs the rocket ship on to the screen	
# @param: none
# @return: none
def rocketShip():
    #if the game is won, blit the full rocket
    if win:
        screen.blit(rocketFull, (426 + move, 324))
    
    #else kirby has not won so blit the rocket in construction
    else:
        #goes through the rocket stages depending on how many ice creams you have collected
        for i in range(0, icTotal):
            #blit image of coressponding rocket stage
            screen.blit(rocketStages[i], (rocketX[i], 324))

# score - outputs the score 
# @param: none
# @return: none
def score():
    #blit image with x changing depending on the number of digits
    screen.blit(scoreText, (450 - space*15, 10))

# end - outputs a box to say your result (win or lose) and score
# @param: none
# @return: none
def end():
    
    #blit box around text
    pygame.draw.rect(screen, BLACK, (200, 175, 250, 150))
    pygame.draw.rect(screen, LIGHTBLUE, (200, 175, 250, 150), 2)
    #blit text
    screen.blit(endText, (225, 200))
    screen.blit(endScore, (225, 250))

#function that redraws the screen
def redraw_screen():
    #filling colour of screen
    screen.fill(BLACK)
    
    #drawing commands
    background()
    
    #if game has started, print the game screen
    if start:
        #if the number of ice creams collected is less than 5 then blit 
        if icTotal < 5:
            iceCream()
        
        #calls drawing functions
        platforms()
        rocketShip()
        
        #if kirby hasn't won, blit kirby
        if not win:
            kirby()
        
        #calls drawing functions
        enemy()
        score()
        
        #if the game has ended, blit the end screen
        if done:
            end()
    
    #otherwise the game hasn't startd and the title screen will be blit
    else:
        titleScreen()
    
    #updating
    pygame.display.update()

#starting gameplay  
inPlay = True
print ("Hit ESC to end the program.")

#keep looping and keeping graphical interface is run while inPlay is true
while inPlay:
    #if the game has started and not done (if during gameplay)
    if start and not done:
        
        #check if kirby has collided with a platform or structure
        kCollide = collide("kirby", kx, ky)
        lCollide = sideCollide()
        #check if kirby has attacked or been attacked by an enemy
        attack()
        
        #if kirby has collected all 5 ice creams and have reached the rocket ship, kirby has won the game
        if icTotal == 5 and kx + 28 >= 506 and ky >= 310:
            win = True
        
        #set spacing to 0
        space = 0
        s = scoreNum
        #while the score is greater than 0, add more spacing for the digits
        while s > 0:
            #divide to find the number of digits
            s = s / 10
            #reset variable
            space = space + 1
        
        #if kirby has hit an ice cream, add and update to score and the number of ice creams collected
        if kx + 28 >= icX[icNum] and kx <= icX[icNum] + 15 and ky + 35 >= icY[icNum] and ky <= icY[icNum] + 10 and icTotal != 5:
            scoreNum = scoreNum + 10
            scoreStr = "SCORE: " + str(scoreNum)
            scoreText = sefont.render(scoreStr, False, WHITE)
            
            icTotal = icTotal + 1
    
            #make the ice cream appear somewhere else
            newNum = random.randint(0, len(icX)-1)
            #keep coming up with new places until it is different from the old number
            while icNum == newNum:
                newNum = random.randint(0, len(icX)-1)
            #change the ice cream to a new location
            icNum = newNum
        
        #goes through all the enemies
        for i in range(len(enemiesIndex)):
            #if the enemy is at the second image, change it to the first
            if enemiesIndex[i] == 2:
                enemiesIndex[i] = 0
            #otherwise just change it to one more than it was before
            else:
                enemiesIndex[i] = enemiesIndex[i] + 1
            
            #if the enemy is facing left move change the image to the new image and move the enemy to the left
            if eDir[i] == "left":
                enemies[i] = enemyL[enemiesIndex[i]]
                enemiesX[i] = enemiesX[i] - 8
            
            #else enemy is facing right and change the image to the new image and move the enemy to the right
            else:
                enemies[i] = enemyR[enemiesIndex[i]]
                enemiesX[i] = enemiesX[i] + 8
            
            #check if the enemy has collided with the platforms/structure
            enemiesCollide[i] = collide("enemy", enemiesX[i], enemiesY[i])
            #if the enemy has not collided with anything, make him fall
            if not enemiesCollide[i] and enemiesY[i] < 367:
                enemiesY[i] = enemiesY[i] + 8
                
                #if it is facing left, blit the left image
                if eDir[i] == "left":
                    enemies[i] = enemyL2
                #otherwise blit the right image
                else:
                    enemies[i] = enemyR2
            
            #if the enemy has hit the left side of the screen, change his direction to right
            if enemiesX[i] <= 0:
                eDir[i] = "right"
            #if the eneemy has hit the right side of the screen, change his direction to left
            elif enemiesX[i] >= 600:
                eDir[i] = "left"
        
        #finds a random number, range will decrease after an enemy comes out 
        num = random.randint(0, rand)
        #if the number equals to 0, make a new enemy
        if num == 0:
            #declare new enemy information
            enemies.append(enemyR1)
            enemiesX.append(76)
            enemiesY.append(72)
            enemiesIndex.append(0)
            eDir.append("right")
            enemiesCollide.append(True)
            
            #if the range is not less than 20 make the difficulty higher by making the range smaller and having a higher probablility of more knights coming out
            if rand >= 20:
                rand = rand - 10
        
        #if kirby is jumping, change y and images accordingly
        if jump:
            
            #keeps track of how long the whole jump time is
            jumpNum = jumpNum + 1
            
            #if jumpNum is less than 8, make kirby jump up
            if jumpNum <= 8:
                #if kirby has hit the ceiling of the structure, do nothing
                if ky <= 265 and ky >= 255 and kx > 0 and kx < 334:
                    pass
                #else he hasn't hit the ceiling make kirby go up
                else:
                    ky = ky - 7
                
                #if he is facing right when he jumps, change the image to him in the air jumping facing the right
                if kDir == "right":
                    k = jumpR1
                #else he is facing left and change the image of kirby jumping facing the left
                else:
                    k = jumpL1
            
            #elif jumpNum is less than 16 and has not hit a platform, making him come back down to where he was before
            elif jumpNum <= 16 and not kCollide:
                ky = ky + 7
                #f he is facing right when he is falling back down, change the image to him in the air falling facing the right
                if kDir == "right":
                    k = jumpR2
                #else he is facing left so change the image to him in the air falling facing the left
                else:
                    k = jumpL2
            
            #else, kirby has come back down to the ground
            else:
                #if kirby is facing right, blit the right facing image
                if kDir == "right":
                    k = walkR2
                #else kirby is facing left, blit the left facing image
                else:
                    k = walkL2
                    
                #reset variables
                jump = False
                kCollide = False
                jumpNum = 0
        
        #else kirby is not jumping      
        else:
            #if kirby has not hit a platform or the ground, make him fall
            if not kCollide and ky < 373:
                #change y coordinates
                ky = ky + 7
                #reset variable
                fall = True
                
                #change the image according to the direction kirby is facing
                if kDir == "right":
                    k = jumpR2
                else:
                    k = jumpL2
            
            #else kirby has collided with a platform or the ground
            else:
                #reset variable
                fall = False
                
                #change the image according to the direction kirby is facing
                if kDir == "right":
                    k = walkR2
                else:
                    k = walkL2
        
        #if kirby is attacking or has just attacked, start attack or delaying attack sequence
        if kAttack or delayAttack:
            #if kirby is attacking, blit correct images according to which way he is facing
            if kAttack:
                #if kirby is facing left, pick the left images
                if kDir == "left":
                    #each attacking kirby image will be on the same image for two blits
                    k = hitL[attackNum/2]
                #else kirby is facing right and pick the right images
                else:
                    #each attacking kirby image will be on the same image for two blits
                    k = hitR[attackNum/2]
                
                #if attackNum is 4, kirby is done attacking
                if attackNum == 4:
                    #if he is facing left, return him to the image of him facing left
                    if kDir == "left":
                        k = walkL2
                    #else return him to the iamge of him facing right
                    else:
                        k = walkR2
                    
                    #reset it to show kirby is done attacking
                    kAttack = False
                    #reset to delay kirby from its next attack so user can not spam click/attack all the enemies
                    delayAttack = True
            
            #if attackNum has reached 6, delay is over and kirby can attack again        
            if attackNum == 6:
                attackNum = 0
                delayAttack = False
            
            #keeps track of how long kirby has attacked for
            attackNum = attackNum + 1
    
    #if kirby won the game, commence winning sequence    
    if win:
        #reset the result and /re-render the text
        result = "YOU WIN"
        endText = sefont.render(result, False, PINK)
        
        #move the rocket ship off the screen by 10 until it has moved 300 pixels over
        if move <= 300:
            move = move + 10
        
        #when it is done moving, set done to true to start ending sequence
        else:
            done = True
            
    #if the game is done, render the end score font
    if done:
        endScore = endFont.render(scoreStr, False, WHITE)
            
    #deals with any keyboard options once program is run
    #looks for the event (action of using keyboard)
    pygame.event.get()
    
    # get_pressed() method generates a True/False list for the status of all keys
    keys = pygame.key.get_pressed()
    
    #looks for escape to be pressed
    if keys[pygame.K_ESCAPE]:
        #reset variable to quie program
        inPlay = False
    
    #if the game is not done, kirby's controls will still work
    if not done:
        
        #looks for left arrow to be pressed and to satisfy the collision conditions
        if keys[pygame.K_LEFT] and kx >= 0 and not lCollide:
            kDir = "left"
            
            #move kirby left by 7
            kx = kx - 7
            
            #if kirby is on the image at index 3, go back to the one at index 0
            if kIndex == 3:
                kIndex = 0
            #otherwise, the index is one more than the previous
            else:
                kIndex = kIndex + 1
            
            #kirby's image is him walking left unless he is jumping, attacking, or falling    
            if not jump and not kAttack and not fall:    
                k = left[kIndex]
        
        #looks for right arrow to be pressed and to satisfy the collision conditions           
        if keys[pygame.K_RIGHT] and kx <= 617:
            kDir = "right"
            
            #moves kirby to the right by 7
            kx = kx + 7
            
            #if kirby is on the image at index 3, go back to the one at index 0
            if kIndex == 3:
                kIndex = 0
            #otherwise, the index is one more than the previous
            else:
                kIndex = kIndex + 1
            
            #kirby's image is him walking right unless he is jumping, attacking, or falling
            if not jump and not kAttack and not fall:
                k = right[kIndex]
        
        #looks for up arrow to be pressed and to satisfy the collision conditions    
        if keys[pygame.K_UP] and not jump and (kCollide or ky == 373):
            #allow kirby to jump
            jump = True
        
        #looks for the space bar to be pressed and makes sures that kirby won't attacke when jumping or when he has just attacked
        if keys[pygame.K_SPACE] and not jump and not delayAttack:
            #if the game hasn't started, start the game and change the background
            if not start:
                #reset variables
                back = game
                start = True
            #else game has started and pressing space will allow kirby to attack
            else:
                kAttack = True

    redraw_screen()                     # the screen window must be constantly redrawn - animation
    pygame.time.delay(50)               # pause for 50 miliseconds
#---------------------------------------#
pygame.quit()                           # always quit pygame when done!


