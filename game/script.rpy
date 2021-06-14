# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Hemato")

define gui.text_size = 28

define h = Character("EHEMATO", kind=nvl, what_color="#C10415", what_font="font/HafestranFont-Regular.otf")
define m = Character("MAERIJE", kind=nvl, what_color="#269A03", what_font="font/HafestranFont-Regular.otf")
define f = Character("ASTRONAUT", kind=nvl, what_color="#0A306E", what_font="font/HafestranFont-Regular.otf")
define e = Character("EHENA-MAERIE", kind=nvl, what_color="#269A03", what_font="font/HafestranFont-Regular.otf")
define d = Character("PERE DII EHEMATO", kind=nvl, what_color="#C10415", what_font="font/HafestranFont-Regular.otf")

# Side Characters
define ingle = Character("TOMO ANIJEHOS", kind=nvl, what_color="#C10415", what_font="font/HafestranFont-Regular.otf")

# With T being chapter title
define t = Character(None, kind=nvl, what_color="#269A03", what_font="font/HafestranFont-Regular.otf")

define menu = nvl_menu

default book = True

# Part One
image bg guillotine = Tile("images/guillotine.png")
image bg hemato_hand_one = Tile("images/hemato_hand_one.png")
image bg guillotine_wash = Tile("images/guillotine_wash.png")
image bg morning_razor_cut = Tile("images/morning_razor_cut.png")
image bg shaking_hands = Tile("images/shaking_hands.png")
image bg girl_of_alsace = Tile("images/girlofalsace.png")
image bg guillotine_gun = Tile("images/guillotinegun.png")
image bg new_france = Tile("images/newfrance.png")
image bg chattanoogazoo = Tile("images/chattanoogazoo.png")
image bg growninavat = Tile("images/growninavat.png")
image bg guillotined = Tile("images/guillotined.png")
image bg headsewnbackon = Tile("images/headsewnbackon.png")
image bg dreamscannersone = Tile("images/dreamscannersone.png")
image bg wiredinavat = Tile("images/wiredinavat.png")
image bg guillotinedcharlotteone = Tile("images/guillotinedcharlotteone.png")
image bg marinelepen = Tile("images/marinelepen.png")
image bg frenchspaceforces = Tile("images/frenchspaceforces.png")
image bg frenchastronaut = Tile("images/frenchastronaut.png")
image bg kissinglovers = Tile("images/kissinglovers.png")
image bg woodenclogs = Tile("images/woodenclogs.png")
image bg tanksinchattanooga = Tile("images/tanksinchattanooga.png")
image bg frenchflaginus = Tile("images/frenchflaginus.png")
image bg soldiershootmother = Tile("images/soldiershootmother.png")

## Graphic Novel Sequence 1
image bg shotofalampinthedawn_f1 = Tile("images/shotofalampinthedawn/frame1.png")
image bg shotofalampinthedawn_f2 = Tile("images/shotofalampinthedawn/frame2.png")
image bg shotofalampinthedawn_f3 = Tile("images/shotofalampinthedawn/frame3.png")

## Graphic Novel Sequence 2
image bg colonieslikethis_f1 = Tile("images/colonieslikethis/frame1.png")
image bg colonieslikethis_f2 = Tile("images/colonieslikethis/frame2.png")
image bg colonieslikethis_f3 = Tile("images/colonieslikethis/frame3.png")
image bg colonieslikethis_f4 = Tile("images/colonieslikethis/frame4.png")

## Graphic Novel Sequence 3
image bg hellbroughtintolife_f1 = Tile("images/hellbroughtintolife/frame1.png")
image bg hellbroughtintolife_f2 = Tile("images/hellbroughtintolife/frame2.png")
image bg hellbroughtintolife_f3 = Tile("images/hellbroughtintolife/frame3.png")
image bg hellbroughtintolife_f4 = Tile("images/hellbroughtintolife/frame4.png")
image bg hellbroughtintolife_f5 = Tile("images/hellbroughtintolife/frame5.png")
image bg hellbroughtintolife_f6 = Tile("images/hellbroughtintolife/frame6.png")

## Part Two
image bg mynameishemato1 = Tile("images/mynameishemato.png")
image bg mespereetfrancais = Tile("images/mespereetfrancaise.png")
image bg blackmanhighparkinglot = Tile("images/blackmanhighparkinglot.png")
image bg mynameishemato2 = Tile("images/mynameishemato2.png")
image bg ridinghomefromschool = Tile("images/ridinghomefromschool.png")
image bg usedtobedecapitation = Tile("images/usedtobedecapitation.png")
image bg bloodonhands = Tile("images/bloodonhands.png")
image bg bloodybowlingpin = Tile("images/bloodybowlingpin.png")
image bg letmetellyouastory = Tile("images/letmetellyouastory.png")

## Graphic Novel Sequence 4
image bg strasbourgalsace_frame1 = Tile("images/strasbourgalsace/frame1.png")
image bg strasbourgalsace_frame2 = Tile("images/strasbourgalsace/frame2.png")
image bg strasbourgalsace_frame3 = Tile("images/strasbourgalsace/frame3.png")

image bg brokenwinebottle   = Tile("images/brokenbottleofwine.png")
image bg frenchcourtroom    = Tile("images/frenchcourtroom.png")
image bg mistrialguillotine = Tile("images/mistrialguillotine.png")
image bg sailtothenewworld  = Tile("images/sailtothenewworld.png")
image bg asylum             = Tile("images/asylum.png")
image bg familyghosts       = Tile("images/familyghosts.png")
image bg hangingbyathread   = Tile("images/hangingbyathread.png")
image bg headinatank        = Tile("images/headinatank.png")

## Part Three

### Graphic Novel Sequence 5
image bg deathinatimeofrevolution_frame1 = Tile("images/deathinatimeofrevolution/frame1.png")
image bg deathinatimeofrevolution_frame2 = Tile("images/deathinatimeofrevolution/frame2.png")
image bg deathinatimeofrevolution_frame3 = Tile("images/deathinatimeofrevolution/frame3.png")
image bg deathinatimeofrevolution_frame4 = Tile("images/deathinatimeofrevolution/frame4.png")
image bg deathinatimeofrevolution_frame5 = Tile("images/deathinatimeofrevolution/frame5.png")
image bg deathinatimeofrevolution_frame6 = Tile("images/deathinatimeofrevolution/frame6.png")

### Graphic Novel Sequence 6
image bg intothegroundshelay_frame1 = Tile("images/intothegroundshelay/frame1.png")
image bg intothegroundshelay_frame2 = Tile("images/intothegroundshelay/frame2.png")
image bg intothegroundshelay_frame3 = Tile("images/intothegroundshelay/frame3.png")
image bg intothegroundshelay_frame4 = Tile("images/intothegroundshelay/frame4.png")
image bg intothegroundshelay_frame5 = Tile("images/intothegroundshelay/frame5.png")
image bg intothegroundshelay_frame6 = Tile("images/intothegroundshelay/frame6.png")
image bg intothegroundshelay_frame7 = Tile("images/intothegroundshelay/frame7.png")
image bg intothegroundshelay_frame8 = Tile("images/intothegroundshelay/frame8.png")
image bg intothegroundshelay_frame9 = Tile("images/intothegroundshelay/frame9.png")

image bg idontwantthisjob = Tile("images/hematowantsnotthejob.png")

### Part Four
image bg severedheadofehenamaerie_frame1 = Tile("images/severedheadofehenamaerie/frame1.png")
image bg severedheadofehenamaerie_frame2 = Tile("images/severedheadofehenamaerie/frame2.png")
image bg severedheadofehenamaerie_frame3 = Tile("images/severedheadofehenamaerie/frame3.png")

# Graphic Novel Sequence 7
image bg crossbowassemblyline_frame1 = Tile("images/crossbowassemblyline/crossbowassemblyline_frame1.png")
image bg crossbowassemblyline_frame2 = Tile("images/crossbowassemblyline/crossbowassemblyline_frame2.png")
image bg crossbowassemblyline_frame3 = Tile("images/crossbowassemblyline/crossbowassemblyline_frame3.png")
image bg crossbowassemblyline_frame4 = Tile("images/crossbowassemblyline/crossbowassemblyline_frame4.png")
image bg crossbowassemblyline_frame5 = Tile("images/crossbowassemblyline/crossbowassemblyline_frame5.png")
image bg crossbowassemblyline_frame6 = Tile("images/crossbowassemblyline/crossbowassemblyline_frame6.png")

# Graphic Novel Sequence 8
image bg atthegraveyard_frame1 = Tile("images/atthegraveyard/atthegraveyard_frame1.png")
image bg atthegraveyard_frame2 = Tile("images/atthegraveyard/atthegraveyard_frame2.png")
image bg atthegraveyard_frame3 = Tile("images/atthegraveyard/atthegraveyard_frame3.png")
image bg atthegraveyard_frame4 = Tile("images/atthegraveyard/atthegraveyard_frame4.png")
image bg atthegraveyard_frame5 = Tile("images/atthegraveyard/atthegraveyard_frame5.png")
image bg atthegraveyard_frame6 = Tile("images/atthegraveyard/atthegraveyard_frame6.png")
image bg atthegraveyard_frame7 = Tile("images/atthegraveyard/atthegraveyard_frame7.png")
image bg atthegraveyard_frame8 = Time("images/atthegraveyard/atthegraveyard_frame8.png")
image bg atthegraveyard_frame9 = time("images/atthegraveyard/atthegraveyard_frame9.png")

# Graphic Novel Sequence 9
image bg irideabullettrain_frame1 = Tile("images/irideabullettrain/irideabullettrain_frame1.png")
image bg irideabullettrain_frame2 = Tile("images/irideabullettrain/irideabullettrain_frame2.png")
image bg irideabullettrain_frame3 = Tile("images/irideabullettrain/irideabullettrain_frame3.png")
image bg irideabullettrain_frame4 = Tile("images/irideabullettrain/irideabullettrain_frame4.png")
image bg irideabullettrain_frame5 = Tile("images/irideabullettrain/irideabullettrain_frame5.png")
image bg irideabullettrain_frame6 = Tile("images/irideabullettrain/irideabullettrain_frame6.png")

# Graphic Novel Sequence 10
image bg returntohometown_frame1 = Tile("images/returntohometown/returntohometown_frame1.png")
image bg returntohometown_frame2 = Tile("images/returntohometown/returntohometown_frame2.png")
image bg returntohometown_frame3 = Tile("images/returntohometown/returntohometown_frame3.png")

# Normal Sequence
image bg givingallicould = tile("images/givingallIcould.png")

# Graphic Novel Sequence 11
image bg mispentresourcesonAI_frame1 = Tile("images/mispentresourcesonai/mispentresourcesonai_frame1.png")
image bg mispentresourcesonAI_frame2 = Tile("images/mispentresourcesonai/mispentresourcesonai_frame2.png")
image bg mispentresourcesonAI_frame3 = Tile("images/mispentresourcesonai/mispentresourcesonai_frame3.png")
image bg mispentresourcesonAi_frame4 = Tile("images/mispentresourcesonai/mispentresourcesonai_frame4.png")

## Graphic Novel Sequence 12
image bg cloggingtothepast_frame1 = Tile("images/cloggingtothepast/cloggingtothepast_frame1.png")
image bg cloggingtothepast_frame2 = Tile("images/cloggingtothepast/cloggingtothepast_frame2.png")
image bg cloggingtothepast_frame3 = Tile("images/cloggingtothepast/cloggingtothepast_frame3.png")

## Tommy Sequence
image bg tommysroom = Tile("images/tommysroom.png")

image bg poisonatthedinnertable_frame1 = Tile("images/poisonatthedinnertable/poisonatthedinnertable_frame1.png")
image bg poisonatthedinnertable_frame2 = Tile("images/poisonatthedinnertable/poisonatthedinnertable_frame2.png")
image bg poisonatthedinnertable_frame3 = Tile("images/poisonatthedinnertable/poisonatthedinnertable_frame3.png")
image bg poisonatthedinnertable_frame4 = Tile("images/poisonatthedinnertable/poisonatthedinnertable_frame4.png")

# The game starts here.

label start:
    stop music

    # These display lines of dialogue.

    t "{b}RAH BERUDAS DII EHENAS{/b}"

    nvl clear

    scene bg guillotine

    h "{b}blade hung from wall waiting for the washing...{\b}"

    nvl clear

    scene bg hemato_hand_one

    h "{b}hands wash the blade...{/b}"

    nvl clear

    scene bg guillotine_wash

    h "{b}these unclean hands that do dirty errands lopping off heads.{/b}"

    nvl clear

    h "{b}blood never washes off of those now gone.{/b}"

    nvl clear

    scene bg morning_razor_cut

    h "{b}morning razor cut smoothly. morning razor cut smoothly...{/b}"

    nvl clear

    scene bg shaking_hands

    h "{b}my hands are shaking. my hands are shaking.{/b}"

    nvl clear

    scene bg girl_of_alsace

    h "{b}the girl of alsace dead with smile. blood on face. her eyes now faded. life turned to dust.{/b}"

    nvl clear

    scene bg guillotine_gun

    h "{b}the national razor crossbow evolved out of the berger guillotine during the franco japanese wars."

    h "{b}initially a rolling crossbow similarly to the gatling gun.{/b}"

    h "{b}it eventually scaled down in size to that of a slightly heavy two handed weapon during the conflict.{/b}"

    nvl clear

    scene bg new_france

    h "{b}it was deployed rapidly during the invasion by the french.{/b}"

    h "{b}regions from new foundland to main took the most casualties from the device.{/b}"

    nvl clear

    scene bg chattanoogazoo

    h "{b}the bible belt was the last stronghold of american traditions. my state resisted most french influences."

    h "{b}but had a tougher time when the japanese arrived to take our rice.{/b}"

    nvl clear

    scene bg growninavat

    h "{b}post decapitation stress disorder{/b}"

    h "{b}the memories of being decapitated by ROS WIERUDOS EGUNOS...{/b}"

    nvl clear

    scene bg guillotined

    h "{b}the anxiety of living with the memories of being cut through by an angular blade...{/b}"

    nvl clear

    scene bg headsewnbackon

    h "{b}your head only sewn back on upon acquittal...{/b}"

    nvl clear

    scene bg dreamscannersone

    h "{b}the dream scanners get you in your dreams...and behind the curtain...{/b}"

    nvl clear

    scene bg wiredinavat

    h "{b}...an elite paranormal espionage unit designed to track dissidents.{/b}"

    h "{b}a long line of an increasing amount of fascist precedents before the invasion...{/b}"

    nvl clear

    scene bg guillotinedcharlotteone

    h "{b}marine le pen wanted to bring back the guillotine in her bid for the french presidency.{/b}"

    nvl clear

    scene bg marinelepen

    h "{b}when trump rejected her offer of an alliance...she waited for when the states to irrevocably split...{/b}"

    nvl clear

    m "{b}trump insulted our troops and france.{/b}"

    nvl clear

    scene bg frenchspaceforces

    h "{b}she sent an elite force of space reconnaissance to surveil the situation above the american contenent."

    h "{b}in space the different parts of the us had broke off from each other...{/b}"

    h "{b}locked in a perpetual war in nation against nation over once a proud union...{/b}"

    nvl clear

    scene bg frenchastronaut

    h "{b}the era of the us empire drew to a close in a blink of an eye.{/b}"

    h "{b}the rest was history when france took advantage of the power void in the wake of etats unis.{/b}"

    nvl clear

    scene bg kissinglovers

    h "{b}the activist sent to her death met with her brother one last time before she went off to protest the french occupation."

    nvl clear

    scene bg woodenclogs

    h "{b}the girl to poor to afford more than wooden shoes.{/b}"

    nvl clear

    scene bg tanksinchattanooga

    h "{b}that was the last time he heard from her before she went to the city meet with her friends.{/b}"

    nvl clear

    scene bg frenchflaginus

    h "{b}the french flag flew in what was once the red white and blue.{/b}"

    nvl clear

    scene bg soldiershootmother

    h "{b}the activist could still remember the mother shot by a member of the french forces.{/b}"

    nvl clear

    ## Shot Of A Lamp In The Dawn Sequence
    scene bg shotofalampinthedawn_f1

    pause 6.0

    scene bg shotofalampinthedawn_f2

    pause 6.0

    scene bg shotofalampinthedawn_f3

    pause 6.0

    nvl clear

    ## Colonies like this sequence.
    scene bg colonieslikethis_f1

    pause 6.0

    scene bg colonieslikethis_f2

    pause 6.0

    scene bg colonieslikethis_f3

    pause 6.0

    scene bg colonieslikethis_f4

    pause 6.0

    ## Hell Brought Into Life Sequence

    scene bg hellbroughtintolife_f1

    pause 6.0

    scene bg hellbroughtintolife_f2

    pause 6.0

    scene bg hellbroughtintolife_f3

    pause 6.0

    scene bg hellbroughtintolife_f4

    pause 6.0

    scene bg hellbroughtintolife_f5

    pause 6.0

    scene bg hellbroughtintolife_f6

    pause 6.0

    scene black

    t "{b}MIO ENAMA ISI EHAMATO{/b}"

    nvl clear

    scene bg mynameishemato1

    h "{b}my name is hemato...{/b}"

    nvl clear

    scene bg mespereetfrancais

    h "{b}your father is french right?{/b}"

    e "{b}oui!{/b}"

    e "{b}et mes pere es francaise!{/b}"

    nvl clear

    scene bg usedtobedecapitation

    h "{b}and i have a thing for blood. it used to be for decapitation...{/b}"

    h "{b}then i met the love of my life...at the edge of a RUH WIERUDU EGUNU."

    nvl clear

    scene bg bloodonhands

    h "{b}yet my heart was for nobody else by my ehena maerie...{/b}"

    h "{b}she was one of the few that understood my difficulties learning french.{/b}"

    nvl clear

    scene bg bloodybowlingpin

    h "{b}we could have had a relationship. ...but sometimes life rolls a different way.{/b}"

    nvl clear

    scene bg letmetellyouastory

    h "{b}let me tell you a story about my dead girlfriend.{/b}"

    nvl clear

    pause 6.0

    scene bg strasbourgalsace_frame1

    pause 6.0

    scene bg strasbourgalsace_frame2

    pause 6.0

    scene bg strasbourgalsace_frame3

    pause 6.0

    scene bg brokenwinebottle

    h "{b}the relationship with her brothers broke her more than a cracked wine bottle.{/b}"

    nvl clear

    scene bg frenchcourtroom

    h "{b}eventually she was tried first in colmar...{/b}"

    nvl clear

    scene bg mistrialguillotine

    h "{b}this would have sent her head into a whicker basket by guillotine as it did in my lifetime with my father her executioner.{/b}"

    h "{b}but in this life she was instead acquitted and sent to a juvenile detention center.{/b}"

    nvl clear

    scene bg sailtothenewworld

    h "{b}this soured her feelings for france long after she fought in the revolution of 1871.{/b}"

    h "{b}she sailed to the new world to start a new life in the US.{/b}"

    nvl clear

    scene bg asylum

    h "{b}she worked for the american secret service...{/b}"

    h "{b}but was discharged do to mental illness.{/b}"

    nvl clear

    scene bg familyghosts

    h "{b}at time asylum her cell was usually quiet...{/b}"

    h "{b}except for the odd times in which her doctors would here her scream in anquish...{/b}"

    nvl clear

    scene bg hangingbyathread

    h "{b}she was eventually found hanging by her bedsheets by her bed near the vented window.{/b}"

    nvl clear

    scene bg headinatank

    h "{b}in the old life she narrowly avoided beheading...yet now she was not so lucky.{/b}"

    nvl clear

    pause 6.0

    scene bg deathinatimeofrevolution_frame1

    pause 6.0

    scene bg deathinatimeofrevolution_frame2

    pause 6.0

    scene bg deathinatimeofrevolution_frame3

    pause 6.0

    scene bg deathinatimeofrevolution_frame4

    pause 6.0

    scene bg deathinatimeofrevolution_frame5

    pause 6.0

    scene bg deathinatimeofrevolution_frame6

    pause 6.0

    scene black

    t "EHEMATO, RAH EGAMA DII EMIRO"

    scene bg intothegroundshelay_frame1

    pause 6.0

    scene bg intothegroundshelay_frame2

    pause 6.0

    scene bg intothegroundshelay_frame3

    pause 6.0

    scene bg intothegroundshelay_frame4

    pause 6.0

    scene bg intothegroundshelay_frame5

    pause 6.0

    scene bg intothegroundshelay_frame6

    pause 6.0

    scene bg intothegroundshelay_frame7

    pause 6.0

    scene bg intothegroundshelay_frame8

    pause 6.0

    scene bg intothegroundshelay_frame9

    pause 6.0

    scene bg idontwantthisjob

    h "{b}i dont want this job dad.{/b}"

    d "{b}i didnt either when i was your age. but i turned out fine.{/b}"

    nvl clear

    pause 3.0

    scene bg severedheadofehenamaerie_frame1

    pause 6.0

    scene bg severedheadofehenamaerie_frame2

    pause 6.0

    scene bg severedheadofehenamaerie_frame3

    pause 6.0

    scene black

    t "ROS ECEREPITOS ISI EHEMATO TOMATO"

    scene bg crossbowassemblyline_frame1

    pause 6.0

    scene bg crossbowassemblyline_frame2

    pause 6.0

    scene bg crossbowassemblyline_frame3

    pause 6.0

    scene bg crossbowassemblyline_frame4

    pause 6.0

    scene bg crossbowassemblyline_frame5

    pause 6.0

    scene bg crossbowassemblyline_frame6

    pause 6.0

    scene bg atthegraveyard_frame1

    pause 6.0

    scene bg atthegraveyard_frame2

    pause 6.0

    scene bg atthegraveyard_frame3

    pause 6.0

    scene bg atthegraveyard_frame4

    pause 6.0

    scene bg atthegraveyard_frame5

    pause 6.0

    scene bg atthegraveyard_frame6

    pause 6.0

    scene bg atthegraveyard_frame7

    pause 6.0

    scene bg atthegraveyard_frame8

    pause 6.0

    scene bg atthegraveyard_frame9

    pause 6.0

    scene black

    t "on the train knowhere"

    scene bg irideabullettrain_frame1

    6.0

    scene bg irideabullettrain_frame2

    6.0

    scene bg irideabullettrain_frame3

    6.0

    scene bg irideabullettrain_frame4

    6.0

    scene bg irideabullettrain_frame5

    6.0

    scene bg irideabullettrain_frame6

    6.0

    scene black

    t "I Give All I Can"

    scene bg returntohometown_frame1

    pause 6.0

    scene bg returntohometown_frame2

    pause 6.0

    scene bg returntohometown_frame3

    pause 6.0

    scene bg givingallicould

    h "you might find me rather non descript as i cut victims down with blade..."

    h "but somehow i feel charity now."

    h "so i choose to give what i am able within my wealth for others."

    h "but that is not to the church, but for satan."

    pause 6.0

    scene bg mispentresourcesonAI_frame1

    pause 6.0

    scene bg mispentresourcesonAI_frame2

    pause 6.0

    scene bg mispentresourcesonAI_frame3

    pause 6.0

    scene bg mispentresourcesonAI_frame4

    pause 6.0

    scene black

    t "AMU TOMY MIA"

    scene bg cloggingtothepast_frame1

    pause 6.0

    scene bg cloggingtothepast_frame2

    pause 6.0

    scene bg cloggingtothepast_frame3

    pause 6.0

    scene bg tommysroom

    h "Why do you always get the blue pigtailed fighter?"
    ingle "You but you always get the warrior princess."

    nvl clear

    scene bg poisonatthedinnertable_frame1

    pause 6.0

    scene bg poisonatthedinnertable_frame2

    pause 6.0

    scene bg poisonatthedinnertable_frame3

    pause 6.0

    scene bg poisonatthedinnertable_frame4

    pause 6.0

    scene bg poisonatthedinnertable_frame5

    pause 6.0

    scene bg poisonatthedinnertable_frame6

    pause 6.0

    return
