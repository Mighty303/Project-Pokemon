import random
from Pokemon import*
from User import User
from delay_print import delay_print
import random
import sys

class Computer(User):
    def play_turn(self, enemy):
        computer_action = random.randint(1,6)
        if computer_action <= 4:
            delay_print(f'\n{self.name} is attacking!\n')
            self.computer_pokemon.set_attacks()
            attacks = self.computer_pokemon.attacks
            attack = random.choice(list(attacks))
            attack, enemy, isEffective = self.computer_pokemon.get_attack_power(attack, enemy)
            self.attack(attack, enemy, isEffective)
            
        elif computer_action == 5:
            Pokemon.heal(self.computer_pokemon)

        elif computer_action == 6:
            self.computer_pokemon = self.switch()
            

    def set_pokemon(self, list_pokemon):
        self.pokemon = []
        for i in range(3):
            pokemon = random.choice(list_pokemon)
            self.pokemon.append(pokemon)
            list_pokemon.remove(pokemon)
        [print(f'{i.name}    \t{i.hp}HP\t{i.ap}AP\t{i.set_type().upper()} TYPE') for i in self.pokemon]
        self.computer_pokemon = random.choice(self.pokemon)
        delay_print(f'\n{self.name} has chosen {self.computer_pokemon}\n')

        return self.computer_pokemon
        
    def switch(self, old_pokemon):
        while True:
            new_pokemon = random.choice(self.pokemon)
            if new_pokemon != old_pokemon:
                delay_print(f"{self.name} has chosen to switch to {new_pokemon}\n")
                return new_pokemon
    
    def attack(self, attack, enemy, isEffective):
        #attack = random.choice(self.computer_pokemon.attacks)
        List = self.computer_pokemon.attacks.get(attack, 'Error attack index not found') #List contains [PowerPoints, Accuracy]
        accuracy = random.randint(0,100)

        if List[1] != 100:            
            if List[1] > accuracy: #attack hits calculate the attack damage
                if self.computer_pokemon.ap > List[1]:
                    dmg = random.randint(List[1], self.computer_pokemon.ap) - 20
                    if isEffective:
                        dmg *= 1.5
                        delay_print("It's super effective!\n")
                    enemy.hp -= dmg
                    delay_print(f'{enemy.name} took {dmg} damage\n\n')
                
                else:
                    dmg = random.randint(self.computer_pokemon.ap, List[1]) - 20
                    if isEffective:
                        dmg *= 1.5
                        delay_print("It's super effective!\n")
                    enemy.hp -= dmg
                    delay_print(f'{enemy.name} took {dmg} damage\n\n')
                    
            else: #attack misses
                delay_print(f"{self.name}'s attack missed...\n")
        else:
            if self.computer_pokemon.ap > List[1]:
                dmg = random.randint(List[1], self.computer_pokemon.ap) - 20
                if isEffective:
                    dmg *= 1.5
                    delay_print("It's super effective!\n")
                enemy.hp -= dmg
                delay_print(f'{enemy.name} took {dmg} damage\n\n')
                
            else:
                dmg = random.randint(self.computer_pokemon.ap, List[1]) - 20
                if isEffective:
                    dmg *= 1.5
                    delay_print("It's super effective!\n")
                enemy.hp -= dmg
                delay_print(f'{enemy.name} took {dmg} damage\n\n')
        if enemy.hp > 0:
            delay_print(f'{enemy.name} now has {enemy.hp}HP\n')

    def is_end_game(self):
        if self.pokemon == []:
            delay_print(f'\n{self.name} has no more Pokemon left!\nGAME OVER\n')
            sys.exit(0)

    def print_attacks(self):
        return random.choice(list(self.attacks))

    def isFainted(self):
        if self.computer_pokemon.hp < 1:
            delay_print(f'{self.computer_pokemon} has fainted!\n')

            old_pokemon = self.computer_pokemon
            self.pokemon.remove(self.computer_pokemon)

            self.is_end_game()

            new_pokemon = self.switch(old_pokemon)
            self.computer_pokemon = new_pokemon
            return new_pokemon
        return self.computer_pokemon
