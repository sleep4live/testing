# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define m = Character("Rafli")
define l = Character("Lulu")
define r = Character("Rendi")

# The game starts here.
scene bg room

label start:

    show rafli talking at Position(xalign=0.1, yalign=0.5)
    show eileen happy at Position(xalign=0.9, yalign=0.5)    
    m "Kamu mau makan apa?"

    menu:
        "Pizza":
            jump select_pizza
        "Sushi":
            jump select_sushi
        "Nggak usah, makasih":
            show eileen talking at Position(xalign=0.9, yalign=0.5)
            e "Oke deh..."

    play sound "audio/laugh.mp3" volume 0.2
    show eileen talking at Position(xalign=0.9, yalign=0.5) 
    e "Aku capek, mungkin lain kali ya."
    return


label select_pizza:
    show eileen talking at Position(xalign=0.9, yalign=0.5)
    e "Kita makan pizza ya!"
    return


label select_sushi:
    show eileen talking at Position(xalign=0.9, yalign=0.5) 
    e "Sushi enak tuh!"
    return
