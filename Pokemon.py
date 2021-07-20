from User import*
from Pokemon import*
from delay_print import delay_print
import random

class Pokemon(object):
    def __init__(self, hp, ap, name):
        self.hp = hp
        self.ap = ap
        self.name = name
        self.attacks = None

    def set_type(self):
        return None

    def set_attacks(self):
        self.attacks = {}

    def print_attacks(self):
        print(f"\n{self.name}'s attacks:")
        [print(f'{num}.{attack}') for num, attack in enumerate(self.attacks, 1)]
        while True:
            try:
                move = int(input('\nPick a move: ')) #add try statment later
                if move > len(self.attacks) or move < 1:
                    print('Enter a valid number')
                    continue
                break
            except:
                print('Enter a valid number')
                continue
        delay_print(f'{self.name} is attacking!\n')
        delay_print(f"{self.name} used {list(self.attacks)[move-1]}\n")
        return list(self.attacks)[move-1]

    def add_attacks(self, attack_dictionary):
        self.attacks = attack_dictionary
            

    def attack(self, attack, enemy, isEffective):
        List = self.attacks.get(attack, 'Error attack index not found') #List contains [PowerPoints, Accuracy]
        accuracy = random.randint(0,100)
        if List[1] != 100:
            if List[1] > accuracy: #attack hits calculate the attack damage
                if self.ap > List[1]:
                    dmg = random.randint(List[1], self.ap) - 20
                    if isEffective:
                        dmg *= 1.5
                        delay_print("It's super effective!\n")
                    enemy.hp -= dmg
                    delay_print(f'{enemy.name} took {dmg} damage\n')
                
                else:
                    dmg = random.randint(self.ap, List[1]) - 20
                    enemy.hp -= dmg
                    delay_print(f'{enemy.name} took {dmg} damage\n')
                    
            else: #attack misses
                delay_print(f"{self.name}'s attack missed...\n") 
        else:
            if self.ap > List[1]:
                    dmg = random.randint(List[1], self.ap) - 20
                    if isEffective:
                        dmg *= 1.5
                        delay_print("It's super effective!\n")
                    enemy.hp -= dmg
                    delay_print(f'{enemy.name} took {dmg} damage\n')
                
            else:
                dmg = random.randint(self.ap, List[1]) - 20
                if isEffective:
                        dmg *= 1.5
                        delay_print("It's super effective!\n")
                enemy.hp -= dmg
                delay_print(f'{enemy.name} took {dmg} damage\n')

        if enemy.hp > 0:
            delay_print(f'{enemy.name} now has {enemy.hp}HP\n')

    def heal(self):
        self.hp += 20
        delay_print(f'\n{self.name} has healed for 20HP\n{self.name} is now at {self.hp} HP\n')

    def __str__(self):
        return self.name

class GrassType(Pokemon):
    GrassAttacks = {
            'Leaf Storm': [130, 90],
            'Mega Drain': [50, 100],
            'Razor Leaf': [55, 95]
        }
    #1.5x stronger against Water
    def set_type(self):
        return 'Grass'

    def set_attacks(self):
        self.add_attacks(GrassType.GrassAttacks)

    def get_attack_power(self, attack, enemy):
        if enemy.set_type() == 'Water':
            isEffective = True
            return attack, enemy, isEffective 
        isEffective = False
        return attack, enemy, isEffective
        
    
class FireType(Pokemon):
    FireAttacks = {
            'Ember':       [60, 100],
            'Fire Punch' : [85, 80],
            'Flame Wheel': [70, 90]
        }
    #1.5x stronger against Grass
    def set_type(self):
        return 'Fire'

    def set_attacks(self):
        self.add_attacks(FireType.FireAttacks)

    def get_attack_power(self, attack, enemy):
        if enemy.set_type() == 'Grass':
            isEffective = True
            return attack, enemy, isEffective    
        isEffective = False
        return attack, enemy, isEffective

class WaterType(Pokemon):
    WaterAttacks = {
            'Bubble':     [40, 100],
            'Hydro Pump': [185, 30],
            'Surf':       [70, 90]
        }
    #1.5x stronger against Fire
    def set_type(self):
        return 'Water'

    def set_attacks(self):
        self.add_attacks(WaterType.WaterAttacks)

    def get_attack_power(self, attack, enemy):
        if enemy.set_type() == 'Fire':
            isEffective = True
            return attack, enemy, isEffective    
        isEffective = False
        return attack, enemy, isEffective
