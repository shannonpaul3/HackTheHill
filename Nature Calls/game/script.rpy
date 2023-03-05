# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Flags

# Chapter 1
default research_flag = False
default kicked_out_flag = False
default menu_reponse_flag = 0
# Chapter 2
default guard1_answered = False
default guard2_answered = False
default guard3_answered = False 
default password_attempt = 0
default code_input = ""


# Characters

# Chapter 1
define y = Character("You")
define u = Character("@tr33sWillSaveU5")

# Chapter 2
define npc1 = Character("Rabbit 1")
define npc2 = Character("Rabbit 2")
define npc3 = Character("Rabbit 3")
define npc_all = Character("Rabbit 1, 2, 3")

# Chapter 3
define sci = Character("Scientist")

# The game starts here.

label start:

############################################################################################################################################################
    # Chapter 1
    scene bg-studyroom
    with fade

    # Start the background music playing.
    play music "background music.ogg" loop

    "As I scrolled through my social media feed for what felt like the hundredth time, I couldn't help but feel a sense of disappointment. "
    "There was nothing to do outside in our enclosed city, the once-spacious parks and basketball courts now covered with towering housing developments as the population continued to grow."
    "We are trapped inside a sealed city, with no escape from the monotony of everyday life. Even if you suit up and walk outside the city there is nothing but barren lands."
    "But little did I know, my endless scrolling was about to lead me down a path I never could have imagined."

    scene bg-laptop
    with fade

    menu post:
        "You decide to make a post on an online forum to see if anybody else can relate."
        
        "How do you cope with the fact that there's no natural greenery or fresh air left?":
            jump choice_post1
        
        "Do you think there's any hope left for the outside world to be restored to its former beauty?":
            jump choice_post2
    
    label choice_post1:
        "..."
        "*Ding*"
        

        u "no natural greenery? no fresh air? ... are you sure about that?"
        jump response

    label choice_post2:
        "..."
        "*Ding*"

        u "i know something you don't..."
        jump response

    menu response:

        "What would you like to reply?"

        "If there is greenery somewhere - why would we be living in these sealed cities?":
            jump answer1
        
        "Do you know where I can find green space??":
            jump answer2

        "What are you not saying?":
            jump answer3
    
    label answer1:
        $ menu_reponse_flag = 1
        jump choice_reponse
    
    label answer2:
        $ menu_reponse_flag = 2
        jump choice_reponse
    
    label answer3:
        $ menu_reponse_flag = 3
        jump choice_reponse

    label choice_reponse: 
        "*Ding*"
        "The notification reads \"Message request from  @tr33sWillSaveU5\""
    
    menu respond:

        "Accept Message Request?"

        "Nah - this user is creeping me out.":
            jump end1
        
        "Yes - I'm curious what they have to say.":
            jump pm

    label pm:
        
        scene bg-forum
        with dissolve

        if menu_reponse_flag == 1 or menu_reponse_flag == 3:
            u "These sealed cities are sealing off more than just polluted air. They are sealing off information as well."

        elif menu_reponse_flag == 2:
            u "Where to find it? I've seen it with my own eyes! There is lots of information being kept secret."
        
        jump pm_response
    
    menu pm_response:
        "What kind of information?":
            jump pm_reponse2
    
    label pm_reponse2:
        u "Information about scientific research and experiments. There is a group of us - scientist - working on a magical seed. I used to be part of the team but was kicked out."
        "You write back anxiously."
        jump pm_response3

    menu pm_response3:

        "Magical Seed?":
            jump research_response

        "Why were you kicked out?":
            jump kicked_out_response
        
    label kicked_out_response:
        u "You see us scientist feel very strongly about interfering with nature... "
        u "I however believe that since we caused this damage we must step in and reverse it if we can. I mean - look at what's left! "
        u "My colleagues did not feel the same way and as I result I lost their trust. They will not allow me to return."
        $ kicked_out_flag = True
        jump check_flag
    
    label research_response:
        u "Yes magical! It's purely based on science of course but it really does feel like a magical discovery."
        u "These seeds will be able to survive any climate and grow back our lush forests and plants. "
        $ research_flag = True
        jump check_flag
    
    label check_flag:
        if research_flag and kicked_out_flag:
            jump pm_response4
        else:
            jump pm_response3

    menu pm_response4:
        "Where can I find these scientists?":
            jump pm_sign_off
        "Why should I believe you?":
            jump pm_sign_off

    label pm_sign_off:
        u "Go and see for yourself. You can find these scientists outside the sealed city beyond the abandoned steam stacks."
        u "There aren't many people who appreciate what we've really lost anymore. It's too distant of a memory. I hope there are more of you out there. Good luck to you."

        "\"@tr33sWillSaveU5\" status switched to unavailable."

    scene bg-studyroom
    with fade

    "You look out your window at the metal city, smoggy air, and barren lands in the distance."

    "Is this information really true? Is it worth risk?"

    menu chapter1:
        "Yes.":
            jump chapter1_end
        "No.":
            jump end1

    label chapter1_end:
        "You grab your oxygen mask and suit up. You head to the edge of the seal."
        jump chapter2_start
    
    label end1:
        "You continue on with your day daydreaming of a greener time."
        return
############################################################################################################################################################
    # Chapter 2

    label chapter2_start:

        scene bg-outside
        with fade

        "You step outside the seal and begin your long walk towards the abandoned steam pipes. You walk for hours and there's nothing but dirt roads."
        "You come to a fork in the road with 3 different paths. Somebody is standing in front of each one. Maybe they can help you with directions."
        jump npc
    #Ask player to choose among the guards.

    label npc:

        show char-npc123
        with dissolve

        npc_all "You've wondered this far out, you must be looking for the lab!"
        npc_all "As a warning only one of us will tell you the truth... You have no way of knowing who lies or who tells the truh - however we will know."
        npc_all "You can only ask us one question to help you find your way."

    menu ask:

        "Which guard do you want to ask?"

        "Guard 1":
            hide char-npc123
            jump ask_guard1
                        
        "Guard 2":
            hide char-npc123
            jump ask_guard2

        "Guard 3":
            hide char-npc123
            jump ask_guard3

    label ask_guard1:
        
        show char-npc1
        with dissolve

        if guard1_answered:
            npc1 "You already asked me"
            jump ask
        else:
            menu question1: 
                npc1 "What question do you want to ask"

                "Which path should I go?":

                    npc1 "My path 1 would lead you to freedom"


                "Are you the liar or the truth-teller?":

                    npc1 "I'm the truth teller"

                "What would the other guards say if I asked them which door leads to freedom?":

                    npc1 "Path 1 or 2"

        $ guard1_answered = True

        hide char-npc1

        if guard1_answered and guard2_answered and guard3_answered:
            jump decide_menu
        
        jump ask


    label ask_guard2:

        show char-npc2
        with dissolve

        if guard2_answered:
            npc2 "You already asked me"
            jump ask
        else:
            menu question2: 
                npc2 "What question do you want to ask"
                
                "Which path should I go?":
                    
                    npc2 "My path 2 would lead you to freedom"

                "Are you the liar or the truth-teller?":

                    npc2 "I'm the truth teller"

                "What would the other guards say if I asked them which door leads to freedom?":

                    npc2 "Path 1 or 2"

        $ guard2_answered = True

        hide char-npc2

        if guard1_answered and guard2_answered and guard3_answered:
            jump decide_menu
        
        jump ask


    label ask_guard3:

        show char-npc3
        with dissolve

        if guard3_answered:
            npc3 "You already asked me"
            jump ask
        else:
            menu question3: 
                npc3 "What question do you want to ask"

                "Which path should I go?":
                
                    npc3 "My path 2 would lead you to freedom"

                "Are you the liar or the truth-teller?":

                    npc3 "I'm the truth teller"

                "What would the other guards say if I asked them which door leads to freedom?":

                    npc3 "Path 1 or 2"

        $ guard3_answered = True
        
        hide char-npc3

        if guard1_answered and guard2_answered and guard3_answered:
            jump decide_menu
        
        jump ask

    label decide_menu:

        show char-npc123
        with dissolve

        menu decide:

            npc_all "Which path will you chose?"

            "Path 1":
                hide char-npc123
                jump end2
            "Path 2":
                hide char-npc123
                jump end2
            "Path 3":
                hide char-npc123
                jump fence
    
    label fence:
        scene bg-gate
        with fade

        "You follow the path until you reach a fence with locked gate."
        "Upon closer inspection, you notice a key pad. This seems to be the only way through."
    
    label key_pad:
        scene bg-hint
        python:
            code_input = renpy.input("Enter the 3 digit code:", length=3)
            code_input = code_input.strip()
        jump check_password

    label check_password:
        
        if code_input == "846":
            
            "*Buzz*"
            "A light turns green and the gate unlocks."
            
            jump chapter3_start

        else:
            if password_attempt == 2:
                jump end3
            
            "*Buzz*"
            "A light turns red. [code_input] is the wrong code."
            "One chance remaining."

            $ password_attempt = password_attempt + 1
            $ code_input = ""
            jump key_pad
        jump key_pad

    label end2:
        "You wonder the path."
        "Hours go by... No lab in sight... Did you go the wrong way?"
        "You look at your oxygen tank metre and it's just above empty. Not enough to get back."
        "Gazing out on the barren lands, you fade away, dreaming of the trees that used to be standing around you."
        return
    
    label end3:
        "*Buzz* You enter the wrong code and the system locks up."
        "You have come too far to return and this gate is the only way through..."
        "You look at your oxygen tank metre and it's just above empty. Not enough to get back."
        "You sit down and gaze out on the barren lands, as you fade away, dreaming of the trees that used to be standing around you."
        return
        
    ################################################################################################################
    #Chapter 3
    label chapter3_start:
        "Chapter 3"

        scene bg-lab
        with fade

        y "Hello?"

        show char-scientist
        with dissolve

        sci "Who are you?"

        y "Those plants are incredible! I never thought I'd see so much greenery in this world!"

        sci "It's beautiful isn't it? These are the only natural plants remaining. No magic behind these, they would not survive in any other climate."

        y "Yes! Why will you not share these \"magical\" plant seeds with the world?"

        sci "We believe that nature should take its course without human intervention."
        sci "We cannot play god. We should not meddle with the natural order of things."
        
    menu convince:
        
        "I appreciate your position, but we have already meddled with nature in so many ways, and the consequences are clear.":
            jump continue_convo
        "Using the magical seed is not about playing god, but about restoring the balance of nature.":
            jump continue_convo
    
    label continue_convo:

        y "We need to take responsibility for our actions and do what we can to fix the problems we have created. "

        sci "You are right about taking responsibility. The truth is we are not ready."
        sci "What you haven't been told is that this magic seed grows plants that release gases poisonous to humans."
        sci "So posoinous we have no material capable of keeping it out."
        sci "The planet would survive but we would not. Are you sure you are ready to take responsibility?" 
        jump make_choice

    menu make_choice:

        "I did not realize that was the case. I do not think I am ready for this.":
            jump end4
        "The fate of the planet is in our hands, and we have a responsibility to act.":
            jump end5

    label end4:
        hide char-scientist
        "The scientists welcome you to stay with them at the lab. To live out your days appreciating the last natural plants on the planet."
        "Nature must run its course."
    label end5:
        hide char-scientist
        "End"

    return
