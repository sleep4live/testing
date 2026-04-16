init python:
    def typing_callback(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/typing2.mp3", channel="sound", loop=True)

        elif event in ("slow_done", "end"):
            renpy.sound.stop(channel="sound")

define fade_black = Fade(0.5, 1, 0.5)
define e = Character("Eileen", who_color="#252274", callback=typing_callback)
define i = Character("Rafli", who_color="#fba92b", callback=typing_callback)
define l = Character("Lulu", who_color="#2aa7b6",  callback=typing_callback)
define r = Character("Rendi", who_color="#73110c",  callback=typing_callback)

label chapter_one_start:
    play sound "jangkrek.mp3"
    scene va with fade_black

    "Plss 😭🙏"
    play sfx "step.wav"
    show rafli
    stop sfx

    stop sound
    return