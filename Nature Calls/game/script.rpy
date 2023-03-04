# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Sitting and scrolling again. You read of people going on walks through the fresh air - a luxury this generation only heard stories of."
    "The city is one of a few left in this barren wasteland, sealed off from the outside world by a dome that looms in the distance. The only thing seperating the breathable air from the polluted.
    You gaze passed the dome into the never-ending expanse of smoke and haze, the product of a past civilisation's rampant pollution."
    "As you sit at your computer, the dim glow of the screen casting a soft light across your face, you can't help but feel a sense of isolation and confinement."
    "The constant hum of machinery and the occasional blaring of sirens are the only sounds that fill the air. It is a bleak existence, but one that you had grown accustomed to."
    # "Little did you know, your world was about to change in ways they could never have imagined."

    # "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
