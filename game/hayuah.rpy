define fade_black = Fade(0.5, 1, 0.5)
label chapter_one_start:
    play sound "jangkrek.mp3"
    scene va with fade_black

    play sfx "step.wav"
    show rafli_2 at Position(xalign=0.1, yalign=0.5)
    i"(Aku tidak tahu kenapa aku setuju untuk ikut malam ini. Udara di sini terasa... berat.)"

    stop sfx
    return