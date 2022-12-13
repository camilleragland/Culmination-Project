# The script of the game goes in this file.

#This is where the choices of the game add up
default heaven = 0 
default hell = 0
default purgatory = 0
default florida = 0 
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
        
        "What just happened?! Who are you?! Where am I?!":

            #This calls the responses of the choices
            call Questioning from _call_Questioning

        "Like absolute trash":
            call Trash from _call_Trash 

        "I feel at peace.":
            call Peace from _call_Peace
        
        "I feel...okay, surprisingly.":
            call Okay from _call_Okay

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
        xpos -0.1, ypos 0.3 zpos 1.0 yzoom 1.0 zoom 0.32
        ease 1.3 xpos -0.1 ypos 0.3 

    show michael neutral with dissolve:
        

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
        
        "Too soon...":

            call Nervous from _call_Nervous

        "Really?":
            call Nervous from _call_Nervous_1

        "Good One. (Sarcastic)":
            call Nervous from _call_Nervous_2

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
        "Oh my God! Why do I look like this?! Where are my hands?!":
            call Questioning2 from _call_Questioning2

        "Why do I have this sheet over me?":
            call Sheet from _call_Sheet

        "(Say Nothing)":
            call Nothing from _call_Nothing
    
    play sound "audio/micheal-neutral.ogg" volume 0.2
    m "Now let's go into the intake room!"
    stop sound fadeout 0.5

#This is Scene 3
    play music "audio/judgement.ogg" volume 0.5 fadein 0.5
    scene bg judgement with fade
    play sound "audio/micheal-mad.ogg" volume 0.2
    show michael really angry with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    m "Why does Rafael keep putting chairs here?! I told him we keep getting complaints from Ghostly Resources for being insensitive!"

    play sound "audio/micheal-neutral.ogg" volume 0.1
    show michael oops with dissolve
    m "{i}sigh{/i}...Anyway just sit tight over there."

    play sound "audio/micheal-neutral.ogg" volume 0.1
    show michael nervous right with dissolve
    m "Oops! I mean...float?"

    menu: 
        "ummm...sure.":
            call Confused from _call_Confused

        "I'll wait here then":
            call Umsure from _call_Umsure

        "I'm going to complain to Human Resources!":
            call Hr from _call_Hr

    play sound "audio/lucrecia-mad.ogg" volume 0.2
    show lucrecia angry right with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    l "Ay, Dios Mio! Rafael keeps putting these chairs here! We’re going to get more complaints from the new souls!"

    play sound "audio/lucrecia-happy.ogg" volume 0.2
    show lucrecia with dissolve
    show lucrecia happy with dissolve
    l "Hola mi amor! Welcome to Dearth! I’m Lucrecia the ambassador for Heaven!"
    hide lucrecia with dissolve

    play sound "audio/nora-mad.ogg" volume 0.2
    show nora angry right with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    n "Jesus! Raf needs to stop with these chairs! It’s not funny anymore! "
    show nora with dissolve
    play sound "audio/nora-happy.ogg" volume 0.2
    show nora happy with dissolve
    n "Hellooooo [player], I’m Nora, welcome! I’m the ambassador for Purgatory, and can’t wait to hear about you!"
    hide nora with dissolve

    play sound "audio/beazley-mad.ogg" volume 0.4
    show beazley angry right with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    b "{i}sigh{/i}...Can we just write Rafael up for these chairs?"
    show beazley with dissolve
    play sound "audio/beazley-happy.ogg" volume 0.3
    show beazley happy with dissolve
    b "Hello, I’m Beazley, welcome, welcome. I’m the ambassador of Hell, and I can't wait to hear from you."

    play sound "audio/nora-mad.ogg" volume 0.2
    show nora angry left with hpunch:
        subpixel True pos (0.5, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    n "{b}BEAZLEY! CHANGE THOSE RIDICULOUS SHEETS! YOU’RE NOT SATAN!{/b}"

    play sound "audio/beazley-mad.ogg" volume 0.4
    show beazley sad right with dissolve
    b "I’m just getting into character honey! Satan asked me to cover his shift for today!"

    play sound "audio/nora-mad.ogg" volume 0.2
    n "Well, you’re not Satan, Beazley! Now take them off!"

    play sound "audio/beazley-mad.ogg" volume 0.4
    show beazley angry right with dissolve 
    b "I’LL TAKE THEM OFF WHEN HELL FREEZES OVER!"
    hide nora with dissolve

    show lucrecia neutral left with dissolve:
        subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/chewing.ogg" volume 1.0
    show popcorn with dissolve:
        subpixel True pos (0.5, 0.45) zpos 1.0 yzoom 1.0 zoom 0.32
    l "{i}Crunch, Crunch, Crunch{/i}"

    hide lucrecia with dissolve
    hide popcorn with dissolve

    
    play sound "audio/nora-mad.ogg" volume 0.2
    show nora angry left with hpunch:
        subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    n "{b}WELL, IT WAS 5 DEGREES YESTERDAY!{/b}"
    
    play sound "audio/beazley-neutral.ogg" volume 0.4
    show beazley neutral right with dissolve
    b "{cps=10}...oh...{/cps}"
    play sound "audio/beazley-happy.ogg" volume 0.3
    show beazley happy closed with dissolve
    b "Good thing this is insulated then!"
    
    play sound "audio/nora-happy.ogg" volume 0.2
    show nora neutral right with dissolve
    n "{i}sigh...{\i}"

    hide beazley with dissolve
    hide nora with dissolve 


    show jaisen with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    show booze with dissolve:
        subpixel True pos (0.3, 0.45) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/jaisen-neutral.ogg" volume 0.5
    j "Haha! Raf is hilarious with these chairs man!"

    show lucrecia neutral left:
        subpixel True pos (0.5, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/lucrecia-neutral.ogg" volume 0.3
    l "Aye Dio..."
    hide lucrecia

    show nora angry left with dissolve:
        subpixel True pos (0.5, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/nora-neutral.ogg" volume 0.2
    n "Really? The Booooze Jaisen?"

    play sound "audio/jaisen-happy.ogg" volume 0.4
    show jaisen happy with dissolve
    j "What? It’s 5’0 clock always in Florida!"
    j "Nice sheet, Beazley!"

    hide nora with dissolve

    show beazley happy closed with dissolve:
        subpixel True pos (0.5, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/beazley-happy.ogg" volume 0.4
    b "Thanks! They’re insulated. It’s 5 degrees in Hell right now."
    
    hide beazley with dissolve
    hide jaisen with dissolve
    hide booze with dissolve

    show michael really angry with vpunch:
        subpixel True pos (0.5, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/micheal-mad.ogg" volume 0.3
    m "Hey guys! Can you get started here? I have a 7:00 bowling party to go to in Purgatory, and I don’t want to be late."
    
#This is Scene 4
    scene bg panel with fade
    play sound "audio/nora-neutral.ogg" volume 0.2
    show nora with dissolve:
        xpos 0.25, ypos 0 zpos 1.0 yzoom 1.0 zoom 0.32
    n "So we’re going to ask you some questions and see what’s the best place on Dearth where you’ll feel right at home."
    n "Got it?"

    p "Yeah, I think I understand."

    play sound "audio/nora-neutral.ogg" volume 0.2
    n "Great! We’re going to start in order, from left to right. Lucrecia you’re up first."
    hide nora with dissolve

#Question 1
    play sound "audio/lucrecia-happy.ogg" volume 0.2
    show lucrecia happy with dissolve:
        xpos 0.25, ypos 0 zpos 1.0 yzoom 1.0 zoom 0.32
    l "Thank you, Mija."
    show lucrecia
    l "I have a good question. How many meals a day do you eat?"

    menu:
        
        "Once a day":

            call Eating from _call_Eating

        "Twice a day":
            call Eating from _call_Eating1

        "Three times a day":
            call Eating from _call_Eating2

        "I don't know? All the time, maybe?":
            call Eating from _call_Eating3
    
    menu: 

        "I do eat more...sometimes!":
            call Still from _call_Still
        "No, I don't!":
            call Eatmore from call_Eatmore

    hide lucrecia

#Question 2
    show nora with dissolve:
        xpos 0.25, ypos 0 zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/nora-neutral.ogg" volume 0.2
    n "Okay, I’m next."
    n "Alright let's see"

    show notepad with dissolve:
        subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/writing.ogg" volume 1.5
    show pencil with dissolve:
        subpixel True pos (0.6, 0.25) zpos 1.0 yzoom 1.0 zoom 0.15

    n "Ahem, here's a serious question."

    play sound "audio/nora-neutral.ogg" volume 0.2
    n "Have you killed a bug before?"

    menu: 
        "Yes.":
            call Bug from _call_Bug
        "No.":
            call NoBug from _call_NoBug

    hide nora with dissolve

#Question 3
    show beazley with dissolve:
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32

    play sound "audio/beazley-neutral.ogg" volume 0.2 
    b "Alright, I’m next."
    b "Have you stolen anything before?"

    menu: 
        "Yes.":
            call Stole from _call_Stole
        "No.":
            call Notstolen from _call_Notstolen
        "Maybe...":
            call Trust from _call_Trust

    hide beazley with dissolve

#Question 4
    show jaisen happy with dissolve: 
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/jaisen-happy.ogg" volume 0.2 
    j "My question is next! Me! I have one!"
    hide jaisen with dissolve 

    show nora with dissolve: 
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/nora-neutral.ogg" volume 0.2 
    n "{i}sigh{/i}...what is it Jaisen?"
    hide nora with dissolve

    show jaisen with dissolve:
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/jaisen-happy.ogg" volume 0.4
    j "Do you like the Jacksonville Jaguars?"
    hide jaisen with dissolve

    show nora angry right with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/nora-mad.ogg" volume 0.2 
    n "Jaisen, that's not the kind of question you ask!"
        
    show jaisen angry left with dissolve: 
        subpixel True pos (0.5, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/jaisen-mad.ogg" volume 0.6
    j "It’s my realm of Dearth and I can ask whatever I like."

    show nora angry right with dissolve:
        subpixel True pos (0, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/nora-mad.ogg" volume 0.2 
    n "How does that help us learn anything about [player]?!"

    show jaisen happy with dissolve: 
        subpixel True pos (0.5, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/jaisen-happy.ogg" volume 0.4
    j "So I can see if they’re cool or not. Obviously, Nora."

    hide jaisen with dissolve
    show beazley neutral left with dissolve:
        subpixel True pos (0.5, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/beazley-neutral.ogg" volume 0.5
    b "Just let him ask his questions, I don’t want Micheal coming back annoyed."

    show nora neutral left with dissolve
    play sound "audio/nora-neutral.ogg" volume 0.2 
    n "Fine, ask away Jaisen."      
    
    hide nora with dissolve
    hide beazley with dissolve

    show jaisen happy with dissolve: 
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/jaisen-happy.ogg" volume 0.4 
    j "So do you like the Jacksonville Jaguars?"

    menu: 
        "Who?":
            call Who from _call_Who
        "No.":
            call Nojaguars from _call_Nojaguars
        "I don't watch that kind of sport":
            call Nosport from _call_Nosport
        "YEAH!!!":
            call Jaguars from _call_Jaguars
    hide jaisen
#Question 5
    show lucrecia with dissolve: 
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/lucrecia-neutral.ogg" volume 0.2 
    l "Alright this is the last question"
    l "Are you good with technology?"

    menu: 
        "Yeah":
            call Fix from _call_Fix
        "No.":
            call Nofix from _call_NoFix
    
    hide lucrecia with dissolve

    show beazley happy with dissolve:
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    b "We're all done! We're going to go figure out where you're home will be."

#Last Scene
    scene bg judgement with fade 
    show nora happy with dissolve: 
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/nora-happy.ogg" volume 0.2 
    n "We're done and came with the conclusion here are your results!"

    screen results:
        image "results.png"
        text "{size= 150}Results by Points{/size}" color "#000000" xalign 0.5
        text "{size= 120}Florida: [florida]{/size}" color "#3d57ee" xalign 0.5 yalign 0.2
        text "{size= 120}Hell: [hell]{/size}" color "#e86f73" xalign 0.5 yalign 0.3
        text "{size= 120}Purgatory: [purgatory]{/size}" color "#5b826a" xalign 0.5 yalign 0.4
        text "{size= 120}Heaven: [heaven]{/size}" color "#ca8833" xalign 0.5 yalign 0.5


    show screen results

    n "So what do you think?"

    menu: 
        "I expected this":
            call Expected from _call_Expected
        "Are you sure about this":
            call Unsure from _call_Unsure

    hide screen results
    hide nora with dissolve

    show beazley happy with dissolve:
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/beazley-happy.ogg" volume 0.2
    b "Glad you we can help you out with everything!"
    hide beazley with dissolve

    show lucrecia happy with dissolve: 
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/lucrecia-happy.ogg" volume 0.2
    l "I'm going to go home and watch my family, my grandaughter is graduating soon"
    hide lucrecia with dissolve

    show jaisen happy with dissolve:
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/beazley-happy.ogg" volume 0.2
    j "I'm going to go play with fireworks and watch Shawnshake Redemption again!"
    hide jaisen with dissolve

    show michael happy with dissolve:
        subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
    play sound "audio/micheal-happy.ogg" volume 0.2
    m "Great you guys are done! Now I can go to my bowling party in Purgatory"
    stop music fadeout 0.5
    $ renpy.movie_cutscene("credits.webm") 

    # This ends the game.
    return

#This is the response to the choices

#This is Scene 
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
        play sound "audio/micheal-happy.ogg" volume 0.2
        show michael happy with dissolve:
            subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
        m "You look good [player]! Also, you don’t need them anymore, you’re a ghost!"
        return

    label Sheet:
        play sound "audio/micheal-happy.ogg" volume 0.2
        show michael happy with dissolve:
            subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
        m "You’re a ghost silly! Have you never seen Casper? A Christmas Carol? GHOSTBUSTERS?"
        return

    label Nothing:
        play sound "audio/micheal-neutral.ogg" volume 0.2
        show michael neutral right with dissolve:
            subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
        m "Come on, we don’t have all of eternity.{cps=15} Oh, wait....{/cps}we do, but I have better things to do on a Tuesday"
        return
    
#This is Entering Room Scene
    label Confused:
        play sound "audio/micheal-happy.ogg" volume 0.2
        show michael happy with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "Thanks [player]!"
        return

    label Umsure:
        play sound "audio/micheal-happy.ogg" volume 0.2
        show michael happy with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "Thanks [player]!"
        return

    label Hr:
        play sound "audio/micheal-neutral.ogg" volume 0.2
        show michael nervous with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "We don't have that..but we do have ghostly resources"
        show michael oops with dissolve:
        m "Please don't complain, we already have too many."
        hide michael with dissolve
        return

#This is Question 1
    label Eating:
        play sound "audio/lucrecia-neutral.ogg" volume 0.2
        show lucrecia with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        l "You need to eat more!"
        $ heaven += 1
        $ hell += 1
        $ purgatory += 1
        $ florida += 1
        return
    
    label Still:
        play sound "audio/lucrecia-mad.ogg" volume 0.2
        show lucrecia angry with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        l "Still! Eat more than that!"
        return

    label Eatmore:
        play sound "audio/lucrecia-mad.ogg" volume 0.2
        show lucrecia angry with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        l "That’s what someone who needs to eat more would say!"
        return
#This is Question 2
    label Bug:
            play sound "audio/nora-mad.ogg" volume 0.2
            show nora super angry with dissolve:
                subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
            n "{b}HOW DARE YOU! BUGS ARE PRECIOUS! DAMNATION! SEND THEM TO FLORIDA!{\b}"

            $ heaven += 1
            $ hell += 1
            $ florida += 1

            hide nora with dissolve
            hide pencil with dissolve
            hide notepad with dissolve

            show beazley neutral left with dissolve: 
                subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
            play sound "audio/beazley-neutral.ogg" volume 0.2 
            b " Now, honey, not everyone likes bugs, and they sometimes kill them"
            return

    label NoBug:
            play sound "audio/nora-happy.ogg" volume 0.2
            show nora excited with dissolve:
                subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
            n "{b}THANK YOU!{\b} Aren’t they precious?"

            $ heaven += 1
            $ hell += 1
            $ purgatory += 1
            return
#This is Question 3
    #Stolen
    label Stole:
            play sound "audio/beazley-neutral.ogg" volume 0.2
            show beazley with dissolve:
                subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
            b "What was it?"
            hide beazley with dissolve 

            menu: 
                "Okay, okay I can explain....":
                    call BigItem from _call_BigItem
                    return
                "Are you lying?":
                    call SmallItem from _call_SmallItem
                    return
                "I really needed it, it was actually essential":
                    call Essential from _call_Essential
                    return
                "I returned it! Please don’t send me to hell! I forgot I had it in my hand!":
                    call Accident from _call_Accident
                    return

            return
    #Not Stolen
    label Notstolen:
            play sound "audio/beazley-neutral.ogg" volume 0.2
            show beazley with dissolve:
                subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
            b "Are you lying?"

            menu: 
                "Ummmm....":
                    call Trust from _call_Trust1
                    return
                "Fine...yes...":
                    call Stole from _call_Stole1
                    return
                "Of course not!":
                    $ heaven += 1
                    $ hell += 1
                    $ purgatory += 1
                    return
            return 

    label Trust:
            play sound "audio/beazley-happy.ogg" volume 0.2
            show beazley happy with dissolve:
                subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
            b "Come on, you can trust me. Isn’t this a trustworthy-looking sheet?"

            menu: 
                "Fine, I've stolen stomething before.":
                    call Stole from _call_Stole2
                    return
                "Nope, never have stolen anything.":
                    $ purgatory += 2
                    $ heaven +=2
                    return
            return
    #Big Item
    label BigItem:
            hide beazley with dissolve
            show jaisen happy with dissolve:
                subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
            j "Nice dude! Was it a TV? An XBOX?"
            $ hell += 1

            hide jaisen with dissolve
            return

    #Small Item
    label SmallItem:
            play sound "audio/beazley-neutral.ogg" volume 0.2
            show beazley with dissolve:
                subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
            b "It's okay, I've stolen a few things in my lifetime"
            $ hell += 2
            $ purgatory += 2
            $ heaven +=1
            $ florida += 2

            return

    #Essential 
    label Essential:
        play sound "audio/lucrecia-happy.ogg" volume 0.2
        hide beazley with dissolve
        show lucrecia with dissolve:
                subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        l "Things happen, so it's alright."
        $ hell += 1
        $ purgatory += 1
        $ heaven +=2
        $ florida += 1

        hide lucrecia with dissolve
        return

    #Accident
    label Accident:
            play sound "audio/nora-happy.ogg" volume 0.2
            hide beazley with dissolve 
            show nora happy with dissolve:
                    subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
            n "It's okay, that's happened to me before at Claire's"
            $ hell += 1
            $ purgatory += 2
            $ heaven +=2

            hide nora with dissolve
            return
#This is Question 4
    label Who:

            play sound "audio/jaisen-mad.ogg" volume 0.6
            show jaisen super angry with dissolve:
                subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
            m "What do you mean who?"
            $ florida -= 1

            return
    
    label Nojaguars:

        play sound "audio/jaisen-mad.ogg" volume 0.6
        show jaisen really sad with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        j "That sucks for you."

        show jaisen happy with dissolve: 
        $ team =  renpy.input("Who's your favorite then?", default = "Baltimore Ravens")

        play sound "audio/jaisen-happy.ogg" volume 0.4 
        j "Oh! [team] is cool too!"
        $ florida += 1
        return

    label Nosport:

        play sound "audio/jaisen-mad.ogg" volume 0.6
        show jaisen sad with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "That sucks, Football is one of the main activities in Florida"

        return

    label Jaguars:

        play sound "audio/jaisen-happy.ogg" volume 0.4
        show jaisen happy with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        m "I knew there was something special about you!"
        $ florida += 2
    
        return
#This is Question 5
    label Fix:
        show lucrecia happy with dissolve: 
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        play sound "audio/lucrecia-happy.ogg" volume 0.2 
        l "Great! Then can you fix my alarm clock?"
        show clock broken with dissolve:
            subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
        menu: 
            "Sure! I just need to set it":
                call Alarm from _call_Alarm
            "I'm not sure how to...":
                call Noalarm from _call_Noalarm
        return

    label Nofix:
        show lucrecia sad with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        play sound "audio/lucrecia-mad.ogg" volume 0.2 
        l "My grandaughter would have done it...."
        return
    label Alarm:
        show clock repaired with dissolve:
            subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32
        show lucrecia happy with dissolve: 
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        play sound "audio/lucrecia-happy.ogg" volume 0.2 
        l "Thank you! Can you fix my remote too?"
        hide clock repaired with dissolve
        show remote with dissolve:
            subpixel True pos (0.55, 0.25) zpos 1.0 yzoom 1.0 zoom 0.32

        menu: 
            "Yeah, I just need batteries to put in it":
                call Batteries from _call_Batteries
            "I'm not sure how to...":
                call Nobatteries from _call_Nobatteries
        return
    
    label Noalarm:
        show lucrecia sad with dissolve: 
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        play sound "audio/lucrecia-mad.ogg" volume 0.2 
        l "Oh...okay, I was hoping you could fix it..."
        return
    
    label Batteries:
        show lucrecia happy with dissolve: 
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        play sound "audio/lucrecia-happy.ogg" volume 0.2 
        l "Thank you so much! My grandaughter used to do this for me everyday."

        hide remote with dissolve
        return
    
    label Nobatteries:
        show lucrecia really sad with dissolve: 
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        play sound "audio/lucrecia-mad.ogg" volume 0.2 
        l "I wish my grandaughter was here, she would have fixed it."

        hide remote with dissolve
        return

#Last Scene
    label Expected:
        hide screen results with dissolve
        play sound "audio/nora-happy.ogg" volume 0.1
        show nora happy with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        n "Good for you [player]! Now let's get you to your new home!"
        
        #This returns you to continue the dialogue
        return

    label Unsure:
        hide screen results with dissolve
        play sound "audio/nora-happy.ogg" volume 0.1
        show nora neutral with dissolve:
            subpixel True pos (0.25, 0) zpos 1.0 yzoom 1.0 zoom 0.32
        n "[player] don't worry, you'll enjoy the place."
        
        #This returns you to continue the dialogue
        return