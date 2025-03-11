import random
from collections import Counter

def rollDice(min,max):
    return random.randint(min,max)

# Bronie do wyboru

weapons = {
    'sword':{'damage':10, 'chanceToHit':70},
    'axe':{'damage':15, 'chanceToHit':60},
    'bow':{'damage':20, 'chanceToHit':50},
    'poleaxe':{'damage':30, 'chanceToHit':35},
    'dagger':{'damage':8, 'chanceToHit':90},
           }
weaponsList = list(weapons.keys())

# Losowanie imienia i punktów życia dla Bossa
bossNamesPrefixes = ['Mighty ','Vile ','Enormous ','Swift ','Devilish ']
bossNamesSuffixes = [' the Destroyer',' the Warmonger',' the Cruel', ' the Allmighty',' the Marked One']
bossNames = ['Diablo','Baal','Mephisto','Duriel','Grzegorz']

bossName = random.choice(bossNamesPrefixes)+random.choice(bossNames)+random.choice(bossNamesSuffixes)
bossHitpoints = random.randint(100,300)
bossAlive = True

# ataki bossa
bossAttacks = {
    'Claws':{'damage':10,'chanceToHit':75,'chanceToBeUsed':50},
    'Tail':{'damage':15,'chanceToHit':60,'chanceToBeUsed':35},
    'Fireball':{'damage':30,'chanceToHit':50,'chanceToBeUsed':10},
    'Ultimate Attack':{'damage':50,'chanceToHit':30,'chanceToBeUsed':5}
                }
bossAttackList = list(bossAttacks.keys())

# Nadanie imienia przez gracza
print('Welcome in Boss Fight Simulator\n')
print('Today you will fight with: ',bossName,'!',sep='')
playerName = input('Please enter your name: ')
playerHitpoints = 250
print('\nWelcome',playerName,'You have',playerHitpoints,'hp')


# Wybór broni
print('\nChoose your weapon!')
for weapon in weaponsList:
    print(weapon,':',weapons[weapon]['damage'],'damage,',weapons[weapon]['chanceToHit'],'chance to hit.')

playerWeapon = input('\n')
while True:
    if playerWeapon not in weaponsList:
        print('You must enter weapon name! Try again')
        playerWeapon = input('\n')
        continue
    else:
        break

# Rozgrywka

gameRound=1
print(playerName,'you are equipped with',playerWeapon)
print('Your fight with',bossName,'begins!\n')
print(bossName,'have', bossHitpoints,'hit points!\n')
print('You have',playerHitpoints,'HP!\n')
print('FIGHT!\n')

while bossAlive:

    print('\nROUND ',gameRound,'!\n',sep='')

    # atak bossa
    print('\n',bossName, 'attack!')
    attack = random.choices(bossAttackList, [50, 35, 10, 5], k=100)
    attackChance = rollDice(0, 99)
    currentBossAttack = attack[attackChance]
    bossAttackHit = rollDice(0, 100)
    if bossAttackHit <= bossAttacks[currentBossAttack]['chanceToHit']:
        playerHitpoints = playerHitpoints - bossAttacks[currentBossAttack]['damage']
        print(bossName, 'hits you with', currentBossAttack, 'for', bossAttacks[currentBossAttack]['damage'],'damage')
        print('You have',playerHitpoints,'hp left')
    else:
        print(bossName,'attacked you with',currentBossAttack,'but missed!')

    # atak gracza
    if playerHitpoints>0:
            playerAttack = rollDice(0,100)
            print('\n',playerName,'attack!')
            if playerAttack<=weapons[playerWeapon]['chanceToHit']:
                bossHitpoints = bossHitpoints-weapons[playerWeapon]['damage']
                print('You hit a boss!',bossName,'with',weapons[playerWeapon]['damage'],'damage! It now have',bossHitpoints,'HP left!')
            else:
                print('You missed')

    # rezultat bitwy

    # player zabija bossa
    if bossHitpoints <= 0:
        print('\nCongratulations ',playerName,'! You killed ', bossName,'!',sep='')
        print('\nAfter hard battle you have', playerHitpoints, 'HP left!')
        bossAlive = False
        break

    # boss zabije gracza
    elif playerHitpoints <= 0:
        print('\nYou DIED!\n')
        print(bossName, 'have', bossHitpoints,'HP left!')
        break
    gameRound += 1
    input('\nPress Enter to begin next round')


input('\nPress Enter to end program')