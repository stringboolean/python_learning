# two opponents: health, power, skill
import random
import time


account = {
    'balance': 100,
    'wins': 0,
    'losses': 0,
    'times_played': 0,
}    

class Fighter:
    def __init__(self):
        self.health = int(random.random() * 100)
        self.power = int(random.random() * 100)
        self.skill = int(random.random() * 100)

    def skillRoll(self):
        return random.randint(0, self.skill)
    
    def updateHealth(self, amount):
        self.health -= int(amount)

    
print(':::: FIGHTERS ::::')
print('Select a fighter to place bet!')

# create list of fighters which means they will have index 0 and 1
fighters = [Fighter(), Fighter()]
print('1: ' + str(fighters[0].__dict__)) # fighter referenced by index 0 in fighters
print('2: ' + str(fighters[1].__dict__))# fighter referenced by index 1 in fighters

selected_fighter = input('Which fighter would you like to bet on? [1 or 2]: ')
while selected_fighter not in ['1', '2']:
    print('You must select 1 or 2!')
    selected_fighter = input('Which fighter would you like to bet on? [1 or 2]: ')

print('You have selected fighter ' + selected_fighter + '.')
bet = input('How much would you like to bet of your ' + str(account['balance']) + '? [$5 minimum]: $')
while not bet.isnumeric() or int(bet) < 5:
    print('You must bet a minimum of $5!')
    bet = input('How much would you like to bet of your ' + str(account['balance']) + '? [$5 minimum]: $')

account['balance'] -= int(bet)
print('You bet of $' + bet + ' has been deducted. Your balance is now $' + str(account['balance']) + '.')

def battle():
    # create skills list that will match the index of the fighters list created above
    skills = []
    for f in fighters:
        # push the skill roll of each fighter into the list using the built in skillRoll method that comes from the Fighter class
        skills.append(f.skillRoll())
    # decide who hits using indexes that correlate with each fighter between both lists (fighters and skills)
    if skills[0] == skills[1]:
        print('The fighters weapons clash together with a loud clang!')
    else:
        attacker = fighters[0] if skills[0] > skills[1] else fighters[1]
        wounded = fighters[1] if skills[0] > skills[1] else fighters[0]
        damage = random.randint(0, attacker.power)
        # here we add 1 to the index of each fighter simply for the sake of displaying them to the user as we did on the betting menu
        print('Fighter ' + str((fighters.index(attacker) + 1)) + ' strikes Fighter ' + str((fighters.index(wounded) + 1)) + ' for ' + str(damage) + '!')
        # call updateHealth method on the wounded fighter itself because it is part of the Fighter class
        wounded.updateHealth(damage)
        if wounded.health <= 0:
            time.sleep(1)
            print('Game Ended, someone died')
            if fighters[int(selected_fighter) - 1].health > 0:
                account['balance'] += int(bet) * 2
                print('You won: Your balance is now ' + str(account['balance']) + '.')

            else:
                print('You lost: Your balance remains at ' + str(account['balance']) + '.')
            exit()
        
while True:
    time.sleep(1)
    battle()

