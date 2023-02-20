#!/usr/bin/python


from sys import exit
import random
import time


def battle(c_name, c_h):
    contenders.append(c_name.upper() +  " - from house " + c_h)

def pick_name(household,m_house):
    household.sort()
    print "write down the first name of the child who should compete for the game of thrones"
    name = raw_input("> ")

    if name in household:
       battle(name, m_house)

    else:
          print "Eh! You need to enter one of the names of the stark household that you used to get access through the gates"
          pick_name()

def prepare_names(v_l):
    v_n = [l.lower() for l in v_l] 
    v_n.sort()
    return v_n

def house_lannister(xy):
    household = ['jamie','tyrion','cersei']
    my_house = xy
    print "You open the Gates to Casterly Rock and it appears a tourney is going on"
    print "All clans and banner men of house %s are present" % (my_house)
    print """
    You spot the 3 children of Lord Tywin sitting close to your left above the melee but a guard stops you before you can be allowed into the tournament"
    You need to recite the first names of Lord Tywin's children to the guard to be allowed in
    """
    v_typed_names = []
    for i in household:
        v_typed_names.append(raw_input("@@@Type a name and press ENTER> "))

    household.sort()
    typed_names = prepare_names(v_typed_names)
    
    
    if typed_names == household:
       print """
       Congratulations! You've been allowed in
       You are finally sitted with the crowd and a man hands you goat skin, a feather and a wooden box
       """
       pick_name(household,my_house)

    else:
      print "You know nothing %s\nBye!\n" % your_name
      exit(1)


def house_targaryan(xy):
    household = ['dany','viserys']
    my_house = xy
    print "You arrive at blackwater bay in dragonstone and marvel at the beautiful castle"
    print "You immediately spot 2 dragons flying overhead with Aerys Tygaryan's children riding each one"
    print """
    You anchor your boat and walk to the gates. 
    To be let in, you need to write the first names of both children on the ground infront of you
    A guard will open the door and check the names before you are let in    
    """    
    v_typed_names = []
    for i in household:
        v_typed_names.append(raw_input("@@@Type a name and press ENTER>"))

    household.sort()
    typed_names = prepare_names(v_typed_names)

    if typed_names == household:
       print """
       Congratulations! You've been allowed in
       You are met by 2 members of the king's guard. One of them hands you ink, a piece of cloth and a dragon claw for writing 
       """
       pick_name(household,my_house)

    else:
      print "You know nothing %s\nBye!\n" % your_name
      exit(1)


def house_stark(xy):
    household = ['rob','sansa','arya','brandon','rickon','jon']
    my_house = xy
    print "You open the Gates to winterfell and a raven approaches you with a message"
    print "You open up the message and it contains the first names of all the children raised in winterfell by Lord Ned Stark "
    print """ 
    Suddenly, a direwolf, comes and snatches this list from your hands. Hope you remember the names... "
    To your right, there's an electronic door that you need to go through"
    On a keypad connected to the door, type in the names that were listed in the message
    """

    v_typed_names = []
    for i in household:
        v_typed_names.append(raw_input("@@@Type a name and press ENTER> "))

    household.sort() 
    typed_names = prepare_names(v_typed_names)

    if typed_names == household:

       print """
       Congratulations! You've unlocked the door
       To your left, there's a grand dining room table with a ballot box on it. Beside the ballot box is a pen and paper
       """

       pick_name(household,my_house)

    else:
      print "You know nothing %s\nBye!\n" % your_name    
      exit(1)


def pick_house():
    c_input = raw_input("> ")
    chosen_house = c_input.lower()

    if chosen_house == 'stark':
        print "The chosen house is", chosen_house
        house_stark(chosen_house) 
        return chosen_house
    elif chosen_house == 'lannister':
        print "The chosen house is", chosen_house
        house_lannister(chosen_house)
        return chosen_house
    elif chosen_house == 'targaryan':
        print "The chosen house is", chosen_house
        house_targaryan(chosen_house)
        return chosen_house
    else:
        print "You have to choose one %s" % your_name
        pick_house()


def manage_houses():
    if len(houses) != 0:    
       ch = pick_house()
       houses.remove(ch)
       avail_houses = houses
       
       
       if len(avail_houses) > 0:
          print
          print "*" * 30
          print "Choose another house from the below"
          print "*" * 30

          for h in avail_houses:
              print h

       manage_houses()

    else:
       #print "All houses have been visited" 
       print
       print "The contenders for the throne are:"  
       for x in contenders:
           print x

       

def start():
    print "Welcome to the Game of Thrones %s !!!" % your_name
    print "Only one House can Rule the Seven Kingdoms"
    print "You have to choose a memeber of each house to battle"
    print "Eventually the winner will be declared King and sit on the Iron Throne"
    print "You have 3 houses to choose from:"
    print """
          Stark - (based in Winterfell)
          Lannister - (based in Casterly Rock)
          Targaryan - (based in Dragonstone)
          """
    manage_houses()
    print 
    print "The fighting has commenced....!!"
    print "It's looking really grisly with body parts flying all around..."
    print "It's looking EPIC! We have to wait to know who wins....\n"
    
    #time.sleep(10)

    for r in range(1,40000):
       for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
    
    winner = random.choice(contenders)

    print "We have a winner......"
    print 
    print "%" * 83 
    print "%" * 5, winner, "will inherit the Iron Throne in Kings Landing", "%" * 5
    print "%" * 83
    print
    print
    print "Well done %s, hope you play again soon :)" % your_name
    print

    
your_name = raw_input("What do you want us to call you: ")
houses = ['stark','lannister','targaryan']
contenders = []
chosen_house = '' 
start()
