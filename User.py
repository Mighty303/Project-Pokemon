from Pokemon import*

import random
import time
import sys

from delay_print import delay_print

class User(object):
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.current_pokemon = None
        self.attacking_pokemon = None

    def set_pokemon(self, set_of_pokemon):
        self.pokemon = set_of_pokemon

        while True:
            try:
                self.list_pokemon()
                index = int(input('\nSelect a Pokemon to battle with: '))
                self.current_pokemon = self.pokemon[index-1]
                delay_print(f'You have chosen {self.current_pokemon}\n')
                if index > len(self.pokemon) or index < 1:
                    print('Invalid Pokemon')
                    continue
                return self.current_pokemon
                #returns the index of the selected pokemon
                
            except:
                print('Enter a valid number')

    def list_pokemon(self):
        [print(f'{i}.{obj.name}\t{obj.hp}HP\t{obj.ap}AP\t{obj.set_type().upper()} TYPE') for i, obj in enumerate(self.pokemon, 1) if obj.hp > 1]
        #numbers off the pokemon in hand

    def stats(self):
        print(f"\n{self.name.upper()}'S POKEMON:")
        [delay_print(f'{i.name}    \t{i.hp}HP\t{i.ap}AP\t{i.set_type().upper()}\n') for i in self.pokemon]
        #lists stats of all pokemon in hand

    def switch(self, pokemon_number):
        delay_print(f'You have chosen {self.pokemon[pokemon_number-1]}\n')
        self.current_pokemon = self.pokemon[pokemon_number-1]
        return self.pokemon[pokemon_number-1]
        #returns the index of the current pokemon
        
    def heal(self):
        Pokemon.heal(self.current_pokemon)

    def is_end_game(self):
        if not self.pokemon:
            delay_print(f'\n{self.name} has no more Pokemon left!\nGAME OVER\n')
            sys.exit(0)
        

    def print_attacks(self):
        self.current_pokemon.set_attacks() #calls the Type's attack set which calls the pokemon class LOL
        return self.current_pokemon.print_attacks()
        #return to gameloop as move

    def attack(self, move, enemy):
        attack, enemy, isEffective = self.current_pokemon.get_attack_power(move, enemy)
        Pokemon.attack(self.current_pokemon, attack, enemy, isEffective)
        # Pokemon.get_attack_power(self.current_pokemon, move, enemy)

    def isFainted(self):
        
        if self.current_pokemon.hp < 1:
            delay_print(f'{self.current_pokemon} has fainted!')
            self.pokemon.remove(self.current_pokemon)
            self.is_end_game()
            

            while True:
                try:
                    print('\nWhich Pokemon would you like to switch to?')
                    self.list_pokemon()
                    index = int(input('POKEMON: '))
                    if index == 0:
                        print('Enter a valid number')
                        continue
                    self.current_pokemon = self.switch(index)
                    break
                except:
                    print('Enter a valid number')
            self.current_pokemon = self.pokemon[index-1]
            return self.current_pokemon
        return self.current_pokemon

    def __str__(self):
        return self.name
