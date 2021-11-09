######################################################################
# Authors: Luke Wilson
# Usernames: wilsonl
# P01
# Purpose: Uses GUIs and key handles for user to use in a choose your own adventure
######################################################################
# Acknowledgements:
####################################################################################
import turtle                   # setting up turtle class
turt = turtle.Turtle()
turt.penup()                    # makes sure turtle is not writing when switch lines
turt.isvisible()
turt.speed(100)


class story:

    def __init__(self):             # sets the init values and adds new shapes to the turtle class
        """creates the class attributes such as the window the class uses and the turtles shapes"""
        self.wn = turtle.Screen()
        self.wn.bgcolor('yellow')
        self.wn.title("return to monkey")
        self.wn.addshape("photos/stage1.gif")
        self.wn.addshape("photos/stage2.gif")
        self.wn.addshape("photos/stage3.gif")
        self.wn.addshape("photos/stage4.gif")
        self.wn.addshape("photos/stage5.gif")
        self.wn.addshape("photos/stage6.gif")
        self.wn.addshape("photos/stage7.gif")
        self.wn.addshape("photos/stage8.gif")
        self.wn.addshape("photos/stage9.gif")
        self.wn.addshape("photos/lose.gif")

    def stage_1(self):                  # starting screen
        """acts as a title screen"""
        turt.goto(0, 50)
        turt.write("return to monkey", font=("arial", 20, "bold"))
        turt.goto(-300, 0)
        turt.write("You're a sad office worker who hates his life.", font=("arial", 10, "bold"))
        turt.goto(-300, -15)
        turt.write("You go home and watch a documentary about monkeys.", font=("arial", 10, "bold"))
        turt.goto(-300, -30)
        turt.write("You see how care free they are. You want to return to monkey.", font=("arial", 10, "bold"))
        turt.goto(-100, -70)
        turt.write("press 1 to continue    press 2 to continue being pathetic human", font=("arial", 10, "bold"))
        turt.goto(0, -200)
        turt.shape("photos/stage1.gif")

    def stage_2(self):                  # stage for deciding your path in the adventure
        """part of story"""
        turt.clear()
        turt.goto(-300, 0)
        turt.write("You go to work one day. You see your computer. You have a choice.", font=("arial", 10, "bold"))
        turt.goto(-300, -45)
        turt.write("press 1: smash computer and scream   press 2: be normal and use it for work", font=("arial", 10,"bold"))
        turt.goto(100, 100)
        turt.shape("photos/stage2.gif")

    def stage_3(self):
        """part of story"""
        turt.clear()                # part 2 of quest
        turt.isvisible()
        turt.goto(-300, 0)
        turt.write("You were fired for smashing company property but that's ok, human technology is evil.",font=("arial", 10, "bold"))
        turt.goto(-300, -15)
        turt.write("You go home and you are hungry. You see a can of spam and a bunch of bananas", font=("arial", 10, "bold"))
        turt.goto(-300, -30)
        turt.write("You have a choice", font=("arial", 10, "bold"))
        turt.goto(-300, -70)
        turt.write("press 1: eat bananas   press 2: eat spam", font=("arial", 10, "bold"))
        turt.goto(100, 100)
        turt.shape("photos/stage3.gif")

    def stage_4(self):                  # part 3 of quest
        """part of story"""
        turt.clear()
        turt.isvisible()
        turt.goto(-300, 0)
        turt.write("You eat the bananas and fall asleep. You wake up and notice you have a tail. This is good.", font=("arial", 10, "bold"))
        turt.goto(-300, -15)
        turt.write("You see some mail on your desk. You look at the letter and see that you owe 20k in taxes", font=("arial", 10, "bold"))
        turt.goto(-300, -30)
        turt.write("You have a choice", font=("arial", 10, "bold"))
        turt.goto(-300, -70)
        turt.write("press 1: tax evasion   press 2: pay your taxes", font=("arial", 10, "bold"))
        turt.goto(175, -150)
        turt.shape("photos/stage4.gif")

    def stage_5(self):                  # part 4 of quest
        """part of story"""
        turt.clear()
        turt.isvisible()
        turt.goto(-300, 0)
        turt.write("Good choice. Monkeys don't pay taxes. You start to grow hairy and have an urge to swing", font=("arial", 10, "bold"))
        turt.goto(-300, -15)
        turt.write("from vines. The next day you go to the zoo, you see the monkey exhibit", font=("arial", 10, "bold"))
        turt.goto(-300, -30)
        turt.write("You have a choice", font=("arial", 10, "bold"))
        turt.goto(-300, -70)
        turt.write("press 1: free your brothers     press 2: do nothing", font=("arial", 10, "bold"))
        turt.goto(100, 150)
        turt.shape("photos/stage5.gif")

    def stage_6(self):                  # part 5 of quest
        """part of story"""
        turt.clear()
        turt.isvisible()
        turt.goto(-300, 0)
        turt.write("You free the monkeys but the police chase you. You hide in the forest.", font=("arial", 10, "bold"))
        turt.goto(-300, -15)
        turt.write("The group of monkeys you freed follow you and accept you into their group", font=("arial", 10, "bold"))
        turt.goto(-300, -30)
        turt.write("One monkey is itchy and trying to pick bugs off himself", font=("arial", 10, "bold"))
        turt.goto(-300, -45)
        turt.write("You have a choice", move=False, font=("arial", 10, "bold"))
        turt.goto(-300, -75)
        turt.write("press 1: pick bugs off him and eat them     press 2: ew, gross. I'm not doing that.", move=False, font=("arial", 10, ("bold")))
        turt.goto(100, 150)
        turt.shape("photos/stage6.gif")

    def stage_7(self):                  # part 6 of quest
        """part of story"""
        turt.clear()
        turt.isvisible()
        turt.goto(-300, 0)
        turt.write("Great Choice! You lose the ability to speak. All you can do is make monkey noises", font=("arial", 10, "bold"))
        turt.goto(-300, -15)
        turt.write("The police catch up to you and the monkeys. Your fellow monkeys are scared.", font=("arial", 10, "bold"))
        turt.goto(-300, -30)
        turt.write("They threaten to take you to jail and put the monkeys back.", font=("arial", 10,"bold"))
        turt.goto(-300, -45)
        turt.write("You have a choice", font=("arial", 10, "bold"))
        turt.goto(-300, -75)
        turt.write("press 1: attack police with monkey strength     press 2: surrender.", font=("arial", 10, "bold"))
        turt.goto(100, 120)
        turt.shape("photos/stage7.gif")

    def stage_8(self):                      # part 7 of quest
        """part of story"""
        turt.clear()
        turt.isvisible()
        turt.goto(-300, 0)
        turt.write("You knock out the police and escape with your fellow monkeys", font=("arial", 10, "bold"))
        turt.goto(-300, -15)
        turt.write("You transform into a monkey. The other monkeys have accepted you as their leader.", font=("arial", 10, "bold"))
        turt.goto(-300, -75)
        turt.write("press 1 to continue", font=("arial", 10, "bold"))
        turt.goto(100, 150)
        turt.shape("photos/stage8.gif")

    def stage_9(self):              # tells player they won
        """part of story"""
        turt.clear()
        turt.isvisible()
        turt.goto(-300, 0)
        turt.write("you have returned to monkey", font=("arial", 20, "bold"))
        turt.goto(100, -100)
        turt.shape("photos/stage9.gif")

    def lose(self):                 # tells player they lost
        """part of story"""
        turt.clear()
        turt.goto(-300, 0)
        turt.write("You had a choice", font=("arial", 10, "bold"))
        turt.goto(-300, -15)
        turt.write("had...",font=("arial", 10, "bold"))
        turt.goto(-300, -75)
        turt.write("you will be stuck as a miserable human", font=("arial", 20, "bold"))
        turt.goto(100, 100)
        turt.shape("photos/lose.gif")