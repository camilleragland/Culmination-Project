# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[player]")

define m = Character("Micheal")

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

    #These display lines of dialogue.
    m "Hey [player]! How are you feeling? "

    #This is a menu of choices, and {b} bolds text
    menu:
        "{b}What just happened? Who are you? Where am I?{b}":

            #This calls the responses of the choices
            call Questioning

        "Like absolute trash":
            call Trash 

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
    label Questioning:
        m "Well [player], you just died. I’m Micheal, aaaaaand this is the Afterlife!"
        #This returns you to continue the dialogue
        return

    label Trash:
        m "Sucks to hear about that bud, you’ll feel better soon though. Anyways, welcome to the Afterlife! I’m the angel Micheal!"
        return