init python:
    def typing_callback(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/typing2.mp3", channel="sound", loop=True)

        elif event in ("slow_done", "end"):
            renpy.sound.stop(channel="sound")

define e = Character("Eileen", callback=typing_callback)
define m = Character("Rafli", callback=typing_callback)
define l = Character("Lulu", callback=typing_callback)
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
    e "Sushi enak tuh!!"
    return

