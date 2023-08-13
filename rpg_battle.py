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
        self.champion = False

    def skillRoll(self):
        return random.randint(0, self.skill)
    
    def updateHealth(self, amount):
        self.health -= int(amount)

    def updateWins(self):
        self.winstreak += 1
        self.champion = True

    def resetHealth(self):
        self.health = self.maxHealth


def generateName(exclude):
    # names list imported from names file
    return names[random.randint(0, len(names) -1)]

record_wins = 0
def updateRecord():
    global record_wins
    record_wins += 1

# create list of fighters using the Fighter class and passing in the generateName method to provide a name for each Fighter
fighters = [Fighter(generateName()), Fighter(generateName())]

# flag used in check to print fighter information when a new fight begins
new_fight = True

def battle():
    global new_fight

    if (new_fight):
      # display fighter stats at beginning of new fight
      print('Current Fighters:')
      print(fighters[0].name + ': Health(' + str(fighters[0].health) + ') Power(' + str(fighters[0].power) + ') Skill(' + str(fighters[0].skill) + ')' + (' *Champ' if fighters[0].champion else ''))
      print(fighters[1].name + ': Health(' + str(fighters[1].health) + ') Power(' + str(fighters[1].power) + ') Skill(' + str(fighters[1].skill) + ')' + (' *Champ' if fighters[1].champion else ''))
      print()
      input('Hit enter to begin the fight!')
      # reset new_fight flag so it doesn't spam fighter stats between each skill roll
      new_fight = False
    
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
        print(attacker.name + ' strikes ' + wounded.name + ' for ' + str(damage) + '!')
        # call updateHealth method on the wounded fighter itself because it is part of the Fighter class
        wounded.updateHealth(damage)
        if wounded.health <= 0:
            time.sleep(1.5)
            print('Fight Ended, ' + attacker.name + ' has emerged victorious and ' + wounded.name + ' has been slain.')
            attacker.updateWins()
            if attacker.winstreak > record_wins:
                print('A new record has been achieved! ' + attacker.name + ' has won ' + str(attacker.winstreak) + ' times in a row!')
                updateRecord()
            else:
                print(attacker.name + ' has ' + str(attacker.winstreak) + ' kills. The current record is ' + str(record_wins) + '.')
            attacker.resetHealth()
            fighters.remove(wounded)
            fighters.append(Fighter(generateName(attacker.name)))
            new_fight = True
            print()
        
while True:
    time.sleep(1.5)
    battle()
