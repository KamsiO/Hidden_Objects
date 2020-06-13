def setup():
    size(1920, 1080)
    global welcomescrn
    welcomescrn = loadImage("small-riverside-house-fantasy-hd-wallpaper-1920x1080-2091.jpg")
    background(welcomescrn)
    
#variable to control what screen you're on
screen = 0
# variables to set bird position on instruction screen
birdx = -1
birdy = 10
# variable to set smoke position on home screen
smokey = -60
smokeyslow = -60
#variable for lives 
lives = 3
# list of words on house level
houselist = ["moon", "painting", "car", "apple", "egg", "ladybug", "strawberry", "flower", "chocolate", "paperclip"]
# list of words on lake level
lakelist = ["pearl", "cherry", "ant", "star", "heart", "bowling ball", "screw", "clover", "lemons", "laptop"] 
# string of objects to find
objects = ""
# to control transparency of objects on both levels
a = 255
c = 255
d = 255
e = 255
f = 255
g = 255
h = 255
i = 255
j = 255
k = 255
# to change color of text on win screen
z = 0
# timer for levels
time = 70

def draw():
    global screen, font
    if screen == 0: # Home screen
        global smokex, smokey, smokeyslow, welcomescrn
        background(welcomescrn)
        font = createFont("Sweet Hipster.ttf", 120)
        fill(225, 225, 225)
        textFont(font)
        text("Welcome", 1410, 100)
        text("to", 1510, 190)
        textSize(200)
        text("Hidden Objects", 1210, 300)
        # Play button
        noStroke()
        fill(0, 0, 0, 40)
        rect(1400, 520, 300, 100, 30)
        textFont(font)
        textSize(100)
        fill(225, 225, 225)
        text("Play", 1490, 590)
        # Chimney smoke
        smoke = loadImage("Smoke-Effect-PNG-Image - Copy.png")
        image(smoke, 670, smokeyslow, 700, 300)
        movingsmoke = loadImage("Smoke-Effect-PNG-Image.png")
        image(movingsmoke, 670, smokey, 700, 300)
        # moving smoke
        smokey = smokey - 5
        smokeyslow = smokeyslow - 2.5
        if smokey == -280:
            smokey = -60
        if smokeyslow == -220:
            smokeyslow = -60

  # Instruction screen          
    elif screen == 1:
        global b, birdx, birdy
        b = loadImage("joanne-baez-screen-1920x1080-2016-11-29-16-25-21.jpg")
        background(b)
        # The bird flying by
        bird = loadImage("duck-34905_640.png")
        image(bird, birdx, birdy, 100, 100)
        birdx = birdx + 10
        # Instruction text
        textSize(100)
        fill(225, 225, 225)
        text("A list of words will be displayed at the bottom of the screen.", 300, 320) 
        text("Find and click all the corresponding images to win.", 410, 420)
        text("Make three mistakes and you lose.", 620, 520)
        text("You don't have a lot of time, but clicking an object adds time.", 280, 620) 
        text("Good luck.", 870, 720)
        # Next button
        text("Next", 1500, 975)
        fill(225, 225, 225, 40)
        noStroke()
        rect(1400, 900, 300, 100, 30)
    
    # Level options screen
    elif screen == 2: 
        #global select, house, lake
        select = loadImage("ruler-of-the-land-blood-art-forest-1920x1080.jpg")
        background(select)
        textSize(200)
        fill(225, 225, 225)
        text("Choose Level - ", 70, 180)
        # House lvl option
        house = loadImage("housepic.png")
        tint(255, 255)
        image(house, 390, 380, 420, 395)
        textSize(80)
        text("House", 550, 815)
        # Lake lvl option
        lake = loadImage("lakepic.png")
        tint(255, 255)
        image(lake, 1130, 385, 430, 410)
        text("Lake", 1315, 815)
        
    # House level
    elif screen == 3:
        global lives, houselist, houseImages, a, c, d, e, f, g, h, i, j, k, time
        room = loadImage("Lair_in_.txt_mode.png")
        background(room)
        # to display lives
        tint(255, 255)
        wood = loadImage("wood.jpg")
        image(wood, 820, 0, 280, 80)
        textSize(70)
        fill(255, 255, 255)
        text("Lives - " + str(lives), 885, 55)
        # to display list of words
        listdisp = loadImage("parchmentbackground.jpg")
        image(listdisp, 0, 900, 1920, 340)
        fill(0, 0, 0)
        textSize(80)
        #text(str(houselist), 115, 915, 1920, 300)
        text(objects, 215, 915, 1920, 300)
        # to update time
        time = time - 1
        # if time runs out
        if time == 0:
            screen = 6
        # to display time
        textSize(60)
        fill(102, 51, 0)
        text("Time -", 880, 1055)
        text(time, 980, 1055)
        # clickable images
        moon = loadImage("e9b59af57aeb98176d5d1bdb74dc725a.png")
        tint(255, a)
        image(moon, 10, 360, 40, 50)
        berry = loadImage("df0b3458fa1d0a31285feb8fb9e16807.png")
        tint(255, c)
        image(berry, 1175, 715, 40, 40)
        car = loadImage("2-2-car-transparent.png")
        tint(255, d)
        image(car, 1250, 178, 60, 40)
        flower = loadImage("PNGPIX-COM-Pansy-Flower-PNG-Image.png")
        tint(255, e)
        image(flower, 20, 100, 50, 50)
        painting = loadImage("Decorative_Painting_landscape.png")
        tint(255, f)
        image(painting, 290, 270, 70, 50)
        chocolate = loadImage("Chocolate-PNG-Clipart.png")
        tint(255, g)
        image(chocolate, 1270, 775, 60, 40)
        egg = loadImage("egg-157224_960_720.png")
        tint(255, h)
        image(egg, 1025, 500, 35, 25)
        pclip = loadImage("paper_clip_by_satans_comrade-d9ua14w.png")
        tint(255, i)
        image(pclip, 1463, 480, 20, 35)
        apple = loadImage("885102_apple_512x512.png")
        tint(255, j)
        image(apple, 958, 577, 20, 20)
        bug = loadImage("images_burned.png")
        tint(255, k)
        image(bug, 168, 765, 30, 30)
        
    # Lake level 
    elif screen == 4: 
        global lives, a, c, d, e, f, g, h, i, j, k, time
        lake = loadImage("44.jpg")
        background(lake)
        # to display lives
        tint(255, 255)
        wood = loadImage("wood.jpg")
        image(wood, 820, 0, 280, 80)
        textSize(70)
        fill(255, 255, 255)
        text("Lives - " + str(lives), 895, 55)
        # to display list of words
        listdisp = loadImage("parchmentbackground.jpg")
        image(listdisp, 0, 862, 1920, 340)
        fill(0, 0, 0)
        textSize(80)
        text(objects, 280, 890, 1920, 300)
        # to update time
        time = time - 1
        # if time runs out
        if time == 0:
            screen = 6
        # to display time
        textSize(60)
        fill(102, 51, 0)
        text("Time -", 865, 1040)
        text(time, 965, 1040)
        # clickable images
        pearl = loadImage("grey1.png")
        tint(255, a)
        image(pearl, 65, 765, 25, 20)
        cherry = loadImage("3-red-cherry-png-image-download-thumb.png")
        tint(255, c)
        image(cherry, 85, 16, 40, 45)
        ant = loadImage("ant-clipart-transparent-16.png")
        tint(255, d)
        image(ant, 700, 1, 90, 90)
        star = loadImage("685910_star_512x512.png")
        tint(255, e)
        image(star, 635, 525, 50, 50)
        heart = loadImage("drawn-heart-3.png")
        tint(255, f)
        image(heart, 845, 688, 27, 27)
        ball = loadImage("Fo4_bowling_ball.png")
        tint(255, g)
        image(ball, 1575, 810, 40, 40)
        screw = loadImage("5-screw-png-image.png")
        tint(255, h)
        image(screw, 553, 415, 45, 50)
        clover = loadImage("Irish_clover.png")
        tint(255, i)
        image(clover, 1890, 515, 30, 30)
        lemon = loadImage("lemon_PNG25191.png")
        tint(255, j)
        image(lemon, 500, 680, 45, 30)
        laptop = loadImage("laptop-notebook-png-image-image-with-transparent-background-18.png")
        tint(255, k)
        image(laptop, 1850, 130, 50, 40)
            
    # Win screen
    elif screen == 5:
        global z
        winbckgrnd = loadImage("Fantasy-Forest-World-Widescreen-1920x1080.jpg")
        background(winbckgrnd)
        textSize(200)
        # changing text color
        fill (z, z, z,)
        z = z + 10
        text("You Won!", 780, 300)
        # exit button
        textSize(100)
        text("Replay", 1665, 972)
        fill(255, 255, 255, 50)
        noStroke()
        rect(1580, 900, 300, 100, 30)
     
    # Loose screen   
    elif screen == 6: 
        global z
        lose = loadImage("Fantasy-Painting-Of-Fantasy-Forest-4K-Wallpaper-1920x1080.jpg")
        background(lose)
        textSize(170)
        # changing text color
        fill (z, z, z,)
        z = z + 10
        text("Better luck next time", 570, 250)
        # exit button
        textSize(100)
        text("Replay", 1665, 972)
        fill(255, 255, 255, 45)
        noStroke()
        rect(1580, 900, 300, 100, 30)

def emptyList(aList): # checks to see if the list of words is empty 
    if(aList == []): 
        return True 
    else:
        return False
    
def livesfunc(lives): # used to check if the player has lost all three lives
    if(lives == 0):
        return True
    else:
        return False

def isInside(x, y, w, h): # used to gauge if the user's click is inside a clickable object
    if((mouseX >= x and mouseX <= x + w) and (mouseY >= y and mouseY <= y + h)):
        return True
    else:
        return False
    
def makeString(aList): # make a string from list of objects
    global objects
    objects = ""
    if (len(aList) != 0):
        for x in aList[:-1]:
            objects = objects + x + ", "
        objects = objects + (aList[-1])
    return objects
        
def mouseClicked(): # handles all of the user's clicks
    global screen, lives, houselist, lakelist, a, c, d, e, f, g, h, i, j, k, time, z
    if (screen == 0): # click play button to change to instruction screen
        if(isInside(1400, 520, 300, 100) == True):
            screen = 1
            
    elif (screen == 1): # click next button to change to level screen
        if(isInside(1400, 900, 300, 100) == True): 
            screen = 2
            
    elif (screen == 2): # on the level select screen 
        if(isInside(390, 380, 420, 395) == True): # click picture of house to change to house level
            makeString(houselist)
            screen = 3
        elif(isInside(1130, 385, 430, 410) == True): # click picture of lake to change to lake level
            makeString(lakelist)
            screen = 4

    elif (screen == 3): # on house level --> setting up what happens when user clicks objects
        if(isInside(10, 360, 40, 50) == True): # moon clicked
            while a != 0: # nothing happens when the same place is clicked
                houselist.remove("moon")
                makeString(houselist)
                a = 0
                time = time + 5
        elif(isInside(1175, 715, 40, 40) == True): # strawberry clicked
            while c != 0: # nothing happens when the same place is clicked
                houselist.remove("strawberry")
                makeString(houselist)
                c = 0
                time = time + 5
        elif(isInside(1250, 178, 60, 40) == True): # car clicked
            while d != 0: # nothing happens when the same place is clicked
                houselist.remove("car")
                makeString(houselist)
                d = 0
                time = time + 5
        elif(isInside(20, 100, 50, 50) == True): # flower clicked
            while e != 0: 
                houselist.remove("flower")
                makeString(houselist)
                e = 0
                time = time + 5
        elif(isInside(290, 270, 70, 50) == True): # painting clicked
            while f != 0:
                houselist.remove("painting")
                makeString(houselist)
                f = 0
                time = time + 5
        elif(isInside(1270, 775, 60, 40) == True): # chocolate clicked
            while g != 0:
                houselist.remove("chocolate")
                makeString(houselist)
                g = 0
                time = time + 5
        elif(isInside(1025, 500, 35, 25) == True): # egg clicked
            while h != 0:
                houselist.remove("egg")
                makeString(houselist)
                h = 0
                time = time + 5
        elif(isInside(1463, 480, 20, 35) == True): # paperclip clicked
            while i != 0: # nothing happens when the same place is clicked
                houselist.remove("paperclip")
                makeString(houselist)
                i = 0
                time = time + 5
        elif(isInside(958, 577, 20, 20) == True): # apple clicked
            while j != 0:
                houselist.remove("apple")
                makeString(houselist)
                j = 0
                time = time + 5
        elif(isInside(168, 765, 30, 30) == True): # ladybug clicked
            while k != 0:
                houselist.remove("ladybug")
                makeString(houselist)
                k = 0
                time = time + 5
        else: # reduces lives when user clicks on background instead of object
            lives = lives - 1
            
        # checks to see if list is empty and if it is, changes to winning screen
        if(emptyList(houselist) == True):
            screen = 5
        # checks to see if all lives are lost
        if(livesfunc(lives) == True):
            screen = 6
        
    elif(screen == 4): # on lake level --> setting up what happens when user clicks objects
        if(isInside(65, 765, 25, 20) == True): # pearl clicked
            while a != 0: # nothing happens when the same place is clicked
                lakelist.remove("pearl")
                makeString(lakelist)
                a = 0
                time = time + 5
        elif(isInside(85, 16, 40, 45) == True): # cherry clicked
            while c != 0: # nothing happens when the same place is clicked
                lakelist.remove("cherry")
                makeString(lakelist)
                c = 0
                time = time + 5
        elif(isInside(700, 1, 90, 90) == True): # ant clicked
            while d != 0: # nothing happens when the same place is clicked
                lakelist.remove("ant")
                makeString(lakelist)
                d = 0
                time = time + 5
        elif(isInside(635, 525, 50, 50) == True): # star clicked
            while e != 0: 
                lakelist.remove("star")
                makeString(lakelist)
                e = 0
                time = time + 5
        elif(isInside(845, 688, 27, 27) == True): # heart clicked
            while f != 0: 
                lakelist.remove("heart")
                makeString(lakelist)
                f = 0
                time = time + 5
        elif(isInside(1575, 810, 40, 40) == True): # bowling ball clicked
            while g != 0: 
                lakelist.remove("bowling ball")
                makeString(lakelist)
                g = 0
                time = time + 5
        elif(isInside(553, 415, 45, 50) == True): # screw clicked
            while h != 0: 
                lakelist.remove("screw")
                makeString(lakelist)
                h = 0
                time = time + 5
        elif(isInside(1890, 515, 30, 30) == True): # clover clicked
            while i != 0: 
                lakelist.remove("clover")
                makeString(lakelist)
                i = 0
                time = time + 5
        elif(isInside(500, 680, 45, 30) == True): # lemon clicked
            while j != 0: 
                lakelist.remove("lemons")
                makeString(lakelist)
                j = 0
                time = time + 5
        elif(isInside(1850, 130, 50, 40) == True): # laptop clicked
            while k != 0: 
                lakelist.remove("laptop")
                makeString(lakelist)
                k = 0
                time = time + 5
        else: # reduces lives when user clicks on background instead of object
             lives = lives - 1
        
        # checks to see if list is empty 
        if(emptyList(lakelist) == True):
            screen = 5 # change to win screen
        # checks to see if all lives are lost
        if(livesfunc(lives) == True):
            screen = 6 # change to lose screen 
        
    elif (screen == 5): # on win screen 
        if(isInside(1580, 900, 300, 100) == True): # click replay button to reset and go back to choose level screen
            # reset lives count
            lives = 3
            # reset list of words
            houselist = ["moon", "painting", "car", "apple", "egg", "ladybug", "strawberry", "flower", "chocolate", "paperclip"]
            lakelist = ["pearl", "cherry", "ant", "star", "heart", "bowling ball", "screw", "clover", "lemons", "laptop"]
            # reset transparency of objects on levels
            a = 255
            c = 255
            d = 255
            e = 255
            f = 255
            g = 255
            h = 255
            i = 255
            j = 255
            k = 255
            # reset color of text on win/lose screen
            z = 0
            # reset timer for levels
            time = 70
            # back to level select screen
            screen = 1
                    
    elif (screen == 6): # on lose screen 
        if(isInside(1580, 900, 300, 100) == True): # click replay button to reset and go back to choose level screen
            # reset lives count
            lives = 3
            # reset list of words 
            houselist = ["moon", "painting", "car", "apple", "egg", "ladybug", "strawberry", "flower", "chocolate", "paperclip"]
            lakelist = ["pearl", "cherry", "ant", "star", "heart", "bowling ball", "screw", "clover", "lemons", "laptop"]
            # reset transparency of objects on levels
            a = 255
            c = 255
            d = 255
            e = 255
            f = 255
            g = 255
            h = 255
            i = 255
            j = 255
            k = 255
            # reset color of text on win/lose screen
            z = 0
            # reset timer for levels
            time = 70
            # back to level select screen
            screen = 1
            
