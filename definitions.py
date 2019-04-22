import os 
import time 


def startGame():
    os.system("clear")
    print "\t\tpWORKINGd"
    print """
    The goal of this game is to make the
    command line learning experience more enjoyable.
    
    Enjoy!
    """ 

    print "\n\nThis game is under construction. Come back later.\n\n"
    exit()

def level3c():
    print """
    Nice! You're ready to play.
    type 'exit' to leave the tutorial.
    """
    
    answer3c = raw_input("$ ")

    if answer3c == "exit":
        startGame()
    else:
        print "type 'exit' and hit enter."
    
def level3b():
    print "text.txt"
    
    answer3b = raw_input("$ ")

    if answer3b == "less text.txt":
        level3c()
    else:
        print "type 'less text.txt' and hit enter."

def level3a():
    print "pWORKINGd/tutorial/levelll"
    
    answer3a = raw_input("$ ")

    if answer3a == "ls":
        level3b()
    else:
        print "type 'ls' and hit enter."

def level3():
    os.system("clear")
    print "\n\t\tTutorial: Level 3."
    print """
    \n\tDirections:
    Type this in order. Hit enter after each command.
    1. pwd
    2. ls
    3. less text.txt 
    4. 
    """
    answer3 = raw_input("$ ")

    if answer3 == "pwd":
        level3a()
    else:
        level3()
   


def level2():
    os.system("clear")
    print "\n\t\tTutorial: Level 2."
    print "\n\tDIRECTIONS:"
    print "-List the directory"
    print "-Type 'ls' and hit enter to see what is here.\n\n"
    print "$ pwd"
    print "/pWORKINGd/tutorial/level_two"
    right_answer = False

    while True:
        answer2 = raw_input("$ ") 

        if answer2 == "ls":
            print "lvl1.txt\tlvl2.txt\tlvl3.txt"
            print "\n\n\t\tType 'less lvl3.txt' to look at the lvl3 text file."
        elif answer2 == "less lvl3.txt":
            print "\n\n\t###tutorial/levelll###"
            clock = 4

            while clock >0:
                time.sleep(1)
                clock -=1
                intro()
        elif answer2 == "less lvl2.txt":
            print "\n\n\t###tutorial/level_two###"
        elif answer2 == "less lvl1.txt":
            print "\n\n\t###tutorial/level1###"              
        else:
            print "No"
            level2()


def level1():
    os.system("clear")
    print "\t\tTutorial: Level 1."
    print "$ pwd"
    print "/pWORKINGd/tutorial/level1"
    print "\n\t\tQuestion: How do you print the working directory?\n"

    answer1 = raw_input("$ ")

    if "pwd" in answer1:
        os.system("clear")
        print "Correct."
        print "\n\n\n(READ THIS) (READ THIS) To access level 2 change the directory to 'tutorial/level_two'. (READ THIS) (READ THIS)"
        clock = 3

        while clock >-1:
            time.sleep(1)
            clock -=1
        intro()
    else:
        print "type 'pwd' and hit enter"
        level1() 



def intro():
    print "\n\t\t\t\tpWORKINGd\n"
    print "\t   KEY:"
    print "pwd = print working directory"
    print "cd = change directory"
    print "\n\tDIRECTIONS:"
    print "- To access level 1 change the directory to 'tutorial/level1'"
    print "- Type 'tutorial/level1' and hit enter."
    print "\n\n$ pwd"
    print "/pWORKINGd/"
    userinput = raw_input("cd ")

    if userinput == "imready":
        startGame()
    elif userinput == "tutorial/levelll":
        level3()
    elif userinput == "tutorial/level_two":
        level2()
    elif userinput == "tutorial/level1":
        level1()    
    else:
        os.system("clear")
        intro()


