# two opponents: health, power, skill
import random
import time
from names import names

class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = int(random.random() * 100)
        self.power = int(random.random() * 100)
        self.skill = int(random.random() * 100)
        self.winstreak = 0
        self.maxHealth = self.health

    def skillRoll(self):
        return random.randint(0, self.skill)
    
    def updateHealth(self, amount):
        self.health -= int(amount)

    def updateWins(self):
        self.winstreak += 1

    def resetHealth(self):
        self.health = self.maxHealth


def generateName():
    # names list imported from names file
    return names[random.randint(0, len(names) -1)]

record_wins = 0
def updateRecord():
    global record_wins
    record_wins += 1

fighters = [Fighter(generateName()), Fighter(generateName())]

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
        print(attacker.name + ' strikes ' + wounded.name + ' for ' + str(damage) + '!')
        # call updateHealth method on the wounded fighter itself because it is part of the Fighter class
        wounded.updateHealth(damage)
        if wounded.health <= 0:
            time.sleep(1)
            print('Fight Ended, ' + attacker.name + ' has emerged victorious and ' + wounded.name + ' has been slain.')
            attacker.updateWins()
            if attacker.winstreak > record_wins:
                print('A new record has been achieved! ' + attacker.name + ' has won ' + str(attacker.winstreak) + ' times in a row!')
                updateRecord()
            else:
                print(attacker.name + ' has ' + str(attacker.winstreak) + ' kills. The current record is ' + str(record_wins) + '.')
            attacker.resetHealth()
            fighters.remove(wounded)
            fighters.append(Fighter(generateName()))
        
while True:
    time.sleep(1)
    battle()
