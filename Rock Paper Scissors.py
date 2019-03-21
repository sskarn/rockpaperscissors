"""
Karnbir Saini
ICS2O0-B
Nov 7, 2017
Rock Paper Scissors
This program is a rock paper scissors game against the PC. The computer uses a list and a random chooser to choose a selection. It has a score counter and is restartable. 
"""

from random import choice #import random chooser 
name = raw_input("Enter your name : ") #Name Input for end game
rps = ['r','p','s'] #RPS List
cw = 0 #Computer Wins Variable
pw = 0 #Player Wins Variable
restartprompt = 1 #restartprompt counter to allow restarts

#While results in a loop
while (restartprompt == 1): #checks for restartprompt to be 1 to restart, else doesn't restart
    print "R: Rock,      P: Paper,     S: Scissors" #Prints options to player
    user = raw_input("Enter your choice among the three : ") #Player inputs option
    user = user.lower() #Turns Player input option to lower case
    py = choice(rps) #Computer selects option randomly

    if user == py: #Tie Display
        print "You chose " + user + ".", " Computer chose " + py + "."
        print "Hence a Tie!"
        print "Computer: ",cw
        print name,": ",pw

    elif user == 'r' and py == 's': #If User has Rock and Computer has Scissors
        print 'You entered Rock. Computer had Scissors. You win!'
        pw+=1
        print "Computer: ",cw
        print name,": ",pw 
    elif user == 'r' and py == 'p': #If User has Rock and Computer has Paper
        print 'You entered Rock. Computer had Paper. You lose!'
        cw+=1
        print "Computer: ",cw
        print name,": ",pw 
    elif user == 's' and py == 'p': #If User has Scissors and Computer has Paper
        print 'You entered Scissors. Computer had Paper. You win!'
        pw+=1
        print "Computer: ",cw
        print name,": ",pw 
    elif user == 's' and py == 'r': #If User has Scissors and Computer has Rock
        print 'You entered Scissors. Computer had Rock. You lose!'
        cw+=1
        print "Computer: ",cw
        print name,": ",pw 
    elif user == 'p' and py == 's': #If User has Paper and Computer has Scissors
        print 'You entered Paper. Computer had Scissors. You lose!'
        cw+=1
        print "Computer: ",cw
        print name,": ",pw 
    elif user == 'p' and py == 'r': #If User has Paper and Computer has Rock
        print 'You entered Paper. Computer had Rock. You win!'
        pw+=1
        print "Computer: ",cw
        print name,": ",pw

    if restartprompt == 1: #Restart Prompt if statement
        continueprompt = raw_input("Do you want to continue? Type y to continue, type anything else to end game.") #continue prompt to restart game
        continueprompt = continueprompt.lower() #Sets input to lower case just in case of a capital case input
        if continueprompt == 'y':
            restartprompt == 1
        else:
            break
        
