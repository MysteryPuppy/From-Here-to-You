#From me to you
#Music from Jukedeck - create your own at http://jukedeck.com.

define m = Character(_("Melon"), color="#FAA8D0")
define k = Character(_("Kiwi"), color="#C3FFC6")

# The game starts here.

label start:
    #Variables
    $ happy = 0
    $ dango = False

    #play music "<loop 0>music/friends.ogg" fadein 2.0

    scene bg bedroom
    with fade

    show kiwi sleep at left
    show melon sleep at right

    k "...zzz..."
    m "...zzz..."
    k "...zzz..."
    m "...zzz..."
    k "..."
    k "...Bmmfhh."
    k "Ughh...Okay wake up time."
    show kiwi grumpy at left
    k "Yaaawn."
    k "Time to go to school..."
    show kiwi normal at left
    k "Okay...I got this, just a few more days left until break."
    k "You've got this kiwi!"
    k "Just a few more days until you get to see her..."
    show kiwi blush at left
    k "Ahhh..."
    k "Okay okay, let's go."

    scene bg fewhours
    pause 4

    scene bg schoolbedroom
    show kiwi normal at left
    show melon sleep at right
    m "zzz...zzz..."
    m "zzz-"
    show melon normal at right with vpunch
    m "I'm up!"
    show melon grump at right
    m "Oh- It's sort of late. Dang it."
    show melon normal at right
    m "Wow but it really is almost time."
    show melon silly at right
    m "Ahh, I can hardly wait."
    show melon normal at right
    m "I wonder when Kiwi is getting back home..."
    show melon grump at right
    m "School lasts too long.."
    m "Hmpph...Summer vacation isn't even fun without him."
    show melon normal at right
    m "Well I hope he's learning a lot."
    m "I'll write him a long text I guess while I wait."
    show melon silly at right
    m "Hehe, I'll write something a lil lewd, hmm~"
    m "Pft..."
    show melon pnormal at right
    m "Okay, let's get to work!"
    m "Ahem..."
    #play music "typing.sumn"
    m "Welcome home my sunshine! I hope that you slept super well and that..."
    m "You had a great day at school. Tell me all about it please!"
    show melon pblush at right
    m "You know I love hearing about your day..."
    m "It makes me very, very happy."
    m "Don't forget that you're the best boyfriend in the whole wide world!"
    show melon pnormal at right
    m "I can't wait to talk"
    m "With love, melon"
    show melon normal at right
    m "And send!"

    scene bg bedroom

    show kiwi pblush at left
    show melon normal at right

    k "Honey I'm home!"

    show melon pnormal at right
    m "Wha- Kiwi!! I just finished sending you my text!"
    show kiwi pblush at left
    k "I know! I just read it and it was really cute. It made me smile so much."
    m "Aww...babe..."
    show melon pblush at right
    m "You're going to make me blush."
    show kiwi psmirk at left
    k "Hehe, cutie."
    show melon pnormal at right
    show kiwi pnormal left
    m "How was school kiki?"
    menu:

        k "Oh you know it was uhh.."

        "Same as always":
            jump same

        "Pretty good!":
            $ happy+=1
            jump good

label same:
    k "Aw, you know, it was how it usually is."
    show kiwi psleep at left
    k "I fought to stay awake most of the time, urg."
    show kiwi pnormal at left
    k "But that doesn't really matter since school is almost out!"
    m "Mm, I guess not but I wish you had more fun at school."
    m "You're so good at it after all."
    show melon psilly at right
    m "Oh well, I'm really excited for break too, ahh~"
    m "We're going to have so much fun."
    k "Yeah, I can't wait!"
    jump continue1

label good:
    k "It was actually really interesting today!"
    k "My history teacher is really funny."
    show kiwi psilly at left
    k "He makes the worst jokes to be honest."
    k "And everyone pretends to hate them but they're actually kinda good."
    show kiwi pnormal at left
    m "Aww, I see!"
    m "I'm really happy you had fun today."
    m "I want you to have fun all day, all the time."
    show melon psad at right
    m "Even when we can't talk or hang out."
    show melon normal at right
    m "But soon we'll be able to hang out all day."
    k "Mm! I can't wait!"
    jump continue1

label continue1:
    m "Oh! So babe your plane arrives at 6 pm right?"
    k "Lemme see...yeah! 6pm your time."
    m "Hehe, we still have time that night then to...do stuff."
    show kiwi psmirk at left
    k "Babe...what are you saying?"
    show melon pblush at right
    m "N-Not {b}THAT{/b}!"
    m "Geee..."
    show melon psilly at right
    m "I meant that we can play some video games or something."
    m "Maybe watch a movie!"
    show melon pnormal at right
    show kiwi pnormal at left
    k "Hehe, I know mel."
    k "Although I do remember you saying before that you wanted to-"
    show melon pblush at right
    m "KIWI! I said what I said b-but we don't have to talk about it now."
    show melon pgrump at right
    m "H-Hmph."
    show kiwi psilly at left
    k "Hehe, I know you want all this."
    m "..."
    m "...Well...Yeah."
    show melon pblush at right
    m "I always want you. You're the most important person in the world to me."
    m "How could I not want all of you."
    show kiwi pblush at left
    k "W-wha-"
    show melon psilly at right
    m "Hehe."
    m "Now it's your turn to blush, hotshot."
    show melon pnormal at right
    show kiwi pnormal at left
    k "Okay, okay you got me."
    k "But yeah, I can't believe we're going to be hugging in two days."
    k "It's been way too long."
    show melon psad at right
    m "Ah, I know. Five months felt like an eternity."
    m "School really gets in the way of traveling..."
    show melon pnormal at right
    k "It is what it is."
    show melon psilly at right
    m "But I wouldn't change it for the world!"
    show kiwi pblush at left
    k "Aww..."
    show melon pnormal at right
    show kiwi pnormal at left
    menu:
        m "Oh...But..."

        "Do you think it was too many months apart?":
            $ happy+=1
            jump toomany

        "It is kind of tough though sometimes":
            jump tough


label toomany:
    k "Hm..."
    k "I mean, it was a long time but I had fun every day with you."
    k "Eventhough we were apart."
    show kiwi pblush at left
    show melon pblush at right
    k "I just want to be able to talk to you and spend time with you."
    k "And it's always worth it when we see eachother again."
    k "So that's why I wouldn't say it's ever too much."
    m "Aw..Kiwi..."
    show melon pnormal at right
    m "Ah, I feel the same way."
    m "Even apart, you're my best friend."
    m "A-And the best boyfriend ever..."
    m "I wouldn't want to spend my time any other way or with anyone else."
    m "You're just...the best."
    show melon pblush at right
    m "> //// <"
    k "> //// <"
    show melon pnormal at right
    show kiwi pnormal at left
    k "But, that doesn't change the fact that I can't wait to see you again."
    k "In real life."
    m "I know baby. I can't wait either."
    show melon psilly at right
    m "I'm going to kiss and snuggle you so much! You better watch out!"
    show kiwi psilly at left
    k "Ohh nooo~ How awful~"
    k "Hehe."
    show kiwi pnormal at left
    jump continue2

label tough:
    m "Hmm, but it has been a little hard recently..."
    m "I mean, since you have to study so much and I have work."
    show melon psad at right
    m "We hardly get time to talk..."
    k "Babe..."
    show melon pnormal at right
    k "You know I dislike not being able to talk to you as much too."
    k "But that period is almost over...I almost have break."
    m "Yeah, you're right. I'm just being a crybaby."
    show kiwi pgrumpy at left
    k "No...hey. Mel I get upset too a lot..."
    show kiwi pnormal at left
    k "I just don't want you to feel bad since I know you're busy too."
    m "M-Mm.."
    show melon psad at right
    m "I know, I just love you a lot..."
    m "And you're my best friend so..."
    m "I always want to talk to you."
    k "I know and I'm sorry baby."
    k "We'll get to talk all day soon."
    show melon pnormal at right
    m "I know.."
    m "Okay, okay. No being sad."
    m "It'll all be better when I get to hold you in my arms."
    jump continue2

label continue2:
    show melon pgrump at right
    m "Ahh, I just want these remaining days to be over already!"
    show melon pnormal at right
    k "They'll pass before you know it, cutie."
    m "That's true!"
    m "Oh! Babe, lemme move to the living room."
    m "I think my internet is dying in here. One sec!"
    k "Alright!"
    scene bg bedliving
    show melon pnormal at right
    show kiwi pnormal at left
    m "Back! Sorry about that."
    k "Aw, no problem babe. I hope the internet's better!"
    m "I think it is."
    m "Want to watch some anime?"
    k "I would love to!"
    show melon psilly at right
    m "Awesome! Lemme check if there's any new good series out."
    k "I'll look too!"
    show melon pnormal at right
    m "Hey...Kiki.."
    k "Yes Melmel?"
    show melon pblush at right
    m "I love you."
    show kiwi pblush at left
    k "I love you too. More than anything."

    scene bg oneweek
    pause 4
    scene bg airportbedroom

    show kiwi normal at left
    show melon sleep at right
    k "Whew, it's pretty early..."
    k "Melon's probably still sleeping, hehe."
    k "I'll send her a text though before I get on the plane."
    show kiwi pnormal at left
    k "To my lovely girlfriend,"
    k "There's only a few more hours until we're together in the same room."
    k "I'm both nervous and very, very, very excited."
    k "I can't wait to bury my head against your shoulder and just..."
    k "Be like that, in peace, for a long time."
    k "I love you with all I've got."
    show kiwi pblush at left
    k "From, Kiwi"
    show kiwi normal at left
    k "Okay. Time to board."
    k "Ahh, I'm so excited."
    k "I hope Melon doesn't get too nervous while I'm gone."
    k "Ah, gotta go."
    hide kiwi normal at left
    scene bg fewhours
    pause 4
    scene bg airportbedroom
    show melon sleep at right
    m "zzz...zzz..."
    m "zz..kiwi...have to-"
    m "Wh-"
    show melon normal at right
    m "Wait...mm...what time is it..."
    m "WHAT??!!"
    show melon grump at right
    m "Ahh, no...I didn't get to wish kiwi safe travels..."
    m "Dang it, why do I always sleep late for these things?"
    m "*Sigh*"
    show melon blush at right
    m "Well, I hope his flight is going well."
    m "Ahh.."
    show melon normal at right
    m "I better get ready for him to arrive though!"
    m "Alright! Let's clean this mess up."
    m "I'll just tuck the dirty pile of clothes in here and uhm..."
    m "Get some new sheets and stuff!"
    show melon normal at right with vpunch
    m "Okay! That looks about all tidied up."

    menu:
        m "Hmm, but am I forgetting anything...?"

        "Yes!":
            $ happy+=2
            $ dango=True
            jump yes

        "Nope.":
            jump nope

label yes:
    m "Oh! Of course!"
    show melon silly at right
    m "I almost forgot his gift!"
    m "Gosh I would have gotten upset with myself if I forgot."
    scene bg grumpycat
    m "I got him this picture..."
    m "Since he loves fluffy cats."
    m "Hehe..look how grumpy..."
    scene bg airportbedroom
    show melon normal at right
    m "Ah, he's going to love it!"
    jump continue3

label nope:
    show melon normal at right
    m "Hmm, nope, I guess that's everything!"
    m "I don't even care if I'm forgetting something to be honest."
    show melon silly at right
    m "I Just want to see his face and give him a big hug."
    jump continue3

label continue3:
    show melon normal at right
    m "It's time to head to the airport to pick him up."
    show melon blush at right with vpunch
    m "I'm so excited I can hardly contain it!"
    show melon normal at right
    if dango==True:
        m "Okay, I got the cat picture, my keys..."
        m "Mm! That's everything!"
    m "I'm good to go I think."
    show melon silly at right
    m "Kiwi, here I come!"

    scene bg airport
    show melon normal at right
    m "Waiting at the airport is always the hardest..."
    show melon sad at right
    m "I get so nervous..."
    m "I hope everything went well with his trip."
    show melon normal at right
    m "No sad thoughts! Just happy ones. Calm down mel."
    m "He's going to walk through that door any moment an-"
    m "And-"
    show melon blush at right
    m "..."
    m "..."
    m "..."
    m "..."
    scene bg end with fade
    show melon blush at right with vpunch
    show kiwi blush at left with vpunch
    m "KIWI!!"
    k "MELON!!!"
    scene bg together

    m "I'm so happy to see you."
    m "You have no idea."
    k "No..I know melon, I know."

    if happy == 4:
        m "wow, you seem really happy these days!"
    else:
        m "I'm going to make you happier."

    scene bg end
    show melon blush at right
    show kiwi blush at left

# This ends the game.

    return
