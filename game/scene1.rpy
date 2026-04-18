define fade_black = Fade(0.5, 3, 0.5)
transform shake:
    xoffset 0
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 0
define flash = Fade(0.1, 0, 0.5, color="#ffffff")

scene black_screen
label chapter_one_start:
 
    play music jangkrek loop
    play sound step
    scene villa2 with fade_black
    pause 1

    show rafli at Position(xalign=0.0, yalign=0.6, zoom=0.1)
    show rendi at Position(xalign=0.2, yalign=0.6, zoom=0.1)
    show lulu at Position(xalign=0.8, yalign=0.6, zoom=0.1)
    show eileen at Position(xalign=1.0, yalign=0.6, zoom=0.1)
    with dissolve

    i renungkan"(Aku tidak tahu kenapa aku setuju untuk ikut malam ini. Udara di sini terasa... berat.)"
    show rafli

    r talk"Kalian lihat bangunan di belakangku ini? Ini dia, guys. Vila 44. Tempat yang katanya jadi lokasi pembantaian satu keluarga di tahun 90-an!"
    l angry"Rendi, tolong hentikan intro bodohmu itu. Dingin banget di sini, dan baterai ponselku tiba-tiba drop jadi 15%%. Kalau kita cuma mau buktikan mitos konyolmu, mending kita pulang."
    r angry"Ah elah, Lu. Lu kan anak sains, masa takut sama mitos? Kita cuma masuk, rekam 30 menit, terus balik. Deal?"
    e talking"Rafli... aku rasa kita nggak seharusnya di sini. Ada yang... ngeliatin kita dari jendela atas."
    play sound patah
    "*KREK*"
    show lulu shock
    show rendi scaret
    show eileen shock
    i scared"Jendela atas? (Melihat ke atas, tapi tidak ada apa-apa) Nggak ada siapa-siapa, El. Mungkin cuma pantulan cahaya bulan."
    l scared"Tuh kan. Mata kamu aja yang capek, El. Lagian, mana ada hantu? Paling gelandangan atau hewan liar."
    r angry"Udahlah, ayo masuk! Pintunya nggak dikunci kok, gue udah cek tadi sore."

    #scene 1 end - scene 2 plays
    play sound pintu fadein 2.0
    scene expression Solid("#000000")
    stop music fadeout 2.0
    "Secara Perlahan, mereka mendorong pintu villa yang rapuh dan sudah diselimuti oleh debu"
    scene villainterior with fade_black
    play music amba loop
    pause 1
    "Di dalam, mereka disambut dengan Ruang tamu yang berdebu dam perabotan yang di tutupi dengan kain putih"
    show rafli at Position(xalign=0.0, yalign=0.6, zoom=0.1)
    show rendi at Position(xalign=0.2, yalign=0.6, zoom=0.1)
    show lulu at Position(xalign=0.8, yalign=0.6, zoom=0.1)
    show eileen at Position(xalign=1.0, yalign=0.6, zoom=0.1)
    with dissolve
    "..."
    play sound slam
    with flash
    show rafli scared at shake
    show rendi scaret at shake
    show lulu shock at shake
    show eileen shock at shake
    "*DOR*"
    play audio kia
    e shock "KYAAA!"
    l shock "Apa-apaan itu?!"
    play sound handle
    pause 3
    i scared "Sial... terkunci! Rendi, bantuin gue dorong!"
    play sound handle
    pause 3
    r talk "Nggak bisa, Raf! Macet total! Padahal tadi gagangnya lancar-lancar aja!"
    play audio breathe2
    l scared "Oke, tenang. Jangan panik. Anginnya kencang, mungkin pintunya nyangkut karena kerangkanya sudah lapuk. Kita cari jalan keluar lain. Pasti ada pintu belakang"
    play audio cry
    e cry "Bukan angin... Ada yang ketawa. Kalian nggak denger? Ada yang ketawa di telingaku..."
    i happy "El, tenang. Kita bertiga ada di sini."
    r talk "Eh, guys... Kalian lihat lukisan di ujung lorong itu nggak sih? Dari tadi gue perhatiin, kayaknya matanya... gerak."
    show rafli scared
    l angry "Rendi, ini bukan waktunya bercanda!"
    r angry "Gue serius, Lu! Sini deh lihat!"
    play audio runaway
    hide rendi with dissolve
    i mad1 "Ren, jangan misah!"
    stop music fadeout 5.0
    "..."
    "..."
    play audio drop
    show rafli scared at shake
    show lulu shock at shake
    show eileen shock at shake
    "!!!"
    "..."
    r "Raf... Lu... El... Sini cepetan. Gue nemu sesuatu."
    return