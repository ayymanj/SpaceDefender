add_library('minim')  # add the Minim library
def setup():
    size(500,650)
    
    global bg, pgCount 
    global playerShip, pshipW, pshipH #player's ship dimensions and variable
    global warship, wship, wshipW, wshipH, wshipX, wshipY, totalNum #dimensions and quantity of enemy warships
    global dx, dy #speed of enemy warships
    global font 
    global levelBtn, normalBtnX, normalBtnY, hardBtnX, hardBtnY, BtnW, BtnH #dimensions and positions of level pages's buttons
    global restartBtn, restartBtnX, restartBtnY, btnW, btnH #dimensions and positions of win/lose pages's restart button
    global exitBtn, exitBtnX, exitBtnY                      #dimensions and positions of win/lose pages's exit button
    global laser, laser1, laserX, laserY, dy_l, visible, laserNum   #variables of playership's laser beam
    global warshipLaserX, warshipLaserY, warshipLaserSpeed, warshipLaserVisible  #variables of warship's laser beam
    global warshipLaserCooldown, warshipCooldownPeriod, warshipShootDelay, warshipShootProbability
    global warshipsAlive #to check is the warship isnt destroyed
    global explosion, explosionFrames, explosionFrameDuration, framecount #variables and dimensions of explosions
    global healthPower, hpX, hpY, powerW, powerH, powerNum #variables and dimensions of powerUps
    global scorePower, spX, spY
    global timeLeft, score, health
    global minim, player 

    # create a Minim object 
    minim = Minim(this)    
    # load the song into the player
    player = minim.loadFile("song.mp3")
    
    
    timeLeft = 30
    score = 0
    health = 3

    font = createFont("ElectronPulseItalic.ttf",60,60)
    bg = loadImage("space.jpg")
    
    playerShip = loadImage("spaceRocket.png")
    pshipW = pshipH = 90
    
    healthPower = loadImage("healthPower.png")
    scorePower = loadImage("scorePower.png")
    hpX = []
    hpY = []
    spX = []
    spY = []
    powerW = 60 
    powerH = 60
    powerNum = 2
    
    for i in range(powerNum):
        hpX.append(random(0, width - powerW))
        hpY.append(-random(50, 500))
    for i in range(powerNum + 1):
        spX.append(random(0, width - powerW))
        spY.append(-random(50, 500))
    
    levelBtn = loadImage("levelButton.png")
    normalBtnX = width/10
    normalBtnY = hardBtnY = height/2
    hardBtnX = width/10 * 5
    BtnW = 200
    BtnH = 90
    
    restartBtn = loadImage("playButton.png")
    exitBtn = loadImage("exitButton.png")
    restartBtnX = width/2 - 80
    restartBtnY = exitBtnY = height/2
    exitBtnX =  width/2 + 40
    btnW = 80
    btnH = 80
    
    
    warship = loadImage("warShip.png")
    totalNum = 35
    wshipW = 80
    wshipH = 85
    dx = dy = 2
    wshipX = []
    wshipY = []
    wship = []
    warshipsAlive = []
    
    # Initialize the page counter to 0
    pgCount = 0 
    
    laser1 = loadImage("laser1.png") # warShiplaser variables
    # Initialize playerlaser variables
    laser = loadImage("laser.png")
    laserNum = 35 # no. of the laser beams in list
    laserX = []   # x positions of the lasers
    laserY = []   # y positions of the lasers
    visible = []  # visibility of the lasers
    dy_l = 10      #speed of laser
    
    # Initialize warship laser variables
    warshipLaserX = []  # Store the X positions of the warship lasers
    warshipLaserY = []  # Store the Y positions of the warship lasers
    warshipLaserVisible = []
    warshipShootDelay = []
    warshipLaserCooldown = []  # List to keep track of cooldown for each warship
    warshipCooldownPeriod = 60  # Cooldown period (in frames)
    warshipLaserSpeed = 3
    warshipShootProbability = 0.005
    
    # Initialize explosion variables
    explosion = loadImage("explosion1.png")
    explosionFrames = []         # List to store the explosion frames for each warship
    explosionFrameDuration = 10  # Number of frames to display the explosion
    framecount = 0
    
    for i in range(laserNum): #updating list for lasers
        laserX.append(0) # Start x position at 0
        laserY.append(0) # Start y position at 0
        visible.append(False) # lasers are not visible at the beginning
    
    
    
    for i in range(totalNum): #updating list for war ships and their health
        wship.append(loadImage("warShip.png"))
        wshipX.append(random(0, width-wshipW)) #random x position
        wshipY.append(-random(10, 400))        #random y postion in negative direction so that they appear out of frame
        warshipsAlive.append(True)
        explosionFrames.append([]) # Initialize an empty list for each warship
        warshipLaserX.append(0)
        warshipLaserY.append(0)
        warshipLaserVisible.append(False)
        warshipLaserCooldown.append(0) # Initialize cooldown to 0 for all warships
        warshipShootDelay.append(int(random(20, 60)))
            
def draw():
    # Check the page count and call appropriate functions
    if  pgCount == 0:
        introPage()
    elif pgCount == 1:
        welcome_page()
    elif pgCount == 2:
        levelPage()
    elif pgCount == 3:
        gamePlay()
    elif pgCount == 4:
        gamePlay()
    elif pgCount == 5:
        winPage()
    elif pgCount == 6:
        losePage()
        
        
                
def setupTextProperties(fillR, fillG, fillB, sz):  #This function helps to set up text properties which reduces repetition.
    textAlign(CENTER)
    textFont(font)
    fill(fillR, fillG, fillB)
    textSize(sz)
    
def introPage(): # Display the introduction page
    global displayText
    
    image(bg, 0, 0, width, height)  # Set background
    
    setupTextProperties(255, 255, 0, 30)  #Yellow text for presentation
    text("- PRESENTING -", width / 2, height / 5 * 1.5)
    
    setupTextProperties(255, 255, 255, 45)  #White text for game title
    text("THE", width / 2, height / 5 * 2.5)
    text("SPACE DEFENDERS", width / 2, height / 5 * 3)
    
    setupTextProperties(255, 255, 255, 15)  # Additional instructions
    text("PRESS 'M' FOR MUSIC & 'S' TO STOP THE MUSIC", width / 2, height - 20)
    
    if frameCount % 40 < 20:
        displayText = True
    else:
        displayText = False
        
    if displayText == True:    
        setupTextProperties(255, 255, 0, 20)  #Instructions
        text("PRESS ENTER TO START", width / 2, height / 5 * 4)


def welcome_page(): # Display the welcome page
    global displayText
    image(bg, 0, 0, width, height)
     
    setupTextProperties(255, 255, 255, 30)  
    text("WELCOME DEFENDER", width / 2, height / 2 - 100)
    
    setupTextProperties(255, 0, 0, 15)  # Red text for game instructions
    text("USE MOUSE TO MOVE AND CLICK TO SHOOT!!!", width / 2, height / 2 - 50)
    # text("PRESS ANY KEY TO START", width / 2, height / 2)
    text("-SHOOT THE ENEMY SHIPS AND GET", width / 2, height / 2 + 50)
    text("500 POINTS BEFORE TIME RUNS OUT!!", width / 2, height / 2 + 100)
    text("-DO NOT LET ANY", width / 2, height / 2 + 150)
    text("WARSHIPS REACH THE BOTTOM SCREEN!!", width / 2, height / 2 + 200)
    
    if frameCount % 40 < 20:
        displayText = True
    else:
        displayText = False
        
    if displayText == True:    
        setupTextProperties(255, 255, 255, 30)  #Instructions
        text("PRESS ANY KEY TO START", width / 2, height / 2)
    
    
def levelPage(): # Display the level selection page
    image(bg, 0, 0, width, height)
    setupTextProperties(255, 255, 0, 25)
    text("CHOOSE YOUR DIFFICULTY LEVEL", width / 2, height / 5 * 2)
    
    #Displaying the level buttons
    image(levelBtn, normalBtnX, normalBtnY, BtnW, BtnH)
    setupTextProperties(255, 255, 255, 20)
    text("NORMAL", 150, normalBtnY+50)
        
    image(levelBtn, hardBtnX, hardBtnY, BtnW, BtnH)
    setupTextProperties(255, 255, 255, 20)
    text("LEGENDARY", 350, normalBtnY+50)
 
def startGame(): # Start the game with selected difficulty level's desired variables
                 # The startGame() function is important for initializing the game with the desired difficulty level's variables and settings.
                 # Without it, the game may not have the correct difficulty level, the score may not reset, or other important variables may not be properly initialized.
                 # By separating the game initialization logic, the code becomes more organized and maintainable.
            
    global timeLeft, health, dy, score, pgCount

    score = 0  # Reset score for new game

    if pgCount == 3:  # Normal difficulty settings
        timeLeft = 30
        health = 3
        dy = 2
    elif pgCount == 4:  # Legendary difficulty settings
        timeLeft = 15  # Decrease time for higher difficulty
        health = 1     # Decrease health for higher difficulty
        dy = 3         # Increase speed for higher difficulty
   
def gamePlay(): # Main game logic
    global pshipW, pshipH, framecount, timeLeft, score, health, dy, pgCount
    image(bg, 0, 0, width, height)
    image(playerShip, mouseX - pshipW /2 , mouseY - pshipH / 2, pshipW, pshipH)
    
    if frameCount % 60 == 0 and timeLeft > 0: # Decrease the timeLeft variable by 1 every 60 frames (1 second) if timeLeft is greater than 0
        timeLeft -= 1    
    
    for i in range(totalNum):
        # Check if a warship should shoot a laser
        if (warshipsAlive[i] == True and warshipLaserVisible[i] == False and random(1) < warshipShootProbability and warshipLaserCooldown[i] == 0 and warshipShootDelay[i] == 0):
            warshipLaserVisible[i] = True
            warshipLaserX[i] = wshipX[i] + wshipW / 2  # Set the laser X position to the middle of the warship
            warshipLaserY[i] = wshipY[i] + wshipH      # Set the laser Y position to the bottom of the warship
            warshipLaserCooldown[i] = warshipCooldownPeriod   # Reset the cooldown
                                                              # The warshipCooldownPeriod determines how long the warship must wait before it can shoot again after firing a laser.
            #Reset the shoot delay period for the current warship
            warshipShootDelay[i] = int(random(20, 60))  # Update the shoot delay period
            
        if warshipLaserCooldown[i] > 0:  #The warshipCooldownPeriod variable determines the duration of the cooldown period that a warship must wait after firing a laser before it can shoot again.
            warshipLaserCooldown[i] -= 1 
        
        if warshipShootDelay[i] > 0:     #The warshipShootDelay variable controls the timing of shots fired by each warship
           warshipShootDelay[i] -= 1    #It is also decreased by 1 if it's greater than 0, controlling the timing of consecutive shots.    
        
        # Update the laser's position and check if it's off the screen
        if warshipLaserVisible[i] == True:
            # Update the Y position of the laser
            warshipLaserY[i] += warshipLaserSpeed
            # Draw the laser
            image(laser1, warshipLaserX[i], warshipLaserY[i], 20, 30)
            # Check if the laser is off the screen and reset its visibility
            if warshipLaserY[i] > height:
                warshipLaserVisible[i] = False
                
        # Draw the warship and update its position
        if warshipsAlive[i] == True:
            image(warship, wshipX[i], wshipY[i], wshipW, wshipH)
            wshipY[i] += dy
            
            if wshipY[i] >= height: # Checking if warship goes out of screen and updating the y-coordinates
                health -= 1
                if health < 0:
                    health = 0
                wshipY[i] = -random(10, 100)
            
            
            wLeft = wshipX[i]              # Leftmost x-coordinate of the warship's bounding box
            wRight = wshipX[i] +  wshipW   # Rightmost x-coordinate of the warship's bounding box
            wTop = wshipY[i]               # Topmost y-coordinate of the warship's bounding box
            wBottom = wshipY[i] +  wshipH  # Bottommost y-coordinate of the warship's bounding box
                            
            for j in range(laserNum): # Loop through all laser beams
                if visible[j] == True:
                    # Define the laser's bounding box coordinates
                    laserLeft = laserX[j]        # Leftmost x-coordinate of the laser's bounding box
                    laserRight = laserX[j] + 20  # Rightmost x-coordinate of the laser's bounding box
                    laserTop = laserY[j]         # Topmost y-coordinate of the laser's bounding box
                    laserBottom = laserY[j] + 30 # Bottommost y-coordinate of the laser's bounding box
                    
                    # Check if the warship's bounding box and the laser's bounding box intersect
                    if (wTop < laserBottom and laserTop < wBottom and wLeft < laserRight and laserLeft < wRight): 
                        warshipsAlive[i] = False  # Set warship as destroyed
                        visible[j] = False  # Set laser as not visible
                        score += 15    # Increase the score      
                        
                        for k in range(5): # Add explosion frames for the current warship
                            explosionFrames[i].append(explosion)
                            #By using loop to add multiple frames of the explosion image to the `explosionFrames` list, this enables the creation of an animated explosion effect when a warship is destroyed in the game.
        
        # Check if the player ship collides with a warship's laser
        if (mouseX - pshipW / 2 < warshipLaserX[i] + 20 and mouseX - pshipW / 2 + pshipW > warshipLaserX[i] and mouseY - pshipH / 2 < warshipLaserY[i] + 30 and mouseY - pshipH / 2 + pshipH > warshipLaserY[i]):
             if warshipLaserVisible[i] == True:
                warshipLaserVisible[i] = False
                score -= 3

             if score < 0:
                score = 0

            
    for i in range(laserNum): # Loop through all laser beams
        if visible[i] == True:
            image(laser, laserX[i], laserY[i], 20, 30)
            laserY[i] -= dy_l
            
    for i in range(totalNum):                                   # Drawing the explosion frames for each warship
        for frame in explosionFrames[i]:
            image(frame, wshipX[i], wshipY[i], wshipW, wshipH)  # Display each explosion frame at the warship's position
            framecount += 1
            
            # Removing explosion frames after a certain duration
            if framecount >= explosionFrameDuration:
                explosionFrames[i] = []  # Clear explosion frames for the warship
                framecount = 0           # Reset frame count
    
    for i in range(powerNum):
        image(healthPower, hpX[i], hpY[i], powerW, powerH)
        hpY[i] += dy
        if hpY[i] > height:
            hpY[i] = random(-50, -500)
            
        # Collision detection between player's ship and healthPower
        if mouseX - pshipW / 2 < hpX[i] + powerW and mouseX - pshipW / 2 + pshipW > hpX[i] and mouseY - pshipH / 2 < hpY[i] + powerH and mouseY - pshipH / 2 + pshipH > hpY[i]:
            health += 1
            hpX[i] = -100  # Move the healthPower off-screen to simulate disappearance
            
            
    for i in range(powerNum + 1):
        image(scorePower, spX[i], spY[i], powerW, powerH)
        spY[i] += dy
        if spY[i] > height:
            spY[i] = random(-50, -500)
            
        # Collision detection between player's ship and scorePower
        if mouseX - pshipW / 2 < spX[i] + powerW and mouseX - pshipW / 2 + pshipW > spX[i] and mouseY - pshipH / 2 < spY[i] + powerH and mouseY - pshipH / 2 + pshipH > spY[i]:
            score += 3
            spX[i] = -100
        
    # Update pgCount based on game conditions
    if score >= 500 and timeLeft > 0 and health > 0:
        pgCount = 5
    elif timeLeft <= 0 or health <= 0 or score<0:
        pgCount = 6
        
    setupTextProperties(255, 255, 255, 15)
    text("Time left: " + str(timeLeft), 50, 30)
    text("Score: " + str(score), 50, 60)
    text("Health: " + str(health), 50, 90)


def winPage(): # Display win screen
    image(bg, 0, 0, width, height)
    
    setupTextProperties(255, 255, 255, 80)
    text("GAME WIN",  width / 2, height / 5 * 1.5)
    
    image(restartBtn, restartBtnX, restartBtnY, btnW, btnH)
    image(exitBtn, exitBtnX, exitBtnY, 90, 90)
    
def losePage(): # Display lose screen
    image(bg, 0, 0, width, height)
    
    setupTextProperties(255, 255, 255, 80)
    text("GAME LOST",  width / 2, height / 5 * 1.5)
    
    image(restartBtn, restartBtnX, restartBtnY, btnW, btnH)
    image(exitBtn, exitBtnX, exitBtnY, 90, 90)
    
def keyPressed():
    global pgCount
    if key == ENTER and pgCount == 0: #Transition from intro to welcome page
        pgCount = 1
    elif pgCount == 1: #Transition from welcome page to level selection page
        pgCount = 2
    elif (key == 's' or key == "S"):  # stop
        player.pause() # pause
        player.rewind() # rewind to the begining of the song
    elif (key == 'm' or key == "M"): # loop
        player.loop()
    
        
        
def mousePressed():
    global pgCount
    if pgCount == 2: #to check if we are on the level selection page
        
      if (mouseX > normalBtnX and mouseX < normalBtnX + BtnW and #To check if the "Normal" button is clicked
          mouseY > normalBtnY and mouseY < normalBtnY +  BtnH):
            pgCount = 3
            startGame() 
            
      elif (mouseX > hardBtnX and mouseX < hardBtnX+ BtnW and #To check if the "Legendary" button is clicked
          mouseY > hardBtnY and mouseY < hardBtnY +  BtnH):
          pgCount = 4 
          startGame()
    
        
    elif pgCount == 3 or pgCount == 4:
        found = False  # A variable to indicate if a laser has been made visible
        for i in range(laserNum):
            if found == False and visible[i] == False:
                laserX[i] = mouseX
                laserY[i] = mouseY
                visible[i] = True # Make the laser visible
                found = True # Set the variable to True to stop looking for invisible lasers
                
    elif pgCount == 5:
        if (mouseX > restartBtnX and mouseX < restartBtnX + btnW and mouseY > restartBtnY and mouseY < restartBtnY +  btnH):  #To check if the "Restart" button is clicked
            setup() # Reset the game state by calling setup() when the "Restart" button is clicked , without setup() the game state may not be properly reset, which can lead to unexpected behavior or incorrect values in variables.
            pgCount = 2
            
        elif (mouseX > exitBtnX and mouseX < exitBtnX+ btnW + 10 and mouseY > exitBtnY and mouseY < exitBtnY +  btnH + 10):   #To check if the "exit" button is clicked
            exit() # Terminate the game by calling exit() when the "exit" button is clicked
    
    elif pgCount == 6:
        if (mouseX > restartBtnX and mouseX < restartBtnX + btnW and mouseY > restartBtnY and mouseY < restartBtnY +  btnH):  
            setup()
            pgCount = 2
            
        elif (mouseX > exitBtnX and mouseX < exitBtnX+ btnW + 10 and mouseY > exitBtnY and mouseY < exitBtnY +  btnH + 10): 
            exit()        
    
    
# Minim requires this stop() function 
def stop():
    # close the player
    player.close()
    # stop Minim
    minim.stop()            
            

                
            
