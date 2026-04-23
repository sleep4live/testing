define fade_black = Fade(0.5, 3, 0.5)
transform shake:
    xoffset 0
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 0
define flash = Fade(0.1, 0, 0.5, color="#ffffff")

label flicker_effect:
    show black
    with Dissolve(0.1)
    hide black
    with Dissolve(0.1)
    return

scene black_screen
label chapter_one_start:
    play music crowd loop volume 0.5
    scene kantin with fade_black
    pause 1.0
    show rafli at Position(xalign=0.0, yalign=0.6, zoom=0.1)
    show rendi at Position(xalign=0.2, yalign=0.6, zoom=0.1)
    show lulu at Position(xalign=0.8, yalign=0.6, zoom=0.1)
    show eileen at Position(xalign=1.0, yalign=0.6, zoom=0.1)
    with dissolve
    l angry "Ada apa Ren ngajakain ke kantin?"
    show lulu
    i talking "Tau nih, Tumben banget ngajakin"
    show rafli
    r talk2 "Yaaaa gpp sih, gw cuma pengen ketemu kalian"
    r talk3 "Ehh lu pada tau ga villa 44?"
    l shock "OHHHHH villa yang jadi tempat pembunuhan itu ya?"
    l rafli "Kenapa emangnya? lu mau ngajakin kita kesana?"
    show lulu
    r talk3 "Gw punya ide konten mengeksplor villa 44 ini.."
    show rendi
    e talk2 "Villa yang angker itu kann? ada penunggunya.."
    show eileen
    i talking "emang lu brani Ren?"
    show rafli
    r talk "udah ngajakin masa takut?"
    l rafli "tengil banget lo, bukan darerah kita lohh itu..."
    show lulu angry2
    r talk3 "aman... pake mobil gw aja"
    e talk2 "lu seriusan Ren? Tempat itu kan Terlarang.."
    show eileen
    l angryy "okeee, gw ikut. tapi tunggu gw balik kerja ya..."

 
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
    l angryy"Rendi, tolong hentikan intro bodohmu itu. Dingin banget di sini, dan baterai ponselku tiba-tiba drop jadi 15%%. Kalau kita cuma mau buktikan mitos konyolmu, mending kita pulang."
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

    #scene 1 end - scene 2 plays#
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
    show lulu rafli
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
    l angryy "Rendi, ini bukan waktunya bercanda!"
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

    scene lorong2 with fade_black
    pause 1
    show rafli at Position(xalign=0.0, yalign=0.6, zoom=0.1)
    show lulu at Position(xalign=0.8, yalign=0.6, zoom=0.1)
    show eileen at Position(xalign=1.0, yalign=0.6, zoom=0.1)
    "..."
    "di akhir lorong yang gelap, Rendi yang hampir tidak terlihat sedang berdiri,"
    "tetapi disebelah kanan mu terdapat sebuah anak tangga menuju lantai atas, dimana suara ledakann sebelumnya berasal, "
    "disaat yang bersamaan Eileen terlihat sangat pucat seolah ingin pingsan."
    "apa yang harus Rafli lakukan...?"

    menu:
        "Hampiri Rendi":
            jump select_rendi
        "Investigasi lantai atas":
            jump select_atas
        "Diam Disini & cari alat untuk dobrak pintu":
            jump select_diam

    label select_rendi:
        $rendilove += 1
        i talking "Kita samperin Rendi dulu. Jangan sampai dia ngelakuin hal bodoh sendirian"
        play audio jp
        scene jskidding with vpunch
        pause 0.5

        scene lorong2 with fade_black
        show eileen cry  at Position(xalign=1.0, yalign=0.6, zoom=0.1)
        e cry "apatu woi"
        show rafli scared at Position(xalign=0.0, yalign=0.6, zoom=0.1)
        i scared "uuraaa"
        show lulu shock at Position(xalign=0.8, yalign=0.6, zoom=0.1)
        l shock "AAAA"
        "Mereka berjalan melalui lorong sempit dengan wallpaper mengelupas, lukisan-lukisan tua"
        "Sesampai nya di ujung lorong, tampak Rendi yang berhadapan dengan potret keluarga bergaya kolonial"

        ### FOTO ###
        play music woodsteps fadein 2.0
        show kolonial with fade_black
        stop music
        window hide
        pause
        window show dissolve
        r "Liat deh... Ini keluarga yang dibantai itu. Tapi... yang aneh... ada satu orang di sini yang wajahnya dicoret."
        l "Mungkin itu pelakunya. Atau korban yang dihapus dari sejarah keluarga."
        window hide
        call flicker_effect
        scene expression Solid("#000000")
        pause 1.0
        "SFX: Tiba-tiba lampu senter Rendi padam"
        window show dissolve
        play music whisper fadein 3.0
        r "Eh, baterainya abis? padahal baru ganti-"
        "Suara bisikan cepat dari belakang lukisan: Kembali... kembali... 
        kembali..."
        e "Eliyn: (teriak dia wak) DIA BILANG KITA HARUS KEMBALI!"
        i "Rafli: Ada ruang rahasia..."

        "apa yang akan rendi lakukan?"

        menu: 
            "Masuk ke lorong":
                jump select_lorong
            "tetap di ruang tamu":
                jump select_ruang

        label select_lorong:
        ""
        return

        label select_ruang:
        "."
        return

    ###Tangga###
    label select_atas:
        $eileenlove -= 1
        i talking "Lulu, jaga Eliyn. Gue mau cek ke lantai atas bentar"
        scene expression Solid("#000000")
        pause 0.5
        "Rafli naik sendiri, meninggalkan Lulu dan Eliyn di bawah."
        play music woodsteps
        pause 0.5
        i "Setiap anak tangga berbunyi seperti mau patah. Kenapa 
        aku merasa... ada yang ikut naik di belakangku?"
        "Mendekati pintu, mendorong pelan"
        stop music 
        play audio pintu
        scene kamar anak with fade_black
        window hide
        pause
        window show dissolve
        i scared "Suasana disini begitu mencekam..." 
        play music music
        ""
        return#

    label select_diam:
        i talking "Kita diam di sini. Cari alat untuk dobrak pintu ini sekarang juga"
        return#

    return


