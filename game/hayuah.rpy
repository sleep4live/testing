define fade_black = Fade(0.5, 5, 0.5)
label chapter_one_start:
 
    play music jangkrek loop
    play sound step
    scene va with fade_black

    show rafli at Position(xalign=0.1, yalign=0.5)
    show rendi talk at Position(xalign=0.4, yalign=0.5)
    show lulu scared at Position(xalign=0.7, yalign=0.5)
    show eileen happy at Position(xalign=0.9, yalign=0.5)

    with dissolve
    i renungkan"(Aku tidak tahu kenapa aku setuju untuk ikut malam ini. Udara di sini terasa... berat.)"
    show rafli

    r talk"Kalian lihat bangunan di belakangku ini? Ini dia, guys. Vila 44. Tempat yang katanya jadi lokasi pembantaian satu keluarga di tahun 90-an!"
    l angry"Rendi, tolong hentikan intro bodohmu itu. Dingin banget di sini, dan baterai ponselku tiba-tiba drop jadi 15%%. Kalau kita cuma mau buktikan mitos konyolmu, mending kita pulang."
    r angry"Ah elah, Lu. Lu kan anak sains, masa takut sama mitos? Kita cuma masuk, rekam 30 menit, terus balik. Deal?"
    e talking"Rafli... aku rasa kita nggak seharusnya di sini. Ada yang... ngeliatin kita dari jendela atas."
    play sound patah
    "*KREK*"
    i scared"Jendela atas? (Melihat ke atas, tapi tidak ada apa-apa) Nggak ada siapa-siapa, El. Mungkin cuma pantulan cahaya bulan."
    l scared"Tuh kan. Mata kamu aja yang capek, El. Lagian, mana ada hantu? Paling gelandangan atau hewan liar."
    r angry"Udahlah, ayo masuk! Pintunya nggak dikunci kok, gue udah cek tadi sore."

    play sound pintu
    scene villa with fade_black
    return