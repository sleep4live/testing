init python:
    def typing_callback(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/typing2.mp3", channel="sound", loop=True)

        elif event in ("slow_done", "end"):
            renpy.sound.stop(channel="sound")

define e = Character("Eileen", who_color="#252274")
define i = Character("Rafli", who_color="#fba92b")
define l = Character("Lulu", who_color="#2aa7b6")
define r = Character("Rendi", who_color="#73110c")
define e = Character("Eileen", callback=typing_callback)
define m = Character("Rafli", callback=typing_callback)
define l = Character("Lulu", callback=typing_callback)
define r = Character("Rendi", callback=typing_callback)

# The game starts here.
scene bg room

label start:
    show rendi talk at Position(xalign=0.4, yalign=0.5)
    show lulu scared at Position(xalign=0.7, yalign=0.5)
    show rafli talking at Position(xalign=0.1, yalign=0.5)
    show eileen happy at Position(xalign=0.9, yalign=0.5)    
    i "Kamu mau makan apa?"

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
    i "my name is Rafli"
    r "my name is Rendi"
    l "my name is lulu"
    e "my name is eileen"
    return


label select_pizza:
    show eileen talking at Position(xalign=0.9, yalign=0.5)
    e "Kita makan pizza ya!"
    return


label select_sushi:
    show eileen talking at Position(xalign=0.9, yalign=0.5) 
    e "Sushi enak tuh!!"
    return

