import random

hero_health = random.randint(0, 100)
hero_health_max = hero_health
hero_skill = random.randint(0, 100)
hero_power = random.randint(0, 100)

villain_health = random.randint(0, 100)
villain_health_max = villain_health
villain_skill = random.randint(0, 100)
villain_power = random.randint(0, 100)


print("-Duel To The Death-\n")

while hero_health > 0 and villain_health > 0:
    print("Hero: " + str(hero_health) + "/" + str(hero_health_max) + " health. " + str(hero_skill) + " skill. " + str(hero_power) + " power.")
    print("Villain: "+ str(villain_health) + "/" + str(villain_health_max) + " health. " + str(villain_skill) + " skill. " + str(villain_power) + " power.\n")
    input()
    hero_skill_roll = random.randint(0, hero_skill)
    villain_skill_roll = random.randint(0, villain_skill)
    print("Skill roll: " + str(hero_skill_roll) + " (vs) " + str(villain_skill_roll) + "\n")
    if hero_skill_roll > villain_skill_roll:
        hero_damage = random.randint(0, hero_power)
        villain_health = villain_health - hero_damage
        print("Hero strikes Villain for " + str(hero_damage) + " damage!\n")
    if hero_skill_roll < villain_skill_roll:
        villain_damage = random.randint(0, villain_power)
        hero_health = hero_health - villain_damage
        print("Villain strikes Hero for " + str(villain_damage) + " damage!\n")
    if hero_skill_roll == villain_skill_roll:
        print("Blades collide in a shower of sparks!")
if hero_health < 1:
    print ("Hero has been slain! Villain is victorious!")
if villain_health < 1:
    print ("Villain has been slain! Hero is victorious!")