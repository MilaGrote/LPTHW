from sys import exit

def start():
    print """
    It's 2116, the world is infested by zobies.
    Zombies can't swim, so you get around by rowing down a river.
    To your right, there's an abandoned car packed with supplies.
    On the riverbank to your left, you suddenly hear screams.
    A little girl is being chased by what seems to be her Zombie dad.
    Where do you go?
    """

    choice = raw_input("> ")

    if choice == "left":
        little_girl()
    elif choice == "right":
        abandoned_car()
    elif choice == "girl":
        little_girl()
    elif choice == "car":
        abandoned_car()
    else:
        dead("You hesitate too long, an aligator jumps out and eats you alive.")


def abandoned_car():
    print """
    You quickly row over to the river-bank.
    While walking to the car, you hear the little girl scream:\n
    \t'HELP!!! MY DAD WANT'S TO KILL ME!!!.\n
                     \(*o*)/
                       )  )
                      /   /

    She's spotted you. How do you react?\n
    (a) You get in the car. She's not your responsibility.
    (b) You try to shoot the zombie from the opposite side of the river,
    (c) Your conscience sends you back so save her.
    """

    choice = raw_input("> ")

    if choice == "b":
        print """
        The loud noise attracts a zombie herd.
        Haven't you seen 'The Walking Dead'?
        """
        zombie_herd()
    elif choice == "a":
        dead("""
        A soccer-mom zombie jumps out of the car and eats your brains.
                                    (>*_*)> 'rawr'
         """)
    elif choice == "c":
        little_girl()
    else:
        print "Concentrate and make a proper decision!"


def little_girl():
    print """
    By the time you get there, the zombie has her at arm's length.
    She's struggling to keep him from biting her.
    You have a gun, a knife, and a bow and arrow that you've never used.
    How do you react?
    """

    choice = raw_input("> ")

    if "gun" in choice:
        print """
        The Zombie is dead.
        The gunshot attracted a large herd of Zombies from the road.
        Haven't you learnt anything from the walking dead?
        """
        zombie_herd()
    elif "knife" in choice:
        print """
        You jab the knife into his head and watch him die.
        you grab the little girl and?\n
        (a) Run toward the road
        (b) Get in the boat and cross the river.
        """
        choice = raw_input("> ")

        if choice == "a":
            print """
            You run right into a herd of Zombies.
            """
            zombie_herd()

        elif choice == "b":
            print "\tYou row to the otherside,"
            print "\tget out of the boat and?...\n"
            print "\t(a) Head straight to the car."
            print "\t(b) Look around."

            choice = raw_input("> ")

            if choice == "a":
                print "\t A soccer-mom zombie jumps out of the car and eats your brains."
                dead("\t\t\t (>*_*)>'rawr'")
            elif choice == "b":
                print """
                The girl spots a zombie:\n
                'MY MOM IS ONE OF THEM!!!'
                      \(*o*)/
                        )  )
                       /   /
                ..do you run or try to kill the soccer-mom zombie?
                """
                choice = raw_input("> ")

                if "run" in choice:
                    zombie_herd()
                elif "kill" in choice:
                    print "\tYou kill the soccer-mom zombie,"
                    print "\tget in the car,"
                    print "\tand drive off."
                    print "\tCongrats! You both survive the Zombie Apocalypse!!!"
                    print "\t(>'o')> ^('-')^ <('o'<)^('-')^(>'o')> ^('-')^ <('o'<)"
                    exit(0)

                else:
                    print """
                    That's not an option. Try again.
                    """
        else:
            print "Don't be foolish, that's not an option..."

    elif "arrow" in choice:
        print """
        You idiot.
        You don't know how to use that thing.
        You've missed and shot the little girl.
        The zombie is now chewing on her arm.
        What are you gonna do now?\n
        (a) Kill the girl.
        (b) Kill her dad.
        (c) Run
        """

        choice = raw_input("> ")

        if choice == "a":
            dead("""
            The zombie-dad eats you brains while you kill his daughter.
                                     (>*_*)> 'rawr'
            """)
        elif choice == "b":
            dead("""
            The now zombie-girl eats you while you kill her dad
                                (>*_*)> 'rawr'
            """)
        elif choice == "c":
            zombie_herd("You run right into a herd of zobies.")

    else:
        print "You can't do that. Try again."

def zombie_herd():
    print """
    They eat your brains.
    Congrats, You are now a Zombie.
    (>*_*)> ^(* _ *)^ <(*_*<)
    """
    exit(0)


def dead(why):
    print why, " "
    exit(0)

start()
