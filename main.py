# adventure game
# choices regarding survival
# day timer, fatigue?, sleeping replenishes fatigue

# tile_names = [
#     '1'
# ]

# class MapTile:
#     def __init__(self, name, loot, trigger) -> None:
#         self.name = name
#         self.loot = loot
#         self.trigger = trigger

# two opponents: health, power, skill
import random

balance = 100
def quitgame():
    print('Game Ended, someone died')
    exit()

class Fighter:
    def __init__(self):
        self.health = int(random.random() * 100)
        self.power = int(random.random() * 100)
        self.skill = int(random.random() * 100)
    
    def updateHealth(self, amount):
        self.health -= int(amount)
        if self.health <= 0:
            quitgame()

    
print(':::: FIGHTERS ::::')
print('Select a fighter to place bet!')
fighters = [Fighter(), Fighter()]
# for f in fighters: print(f.__dict__)
print('1: ' + str(fighters[0].__dict__))
print('2: ' + str(fighters[1].__dict__))

seleccted_fighter = input('Which fighter would you like to bet on? [1 or 2]: ')

print('You have selected fighter ' + seleccted_fighter + '.')
bet = input('How much would you like to bet of your ' + str(balance) + '? ')

balance = balance - int(bet)
print('Your balance is now ' + str(balance) + '.')

def battle():
    
    pass

while True:
    battle()

