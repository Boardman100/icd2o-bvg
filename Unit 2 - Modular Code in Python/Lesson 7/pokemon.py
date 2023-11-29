import random
import time
def choose_pokemon():
    player = input(f"What is your trainer's name: ")
    pokemon = input(f"Which pokemon do you choose: ")
    return pokemon, player
player_pokemon,player_name = choose_pokemon()

def game_intro(player_pokemon,player_name):
    time.sleep(2)
    print(f"You are {player_name}, one of the top trainers in the world! You recently won 8 gym badges with his partner {player_pokemon}.")
game_intro(player_pokemon,player_name)

def make_decision():
    time.sleep(3)
    encounter = input("You have encountered a wild charizard, would you like to battle it or attempt to catch it? Answer b/c: ")
    if encounter == "b":
        battle = True
    else:
        battle = False
    return battle
battle = make_decision()

def manage_your_health(health):
    if random.randint(1,2) == 1:
        damage = 500
        new_health = health-damage
        if new_health <= 0:
            print(f"Oh no, {player_pokemon} has no health left...")
            exit()
        print(f"Oh no! You took {damage} damage... You now have {new_health} health")
    else:
        damage = 800
        new_health = health-damage
        if new_health <= 0:
            print(f"Oh no, {player_pokemon} has no health left...")
            exit()
        print(f"The charizard is using his special move, flamethrower! You took {damage} damage... You now have {new_health} health")
    return new_health

def manage_op_health(health):
    if random.randint(1,2) == 1:
        damage = 500
        new_health = health-damage
        if new_health <= 0:
            print(f"Oh no, {player_pokemon} has no health left...")
            exit()
        print(f"Yes! The charizard took {damage} damage! He now has {new_health} health remaining!")
    else:
        damage = 800
        new_health = health-damage
        if new_health <= 0:
            print(f"Yes, charizard has no health left!")
            catch = input(f"Would you like to attempt to catch the charizard for extra xp? y/n: ")
            if catch == 'y':
                num = random.randint(1,10)
                if num >=3:
                    print("You caught the charizard!")
                else:
                    print("You missed the catch...")
            exit()
        print(f"{player_pokemon} is using his special move, power slap! The charizard took {damage} damage! He now has {new_health} health")
        #endgame()
    return new_health

def actions(battle,player_pokemon):
    op_health = random.randint(800,1400)
    your_health = random.randint(1200,2000)
    time.sleep(1)
    if battle == False:
        num = random.randint(1,10)
        if num >=3:
            print("You caught the charizard!")
        else:
            print("You missed the catch... the charizard is angry. Your only choice is to battle!")
            battle == True
    if battle == True:
        print(f"You have {your_health} health! Charizard has {op_health} health!")
        time.sleep(5)
        print(f"{player_pokemon} is only able to use his special move sometimes. Look out for when he is ready to use one!")
        time.sleep(5)
        your_health = manage_your_health(your_health)
        time.sleep(5)
        op_health = manage_op_health(op_health)
        time.sleep(5)
        your_health = manage_your_health(your_health)
        time.sleep(5)
        op_health = manage_op_health(op_health)
        time.sleep(5)
        your_health = manage_your_health(your_health)
        time.sleep(5)
        op_health = manage_op_health(op_health)
        time.sleep(5)
        your_health = manage_your_health(your_health)
        time.sleep(5)
        op_health = manage_op_health(op_health)
        time.sleep(5)
actions(battle,player_pokemon)