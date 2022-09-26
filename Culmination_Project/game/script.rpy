# The script of the game goes in this file.


#This is a fade to white transition
define fade = Fade(0.5, 0.0, 0.5, color="#fff")


# The game starts here.

label start:
    #Asks player for name
    $ player =  renpy.input("Hey, What's your name?", default = "Cameron")

    $ player = player.strip()

    #This is a default name
    if player == "":
        $ player = "Cameron"

    scene scene1 bg with fade
    show michael neutral with fade:
    #This is the default for the character talking to the player
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32

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
        
        "I feel...okay, surprisingly.":
            call Okay

    show michael neutral with dissolve
    p "{cps=20}So...what happens now?{/cps}"

    m "Good Question! So you have to go up to Dearth, and go to our processing center!"

    p "Dearth?"

    m "Oh! That’s the name of the Afterlife. You know, dearth, it means the lack of. You know, lack of life in the Afterlife."

    m "Also, it’s just a play on words of Dead Earth, since everything is dead and it’s like Earth."

    p "Is it like Hell? Heaven? Purgatory?{cps=15}....or Florida?{/cps}"

    show michael happy with dissolve
    m "Crazy that you know about that! Let’s get you to the processing center to find out!"

    show michael neutral with dissolve
    p "Processing Center?"

    m "Don’t worry, you’ll see, just come in with me."

    scene scene1 bg
    show michael nervous with fade:
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    m "{cps=10}So....{/cps} how was the weather down there?"

    p "{cps=5}...{/cps}"

    show michael nervous right with dissolve
    m "{cps=10}....{/cps}Do you come here often?"

    p "Too soon."

    show michael oops with dissolve
    m "I know...sorry, just making small talk."

    show bg placeholder with fade:
    #This is just the placeholder for the background
        pos (0, 0) zpos 1.0 yzoom 1.0 zoom 3.5

#This is Scene 2
    show michael happy:
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32

    m "Alright, this is our floor! Right, this way!"

    hide michael happy
    show bg placeholder with fade:
        pos (0, 0) zpos 1.0 yzoom 1.0 zoom 3.5
    
    menu:
        "{b}Oh my God! Why do I look like this?! Where are my hands?{b}":
            call Questioning2

        "Why do I have this sheet over me?":
            call Sheet

        "(Say Nothing)":
            call Nothing

    show bg placeholder with fade:
    #This is just the placeholder for the background
        pos (0, 0) zpos 1.0 yzoom 1.0 zoom 3.5

#This is Scene 3

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
        m "Well [player], you just died. I’m Micheal, {cps=15}aaaaaand{/cps} this is the Afterlife!"
        #This returns you to continue the dialogue
        return

    label Trash:
        m "Sucks to hear about that bud, you’ll feel better soon though. Anyways, welcome to the Afterlife! I’m the angel Micheal!"
        return

    label Peace:
        show michael happy with dissolve
        m "Well, you took that surprisingly well. Anyways, welcome to the Afterlife [player]! I’m the angel Micheal!"
        return

    label Okay:
        show michael happy with dissolve
        m "That’s good. Welcome to the Afterlife [player]! I’m the angel Micheal!"
        return

#This is Scene 2
    label Questioning2:
        show michael happy:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "You’ll look good [player]! Also, you don’t need them anymore, you’re a ghost!"
        return

    label Sheet:
        show michael neutral right:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "God got tired after 4000 BC and just started throwing sheets, you can just spruce it up after intake."
        return

    label Nothing:
        show michael neutral right:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "Come on, we don’t have all of eternity.{cps=15} Oh, wait....{/cps}we do, but I have better things to do on a Tuesday"
        return