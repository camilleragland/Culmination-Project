# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[player]", color = "#FFFFFF")

define m = Character("Micheal", color = "#F1C0E9")

define n = Character("Nora")

define l = Character("Lucrecia")

define b = Character("Beazley")

define j = Character("Jaisen")

# The game starts here.

label start:
    #Asks player for name
    $ player =  renpy.input("Hey, What's your name?", default = "Cameron")

    $ player = player.strip()

    #This is a default name
    if player == "":
        $ player = "Cameron"

    show bg placeholder:
    #This is just the placeholder for the background
     pos (0, 0) zpos 1.0 yzoom 1.0 zoom 3.5 

    show character:
    #This is the default for the character talking to the player
        subpixel True pos (0.35, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32

#This is Scene 1
    #These display lines of dialogue.
    m "Hey [player]! How are you feeling? "

    #This is a menu of choices, and {b} bolds text
    menu:
        "{b}What just happened? Who are you? Where am I?{b}":

            #This calls the responses of the choices
            call Questioning

        "Like absolute trash":
            call Trash 

        "I feel at peace.":
            call Peace
        
        "I feel…okay, surprisingly.":
            call Okay

    p "So..what happens now?"

    m "Good Question! So you have to go up to Dearth, and go to our processing center!"

    p "Dearth?"

    m "Oh! That’s the name of the Afterlife. You know, dearth, it means the lack of. You know, lack of life in the Afterlife."

    m "Also, it’s just a play on words of Dead Earth, since everything is dead and it’s like Earth."

    p "Is it like Hell? Heaven? Purgatory?....or Florida?"

    m "Crazy that you know about that! Let’s get you to the processing center to find out!"

    p "Processing Center?"

    m "Don’t worry, you’ll see, just come in with me."

    m "So…how was the weather down there?"

    p "..."

    m "....Do you come here often?"

    p "Too soon."

    m "I know...sorry, just making small talk."

    #Hides last sprite
    hide character

    #This is the default for the character on the right
    show character:
        subpixel True pos (0.7, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    
    m "Once you add a story, pictures, and music, you can release it to the world!"

    hide character

    #This is the default for the character on the Left
    show character:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
        
    m "Hello, World!"

    # This ends the game.
    return

#This is the response to the choices

#This is Scene 1
    label Questioning:
        m "Well [player], you just died. I’m Micheal, aaaaaand this is the Afterlife!"
        #This returns you to continue the dialogue
        return

    label Trash:
        m "Sucks to hear about that bud, you’ll feel better soon though. Anyways, welcome to the Afterlife! I’m the angel Micheal!"
        return

    label Peace:
        m "Well, you took that surprisingly well. Anyways, welcome to the Afterlife [player]! I’m the angel Micheal!"
        return

    label Okay:
        m "That’s good. Welcome to the Afterlife [player]! I’m the angel Micheal!"
        return