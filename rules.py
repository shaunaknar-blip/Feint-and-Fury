#This module explains the rules line by line if the user wants to read them.
def rules(hpp,hpc):
    while True:
        x = input('Do you want to read the rules first Y/N: ')
        if x.lower() == 'y' or x.lower() == 'yes': # using the .lower() function makes the variable case insensitive.
            print('Let\'s look at some brief rules before you play this simple game')
            
            '''this time variable is used to guide the user slowly through the rules
                if the player is shown all the rules at once it could feel overwhelming,
                so this shows only tiny snipets one at a time.'''
            
            time = input('\nPress Enter to read further: ')
            print('\n#OBJECTIVE\n')
            print('The player is supposed to fight against their opponent which is the computer.')
            time = input('\nPress Enter to read further: ')
            print('\n#ATTACK TYPES\n')
            print('The player can use the following attack types:')
            print('1. SLASH')
            print('This move deals 10 damage to the opponent if the attack is successful\n')
            print('2. FIREBALL')
            print('This move deals 15 damage to the opponent if the attack is successful\n')
            print('3. ARROW SHOT')
            print('This move deals 5 damage to the opponent if the attack is successful\n')
            print('4. THUNDER BOLT')
            print('This move will deal 25 damage to the opponent if successful and will also deal 5 damage to you as well.')
            print('So use it carefully\n')
            time = input('\nPress Enter to read further: ')
            print('\n#CHECKING ATTACK\n')
            print('To check if an attack is successful, a die will be rolled by the computer.')
            print('If the outcome is 1, then the attack is dealt successfully')
            print('If it is 2, then the attack nearly missed the opponent and no one gets damage')
            print('If it is 3, then the attack missed completely and the opponent will attack\n')
            time = input('\nPress Enter to read further: ')
            print('\n#INVENTORY\n')
            print('You have a predefined inventory, which has a set number of Strength Potions and  Health Potions')
            print('Every strenght potion gives you +2 strength.\n')
            time = input('\nPress Enter to read further: ')
            print('\n#POTIONS\n')
            print(f'The Computer has {hpc} HP')
            print(f'You have {hpp} health; health potions can be used which will increase your HP by 5 each\n')
            print('You have to enter the keyword \'inventory\' first to open your inventory.')
            print('Then you can enter either \'health potion\' or \'strength potion\'.\n')
            time = input('\nPress Enter to read further: ')
            print('\n#END/RESET\n')
            print('To reset and restart the game just enter the keyword \'reset\' or \'restart\'')
            print('To end the game enter the keyword \'end\' or \'end game\'\n')
            print('Have Fun!! ^_____^\n')

            break
        elif x.lower() == 'n' or x.lower() == 'no':
            print('Ok lets move on!\n')
            break
        else: # this code block is used to handle any mistakes that users make during entering values
            print('INVALID INPUT')
            print('Please enter only a y or n.\n')
