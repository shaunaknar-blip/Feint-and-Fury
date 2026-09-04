import random
import attacks
import rules
import inventory

#Reset restarts the game by calling the main() function again.
def reset():
    main()

#Main Game Function
def main():
    title = "⋆༺𓆩⚔𓆪༻⋆ Feint & Fury ⋆༺𓆩⚔𓆪༻⋆"
    print(title.title(),'\n\n')

#this code block is used to choose a difficulty level.
    while True: 
        level = input('Choose a difficulty level between 1 - 3 '
                      '\n 1 - Easy\n 2 - Medium \n 3 - Hard\n Enter: ')
        if level == '1':
          inventory = ['Strength Potion','Strength Potion','Strength Potion',
                       'Strength Potion','Health Potion','Health Potion',
                       'Health Potion','Health Potion',]
          # in each difficulty level you get a set no. of health and strength potions.Higher the difficulty lesser the potions given.
          
          hpp = 70 # player HP
          hpc = 70 # Computer HP
          strength = 2 # Strength is an interger added to increase the damage caused by an attack to the computer
          
          print(f'You chose difficulty level {level}')
          break
        elif level == '2':
            inventory = ['Strength Potion','Strength Potion','Strength Potion',
                         'Health Potion','Health Potion','Health Potion',]
            hpp = 60
            hpc = 70
            strength = 0
            print(f'You chose difficulty level {level}')
            break
        elif level == '3':
            inventory = ['Strength Potion','Strength Potion',
                         'Health Potion','Health Potion',]
            hpp = 50
            hpc = 90
            strength = 0
            print(f'You chose difficulty level {level}')
            break
        else:
            print('INVALID INPUT\n INPUT A NO. BETWEEN 1 AND 3')
            continue
    #this will print the rules.
    rules.rules(hpp,hpc)
    print(f'Better be ready because I am!!')
    print('System: Your HP is ', hpp)
    print('System: Comp\'s HP is ', hpc)
    x = input('Press ENTER to start the game:\n')
    #this is the main game logic. This will run in a loop until either player's HP or computer's HP reaches 0 or less.
    while hpp > 0 or hpc > 0:
        a = input('System: What will be your move: ')
        roll = random.randint(1, 3) # this die roll determines the outcome of the attack.
        if (a.lower()).strip() == 'slash':
            hpc, hpp = attacks.slash(roll, hpc, hpp, strength)
            
        elif (a.lower()).strip() == 'thunderbolt' or (a.lower()).strip() == 'thunder bolt':
            hpc, hpp = attacks.thunder_bolt(roll, hpc, hpp, strength)
            
        elif (a.lower()).strip() == 'fireball' or (a.lower()).strip() == 'fire ball':
            hpc, hpp = attacks.fireball(roll, hpc, hpp, strength)
            
        elif (a.lower()).strip() == 'arrowshot' or (a.lower()).strip() == 'arrow shot':
            hpc, hpp = attacks.arrow_shot(roll, hpc, hpp , strength)

        #this invokes the inventory module.  
        elif (a.lower()).strip() == 'inventory':
            print(f'\nINVENTORY:\nHealth Potions - {inventory.count('Health Potion')}\nStrength Potion - {inventory.count('Strength Potion')}\n')
            # displays your inventory before using something
            
            strength, hpp, inventory = Inventory.invent(strength, hpp, inventory)
            # this assigns health, strenght, and inventory their values after the execution of the inent function
            
            print(f'\nINVENTORY:\nHealth Potions - {inventory.count('Health Potion')}\nStrength Potion - {inventory.count('Strength Potion')}\n')
            # displays your inventory after using something
            
        elif (a.lower()).strip() == 'end' or (a.lower()).strip() == 'endgame': # this line ends the game
            break
        
        elif (a.lower()).strip() == 'reset' or (a.lower()).strip() == 'restart':# this line restarts the game
            reset()
            return #Added here so that when resetting this running function is terminated.
        
        else: # this code block will prevent any incorrect input that might have been entered by the user.
              # it handles the error by displaying a INVALID INPUT message.
            print('INVALID INPUT !')
            print('Please check for mistakes and try again.')
        print()
        print('System: Your HP is', hpp)
        print('System: Your strength is', strength)
        print('System: Comp\'s HP is', hpc)# this ends one move from the user
        print()
        if hpp <= 0 or hpc <= 0:# the HPs are checked to find if anyone has been defeated
            break
    
    if hpp <= 0: # Computer won the game
        print('Comp: I won!')
        print(f'Comp: Better luck next time!')
        print('⌐■_■')
        print('ヾ⌐■_■ノ♪')
    elif hpc <= 0: # User won the game
        print(f'Comp: OK I let you win this time but I\'ll win next time')
        print('o一︿一+o')
    else: # the game was a draw
        print('System: It\'s a draw X_X')

if __name__ == "__main__":#this ensures that this module can't be invoked in any other code.
    print()
    print()
    main()
    
