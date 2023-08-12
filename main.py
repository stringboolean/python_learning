# two opponents: health, power, skill
import random


account = {
    'balance': 100,
    'wins': 0,
    'losses': 0,
    'times_played': 0,
}

def quitgame():
    print('Game Ended, someone died')
    exit()

class Fighter:
    def __init__(self):
        self.health = int(random.random() * 100)
        self.power = int(random.random() * 100)
        self.skill = int(random.random() * 100)

    def skillRoll(self):
        return random.randint(0, self.skill)
    
    def updateHealth(self, amount):
        self.health -= int(amount)
        if self.health <= 0:
            quitgame()

    
print(':::: FIGHTERS ::::')
print('Select a fighter to place bet!')

# create list of fighters which means they will have index 0 and 1
fighters = [Fighter(), Fighter()]
print('1: ' + str(fighters[0].__dict__)) # fighter referenced by index 0 in fighters
print('2: ' + str(fighters[1].__dict__))# fighter referenced by index 1 in fighters

seleccted_fighter = input('Which fighter would you like to bet on? [1 or 2]: ')

balance = 100

print('You have selected fighter ' + seleccted_fighter + '.')
bet = input('How much would you like to bet of your ' + str(balance) + '? ')

balance -= int(bet)
print('Your balance is now ' + str(balance) + '.')

def updateAccount():
    if fighters[int(seleccted_fighter) - 1].health > 0:
        balance += int(bet)
    else:
        balance -= int(bet)
        print('Your balance is now ' + str(balance) + '.')

def battle():
    # create skills list that will match the index of the fighters list created above
    skills = []
    for f in fighters:
        # push the skill roll of each fighter into the list using the built in skillRoll method that comes from the Fighter class
        skills.append(f.skillRoll())
    if skills[0] > skills[1]:
        # decide who hits using indexes that correlate with each fighter between both lists (fighters and skills)
        attacker = fighters[0] if skills[0] > skills[1] else fighters[1]
        wounded = fighters[1] if skills[0] > skills[1] else fighters[0]
        damage = random.randint(0, attacker.power)
        # here we add 1 to the index of each fighter simply for the sake of displaying them to the user as we did on the betting menu
        print('Fighter ' + str((fighters.index(attacker) + 1)) + ' strikes ' + str((fighters.index(wounded) + 1)) + ' for ' + str(damage) + '!')
        # check to see if the game is over and update the balance if so before the game ends
        if wounded.health <= 0: updateAccount()
        # call updateHealth method on the wounded fighter itself because it is part of the Fighter class
        wounded.updateHealth(damage)

while True:
    battle()

