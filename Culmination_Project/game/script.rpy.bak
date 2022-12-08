# The script of the game goes in this file.


#This is a fade to white transition
define fade = Fade(0.5, 0.0, 0.5, color="#fff")

#Movie backgrounds
image walk_hall = Movie(play="images/hallway.webm")

# The game starts here.

label start:
    stop music 
    $ renpy.movie_cutscene("scene-1.webm") 
    #Asks player for name
    $ player =  renpy.input("Hey, What's your name?", default = "Cameron") 

    $ player = player.strip()
    

    #This is a default name
    if player == "":
        $ player = "Cameron"

    scene bg blue with fade
    play music "audio/scene1.ogg" volume 0.5
    show michael neutral with fade:
    #This is the default for the character talking to the player
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32

    
#This is Scene 1
    #These display lines of dialogue.
    play sound "audio/micheal-happy.ogg" volume 0.2
    m "Hey [player]! How are you feeling? "
    hide michael neutral

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

    show michael neutral with dissolve:
    p "{cps=20}So...what happens now?{/cps}"

    play sound "audio/micheal-happy.ogg" volume 0.2
    m "Good Question! So you have to go up to Dearth, and go to our processing center!"

    p "Dearth?"

    play sound "audio/micheal-happy.ogg" volume 0.2
    m "Oh! That’s the name of the Afterlife. You know, dearth, it means the lack of. You know, lack of life in the Afterlife."

    play sound "audio/micheal-happy.ogg" volume 0.2
    m "Also, it’s just a play on words of Dead Earth, since everything is dead and it’s like Earth."

    p "Is it like Hell? Heaven? Purgatory?{cps=15}....or Florida?{/cps}"

    show michael happy with dissolve:
        xpos 0.25, ypos 0 zpos 1.0 yzoom 1.0 zoom 0.32
        ease 1.3 xpos -0.1 ypos 0.3 

    show michael neutral with dissolve:
        xpos -0.1 ypos 0.3 zpos 1.0 yzoom 1.0 zoom 0.32

    play sound "audio/micheal-happy.ogg" volume 0.2
    m "Crazy that you know about that! Let’s get you to the processing center to find out!"

    p "Processing Center?"
    
    play sound "audio/micheal-happy.ogg" volume 0.2
    m "Don’t worry, you’ll see, just come in with me."
    
    stop music fadeout 0.5
    play sound "audio/elevator-ding.ogg" volume 0.2
    show elevator with dissolve
    
    pause 1.0

#This is Scene 2
    scene bg elevatorearth with dissolve
    play music "audio/elevator.ogg" volume 1.0
    show michael nervous with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32

    play sound "audio/micheal-neutral.ogg" volume 0.1
    m "{cps=10}So....{/cps} how was the weather down there?"

    p "{cps=5}...{/cps}"

    pause 0.8
    show michael nervous right with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32

    play sound "audio/micheal-neutral.ogg" volume 0.1
    m "{cps=10}....{/cps}Do you come here often?"

    
    play sound "audio/elevator-ding.ogg" volume 0.2
    show bg elevatordearth

    menu:
        
        "{b}Too soon...{b}":

            call Nervous

        "Really?":
            call Nervous

        "Good One. (Sarcastic)":
            call Nervous

    pause 0.6
    p "{cps=5}...{/cps}"

    
    show bg elevatorintake 
    
    
    play sound "audio/elevator-ding.ogg" volume 0.2
    show michael happy with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    m "Alright, this is our floor! Right, this way!"
    play sound "audio/hallway.ogg" volume 0.1 

    stop music fadeout 0.5
    hide michael happy
    play music "audio/hallway.ogg" fadein 0.3 volume 0.2
    
    $ renpy.movie_cutscene("hallway.webm") 
    stop sound fadeout 0.5
    
    show bg reflection with dissolve
    pause 0.7
    p "{cps=5}...{/cps}"

    menu:
        "{b}Oh my God! Why do I look like this?! Where are my hands?{b}":
            call Questioning2

        "Why do I have this sheet over me?":
            call Sheet

        "(Say Nothing)":
            call Nothing
    
    play sound "audio/micheal-neutral.ogg" volume 0.2
    m "Now let's go into the intake room!"
#This is Scene 3

    scene bg placeholder with fade
    play sound "audio/micheal-mad.ogg" volume 0.2
    show michael really angry with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    m "Why does Rafael keep putting chairs here?! I told him we keep getting complaints from HR for being insensitive!"

    play sound "audio/micheal-neutral.ogg" volume 0.1
    show michael oops with dissolve
    m "{i}sigh{/i}...Anyway just sit tight over there."

    play sound "audio/micheal-neutral.ogg" volume 0.1
    show michael nervous right with dissolve
    m "Oops! I mean...float?"

    p "umm...sure."
    hide michael with dissolve

    play sound "audio/lucrecia-mad.ogg" volume 0.2
    show lucrecia angry right with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    l "Ay, Dios Mio! Rafael keeps putting these chairs here! We’re going to get more complaints from the new souls!"

    play sound "audio/lucrecia-happy.ogg" volume 0.2
    show lucrecia with dissolve
    show lucrecia happy with dissolve
    l "Hola mi amor! Welcome to Dearth! I’m Lucrecia the ambassador for Heaven!"
    hide lucrecia with dissolve

    
    show nora angry right with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    n "Jesus! Raf needs to stop with these chairs! It’s not funny anymore! "
    show nora with dissolve
    show nora happy with dissolve
    n "Hellooooo [player], I’m Nora, welcome! I’m the ambassador for Purgatory, and can’t wait to hear about you!"
    hide nora with dissolve

    show beazley angry right with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    b "{i}sigh{/i}...Can we just write Rafael up for these chairs?"
    show beazley with dissolve
    show beazley happy with dissolve
    b "Hello, I’m Beazley, welcome, welcome. I’m the ambassador of Hell, and I can't wait to hear from you."
    hide beazley with dissolve

    show nora angry right with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    n "{b}BEAZLEY! CHANGE THOSE RIDICULOUS SHEETS! YOU’RE NOT SATAN!{/b}"
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

    show bg placeholder with fade:
    #This is just the placeholder for the background
        pos (0, 0) zpos 1.0 yzoom 1.0 zoom 3.5

    # This ends the game.
    return

#This is the response to the choices

#This is Scene 1
    label Questioning:

        play sound "audio/micheal-happy.ogg" volume 0.1
        show michael neutral with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "Well [player], you just died. I’m Micheal, {cps=15}aaaaaand{/cps} this is the Afterlife!"
        
        #This returns you to continue the dialogue
        return

    
    label Trash:

        play sound "audio/micheal-happy.ogg" volume 0.1
        show michael neutral with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "Sucks to hear about that bud, you’ll feel better soon though. Anyways, welcome to the Afterlife! I’m the angel Micheal!"
        return

    label Peace:

        play sound "audio/micheal-happy.ogg" volume 0.1
        show michael happy with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "Well, you took that surprisingly well. Anyways, welcome to the Afterlife [player]! I’m the angel Micheal!"

        return

    label Okay:

        play sound "audio/micheal-happy.ogg" volume 0.1
        show michael happy with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "That’s good. Welcome to the Afterlife [player]! I’m the angel Micheal!"
        return

#This is Scene 2
    label Nervous:
        play sound "audio/micheal-neutral.ogg" volume 0.1
        show michael oops with dissolve:
            subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32     
        m "I know...sorry, just making small talk."
        return

#This is Scene 3
    label Questioning2:
        show michael happy with dissolve:
            subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
        m "You look good [player]! Also, you don’t need them anymore, you’re a ghost!"
        return

    label Sheet:
        show michael happy with dissolve:
            subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
        m "You’re a ghost silly! Have you never seen Casper? A Christmas Carol? GHOSTBUSTERS?"
        return

    label Nothing:
        show michael neutral right with dissolve:
            subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
        m "Come on, we don’t have all of eternity.{cps=15} Oh, wait....{/cps}we do, but I have better things to do on a Tuesday"
        return
    
    