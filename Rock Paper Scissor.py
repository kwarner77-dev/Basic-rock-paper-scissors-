# we import the canBeConverted function and the random package

import canBeConverted
import random

random.seed()   #we set our random seed value


# get the number of rounds

while True:           
    print('How many rounds would you like to play?  ')

    rounds = input('(enter an odd number in the range of 1 and 7):  ') 

    nrounds = None   #we set a variable nrounds(number of rounds) to None before we run through if statement

    if canBeConverted.toInt(rounds) == True:   #if statement using our canBeconverted function to see if its a valid integer
        nrounds = int(rounds)     

        if nrounds % 2 == 0 or nrounds > 7:  # next we use another if statement to check if the value within the variable is NOT allowed (if it is NOT a proper odd nunmber in range 1-7)
            nrounds = None 

    if nrounds == None:   # we add another if statement to check if nrounds is ==None (meaning something invalid was entered) and if it is then we prompt the user again for a valid odd number in range
        print('You must enter an odd number between 1 and 7. \n')
    else:   # however if nrounds isnt None, then it successfuly has been verified as a valid odd number in range
        break
    print()
print('Ready! \n')

humanwins = 0     
ties = 0     

#create a dictionary holding possible outcomes
whowon = {'rr': 'no one', 'rp': 'computer', 'rs': 'human',
                  'pr': 'human', 'pp': 'no one', 'ps': 'computer',
                  'sr': 'computer', 'sp': 'human', 'ss': 'no one'}

#play the rounds

for i in range(nrounds):   # for loop going through each round in variable nrounds

    print()
    print(' Round {}! \n'.format(i +1))     # we print the round we r in plus to get to proper number displayed

    while True:    

        #get the human's selection
        humanchoice = input('Make your choice! (r)ock  (p)aper   (s)cissors:   ')

        if humanchoice not in 'rps':
            print('The only valid options are r, p, or s.')

        else:
            break
        #get the computer's selection

    computerchoice = random.choice( ['r', 'p', 's'] )
        
    print()
    print('Computer chooses ' + computerchoice)

        #figure out who won

    winner = whowon[humanchoice + computerchoice]

    print()

    print('Result for this round: {} wins.'.format(winner) )

    if winner == 'human':
        humanwins += 1

    elif winner == 'no one':
        ties += 1

computerwins = nrounds - ties - humanwins

#display the final score

print()
print('Results: ')
print('Human: {}  Computer:  {}'.format(humanwins, computerwins))


if humanwins < computerwins:
    print()
    print('I am victorious! \n')

else:
    print()
    print('Eh, you got lucky\n')



