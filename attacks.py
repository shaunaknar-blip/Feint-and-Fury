# Basic Attacks
import random

def slash(roll, hpc, hpp, strength=0):
    print('System: You Chose Slash ▬▬ι═══════ﺤ ')
    print('Comp: Let\'s roll the dice')
    print('System: The roll is', roll)
    print()
    if roll == 1:
        hpc -= (10+strength)#damage done to computer
        print('Comp: Ohh You hit me !!!＞﹏＜')
        print(f'Comp: I lost {10+strength} HP')
        print()
    elif roll == 2:#no damage to anyone
        print('Comp: HUSH! missed it! Nearly got me ￣┰￣* ')
        print()
    else:
        print('Comp: Missed it Hah! Now I attack')
        print('Comp: Haiyya!! ╰（‵□′）╯')
        hpp, attackname, die = comp(hpp)#player gets damage
        print(f'System: Computer used {attackname} attack')
        print(f'System: Die is rolled. The Computer Rolled {die}.')
        print()
    
    return hpc, hpp

def fireball(roll, hpc, hpp, strength=0):
    print('System: You chose Fireball 🔥')
    print('Comp: Let\'s roll the dice')
    print('System: The roll is', roll)
    print()
    if roll == 1:
        hpc -= (15 +strength)#damage done to computer
        print('Comp: Ohh You hit me !!!＞﹏＜')
        print(f'Comp: I lost {15+strength} HP')
        print()
    elif roll == 2:#no damage to anyone
        print('Comp: HUSH! missed it! Nearly got me ￣┰￣* ')
        print()
    else:
        print('Comp: Missed it Hah! Now I attack')
        print('Comp: Haiyya!! ╰（‵□′）╯')
        hpp, attackname, die = comp(hpp)#player gets damage
        print(f'System: Computer used {attackname} attack')
        print(f'System: Die is rolled. The Computer Rolled {die}.')
        print()
    return hpc, hpp

def arrow_shot(roll, hpc, hpp, strength=0):
    print('System: You chose Arrow Shot 🏹')
    print('Comp: Let\'s roll the dice')
    print('System: The roll is', roll)
    print()
    if roll == 1:
        hpc -= (5 + strength)#damage done to computer
        print('Comp: Ohh You hit me !!!＞﹏＜')
        print(f'Comp: I lost {5+strength} HP')
        print()
    elif roll == 2:#no damage to anyone
        print('Comp: HUSH! missed it! Nearly got me ￣┰￣* ')
        print()
    else:
        print('Comp: Missed it Hah! Now I attack')
        print('Comp: Haiyya!! ╰（‵□′）╯')
        hpp, attackname, die = comp(hpp)#player gets damage
        print(f'System: Computer used {attackname} attack')
        print(f'System: Die is rolled. The Computer Rolled {die}.')
        print()
        
    return hpc, hpp

# Special Attacks
def thunder_bolt(roll, hpc, hpp, strength=0):
    print('System: You chose Thunderbolt ⚡︎')
    print('Comp: Let\'s roll the dice')
    print('System: The roll is', roll)
    print()
    if roll == 1:
        hpc -= (25+strength)#damage done to computer
        hpp -= 5#player gets damage
        print('Comp: Ohh You hit me !!!＞﹏＜')
        print(f'Comp: I lost {25+strength} HP')
        print()
    elif roll == 2:#no damage to anyone
        print('Comp: HUSH! missed it! Nearly got me ￣┰￣* ')
        print('System: You lost 5 HP')
        print()
        hpp -= 5#player gets damage
    else:
        print('Comp: Missed it Hah! Now I attack')
        print('Comp: Haiyya!! ╰（‵□′）╯')
        hpp, attackname, die = comp(hpp)#player gets damage
        print(f'System: Computer used {attackname} attack')
        print(f'System: Die is rolled. The Computer Rolled {die}.')
        print()
    
    return hpc, hpp

compattack = ['thunderbolt', 'arrowshot', 'fireball', 'slash']

def comp(hpp):#the computer attacks
    attackname = random.choice(compattack)#chooses computer's attack.
    die = random.randint(1,3)
    if attackname == 'thunderbolt':
        if die == 3:
            hpp -= 30#player gets damage
        elif die == 2:
            hpp -= 15#player gets damage
        else :
            hpp = hpp
    elif attackname == 'arrowshot':
        if die == 3:
            hpp -= 5#player gets damage
        elif die == 2:
            hpp -= 2#player gets damage
        else:
            hpp =hpp
    elif attackname == 'fireball':
        if die == 3:
            hpp -= 15#player gets damage
        elif die == 2:
            hpp-=7#player gets damage
        else:
            hpp =hpp
    else:
        if die == 3:
            hpp -= 10#player gets damage
        elif die == 2:
            hpp -= 5#player gets damage
        else:
            hpp = hpp
    return hpp, attackname , die
