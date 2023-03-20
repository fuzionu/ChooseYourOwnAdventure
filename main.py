name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

while True:
    answer = input("You are on a dirt road, it has come to an end and you can go left or right."
                   " Which way will you go? LEFT/RIGHT\n> ").lower()
    if answer == "left" or answer == "right":
        break
    else:
        continue

if answer == "left":
    while True:
        answer = input(
            "You come to a river, you can walk around it or swim across. What will you do? WALK/SWIM\n> ").lower()

        if answer == "walk" or answer == "swim":
            break
        else:
            continue

    if answer == "swim":
        print("You swam across and were eaten by an aligator.\nGAME OVER!")
        quit()
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died of thirst.\nGAME OVER!")
        quit()

elif answer == "right":
    while True:
        answer = input(
            "You come to a bridge, it looks wobbly, do you want to cross it or go back? CROSS/BACK\n> ").lower()

        if answer == "cross" or answer == "back":
            break
        else:
            continue

    if answer == "cross":
        while True:
            answer = input("You carefully cross the bridge, it creaks, you sweat but you made it.\n"
                           "After crossing you met a stranger. Do you want to talk to him? YES/NO\n> ").lower()

            if answer == "yes" or answer == "no":
                break
            else:
                continue

        if answer == "yes":
            while True:
                answer = input("The stranger seem to be a thief. He takes out a knife and tells you to give your money.\n"
                    "Will you give it? YES/NO\n> ").lower

                if answer == "yes" or answer == "no":
                    break
                else:
                    continue

            if answer == "yes":
                while True:
                    answer = input("The thief takes your money and leaves with happy face.\n"
                                   "You walk forward and see a woman on the side of the road.\n"
                                   "She asks you for help.\n"
                                   "Will you help? YES/NO\n> ").lower()

                    if answer == "yes" or answer == "no":
                        break
                    else:
                        continue

                if answer == "yes":
                    print("You help her get up. She is very pretty. You take her on your arms and walk to the doctor")
                    print("Doctor helps her, she is very thankful to you and wants to spend time with you.")
                    print("Later you marry her. GAME WON!")
                elif answer == "no":
                    print("You walk past her while she is begging for help. You leave her there.")
                    print("Later as she couldn't move on her own she was eaten alive by a wolf.")
                    print("You couldn't stand what you did, so you hanged yourself on a tree.\nGAME OVER!")

            elif answer == "no":
                print("The thief stabs you in the stomach and takes your money. You die of injury.\nGAME OVER!")

        elif answer == "no":
            print(
                "You walk past the stranger, but he is a thief. He takes out a knife and stabs you in the back.\nGAME OVER!")

    elif answer == "back":
        print("You walked back, slipped on a rock, fell on your head and died of head injury.\nGAME OVER!")
