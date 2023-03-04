# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Flags
default research_flag = False
default kicked_out_flag = False
default menu_reponse_flag = 0

# Characters
define y = Character("You")
define u = Character("@tr33sWillSaveU5")

# The game starts here.

label start:

    scene bg-studyroom
    with fade

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
        u "Unfortunately I never got to see the research complete... but I just have a feeling they figured it out."
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
    
    "Is this information really true? Even if it was, is it worth the risk heading out beyond the city? The steam stacks are too far for any mobile service and oxygen is limited."
    
    scene bg-studyroom
    with fade

    "You look out your window at the metal city, smoggy air, and barren lands in the distance."

    "Is it worth risk?"

    menu chapter1:
        "Yes.":
            jump chapter1_end
        "No.":
            jump end1

    label chapter1_end:
        "End of chapter 1"
    
    label end1:
        "You continue on with your day daydreaming of a greener time."

    return
