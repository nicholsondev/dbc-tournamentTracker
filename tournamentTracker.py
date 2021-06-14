# main function to prompt user for the number of participants in the tournament
def main():
    

    print('Welcome to the Last Tournament\n============================')
    while True:
        try:
            getParticipantCount = int(input('How many participants are going to compete: '))
            if getParticipantCount > 0:
                print(f'\nThere are {getParticipantCount} particpant slots ready to be filled!\n')
                mainMenu(getParticipantCount)
                break
            else:
                print('It needs to be above 0')
        except ValueError:
            print('That is not a valid number. Try again...')

    
# main menu
def mainMenu(getParticipantCount):
    import sys
    tournamentList = [None] * getParticipantCount
    finished = False
    
    # loop to continue menu until they exit
    while not finished:

        print('\nMain Menu\n=========\n1. Sign a player up\n2. Remove a player from the Tournament\n3. View the participant list\n4. Exit\n')
        # try/catch to look for int only for the menu
        while True:
            try:
                choice = int(input('Select one of the options.\n'))
                break
            except ValueError:
                print('That is not a valid number. Try again...')
        # go to respective function once choice is made  
        if choice == 1:
            addParticipant(tournamentList)
        elif choice == 2:
            removeParticipant(tournamentList)
        elif choice == 3:
            viewParticipants(tournamentList)
        elif choice == 4:
            while True: 
                exit = input('Exit\n====\nDo you really have to go?\nExit? (y/n): ').lower()
                if exit == 'n':
                    finished = False
                    break
                elif exit == 'y':
                    print('\nUntil next time!')
                    finished = True
                    break
        else:
            print('Please choose one of the options above!!!')


# add player 
def addParticipant(tournamentList):
    finished = False
    limit = len(tournamentList)

    print('\nTime to add in a Participant\n============================')
    name = input('Enter player name: ')

    while not finished:
        
        # loop to make sure they are entering a number with in the available slot range
        while True: 
            try: 
                position = int(input(f'Choose your starting position # 1 - {limit}: '))
            except ValueError:
                print('That is not a number.')
            else:
                if 1 <= position <= limit:
                    break
                else:
                    print(f'Out of range. Enter a number between 1 and {len(tournamentList)}\n')

        if tournamentList[position-1] == None:
            tournamentList[position-1] = name
            print(f'You have successfully signed {name} up in position #{position}.\n')
            finished = True
        else:
            print(f'I am sorry! Position #{position} is already taken.\n')
    return(tournamentList)

# remove player
def removeParticipant(tournamentList):
    finished = False
    limit = len(tournamentList)
    print('\nWho are you removing now?\n=========================')

    while not finished:
        
        name = input('Enter player name: ')
        position = int(input(f'Choose your starting position # 1 - {limit}: ')
)
        if tournamentList[position - 1] == name:
            tournamentList[position - 1] = None
            print(f'{name} has been successfully erased from the tournament listing\n')
            finished = True
        else:
            print(f'{name} is not in that position\n')
    return(tournamentList)

# view participant list
def viewParticipants(tournamentList):
    print('\nView Participants\n=================')
    # selection to be added if they want to look up single participant
    # position = input(f'Pick the participant slot you want to view # 1 - {len(tournamentList)}: ')

    for position, name in enumerate(tournamentList):
        print(f'{position + 1:}: {name}')

if __name__ == '__main__':
    main()