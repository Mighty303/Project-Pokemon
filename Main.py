from User import*
from Computer import*
from Pokemon import*
from delay_print import delay_print

import random
import time
import sys


def game_loop():
    pokedex = [
        #TYPE: HP, AP, NAME
        GrassType(60, 40, 'Bulbasaur'),
        GrassType(40, 60, 'Bellsprout'),
        GrassType(50, 50, 'Oddish'),
        FireType(25, 70, 'Charmander'),
        FireType(30, 50, 'Ninetails'),
        FireType(40, 60, 'Ponyta'),
        WaterType(80, 20, 'Squirtle'),
        WaterType(70, 40, 'Psyduck'),
        WaterType(50, 50, 'Poliwag')]

    print('''
                                  ,'\                              
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
                                                                    ''')
    delay_print('Welcome to Pokemon.py\n\nEnter your username\n')
    player = User(input('USERNAME: '))
    delay_print(f'\n{player.name}, select 3 Pokemon from the pokedex\n')
    [print(f'{index}.{obj}\t{obj.hp}HP\t{obj.ap}AP\t{obj.set_type().upper()} TYPE') for index, obj in enumerate(pokedex, 1)]

    player_pokemons = []
    print(f'\nSelect 3 Pokemon by number')
    count = 1

    while count < 4:
        try:
            pokemon = int(input(f'Pokemon {count}: '))
            if pokemon > len(pokedex) or pokemon < 1:
                print('Invalid index')
            elif pokedex[pokemon-1] in player_pokemons:
                print('You cannot pick the same Pokemon!')
            else:
                player_pokemons.append(pokedex[pokemon-1])
                count += 1
        except ValueError:  print('Please enter a number')


    print("\nPLAYER'S POKEMON")
    [pokedex.remove(i) for i in player_pokemons] 
    #remove all the player's pokemon from the pokedex for the computer
    player.list_pokemon()
    player_pokemon = player.set_pokemon(player_pokemons)
    #returns the current pokemon
    
    print("\nCOMPUTER'S POKEMON")
    comp = Computer('COMPUTER') 
    computer_pokemon = comp.set_pokemon(pokedex)
    
    game_over = False
    while game_over != True:
        try:
            player_pokemon = player.isFainted()
            #Player's turn
            time.sleep(2)
            delay_print(f"\n{player.name.upper()}'S TURN\n\n")
            print(f'POKEMON:\n{player.current_pokemon.name}   \t{player.current_pokemon.hp}HP\t{player.current_pokemon.ap}AP')
            action = int(input(f'{player.name}, what would you like to do?\n1.Attack\n2.Heal\n3.Switch\n4.Stats\n'))

            if action == 1:
                print(f'{player.name.upper()} is attacking!')
                move = player.print_attacks()
                player.attack(move, computer_pokemon)
                
                
            elif action == 2:
                player.heal()

            elif action == 3:
                while True:
                    try:
                        print('\nWhich Pokemon would you like to switch to?')
                        player.list_pokemon()
                        index = int(input('POKEMON: '))
                        player_pokemon = player.switch(index)
                        break
                    except:
                        print('Please enter a valid number')
            
            elif action == 4:
                player.stats()
                continue

            else:
                print('Enter a valid number')
                continue

        except ValueError:
            print('Enter a valid number')
            continue
        except IndexError:
            print('Enter a valid')
            continue


        #Computer's turn
        computer_pokemon = comp.isFainted()
        time.sleep(2)
        print(f"\n{comp.name}'S TURN")
        comp.play_turn(player_pokemon)
        
    print('Gameover')

if __name__ == '__main__':
    game_loop()
