import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro():
    print_pause("Upon regaining consciousness, you " 
                "discover yourself in a confined space.")
    print_pause("The air is heavy with tension and the distant sound of gunfire.")
    print_pause("You remember you're a trained agent on a mission deep in enemy territory.")
    print_pause("Your objective: Retrieve the classified documents and escape alive.")

def main_choice():
    print_pause("What will you do next? Please enter number:")
    choice = input("1. Check your equipment\n"
                   "2. Move towards the enemy base\n"
                   "3. Wait for further instructions\n")
    if choice == '1':
        check_equipment()
    elif choice == '2':
        move_to_base()
    elif choice == '3':
        wait_for_instructions()
    else:
        main_choice()

def check_equipment():
    print_pause("You quickly check your equipment:")
    print_pause("- Pistol with silencer")
    print_pause("- Tactical vest")
    print_pause("- Lockpicking kit")
    print_pause("- First-aid supplies")
    print_pause("- Smoke grenades")
    main_choice()

def move_to_base():
    print_pause("You stealthily make your way towards the enemy base.")
    print_pause("The night conceals your movements.")
    print_pause("As you approach, you see guards patrolling the perimeter.")
    action = input("What will you do? Please enter number:\n"
                   "1. Take out the guards silently\n"
                   "2. Create a distraction\n"
                   "3. Try to sneak past them\n")
    if action == '1':
        take_out_guards()
    elif action == '2':
        create_distraction()
    elif action == '3':
        sneak_past_guards()
    else:
        move_to_base()

def wait_for_instructions():
    print_pause("You wait patiently, ears attuned to any sound.")
    print_pause("After what feels like an eternity, you receive a coded message.")
    print_pause("It's your contact with further instructions.")
    print_pause("'Proceed to the coordinates provided. Be cautious.'")
    move_to_base()

def take_out_guards():
    print_pause("You carefully approach the guards, aiming your silenced pistol.")
    for _ in range(2):
        guard_health = random.randint(20, 40)
        your_damage = random.randint(30, 50)
        print_pause(f"You take a shot, inflicting {your_damage} damage.")
        guard_health -= your_damage
        if guard_health > 0:
            print_pause(f"The guard retaliates, but misses you.")
            print_pause(f"The guard's health: {guard_health}")
        else:
            print_pause("You take out the guard silently.")
    move_to_base()

def create_distraction():
    print_pause("You grab a nearby rock and throw it towards the bushes.")
    print_pause("The guards, alerted, move towards the noise.")
    print_pause("This gives you a chance to slip by unnoticed.")
    move_to_base()

def sneak_past_guards():
    print_pause("You carefully time your movements with the guards' rotations.")
    print_pause("Using shadows and cover, you manage to slip past them.")
    print_pause("You're now inside the enemy base.")
    search_for_documents()

def search_for_documents():
    print_pause("You find yourself in a dimly lit room.")
    print_pause("There's a desk with a computer and a locked drawer.")
    action = input("What will you do? Please enter number:\n"
                   "1. Hack the computer\n"
                   "2. Try to pick the lock\n"
                   "3. Look around for clues\n")
    if action == '1':
        hack_computer()
    elif action == '2':
        pick_lock()
    elif action == '3':
        look_for_clues()
    else:
        search_for_documents()

def hack_computer():
    print_pause("You quickly access the computer and start hacking.")
    print_pause("After a tense few minutes, you gain access to the system.")
    print_pause("You find the classified documents and download them.")
    escape()

def pick_lock():
    print_pause("You take out your lockpicking kit and start working on the drawer.")
    print_pause("After a few nerve-wracking seconds, you hear a click.")
    print_pause("The drawer opens, revealing the classified documents.")
    escape()

def look_for_clues():
    print_pause("You search the room for any hidden clues or keys.")
    print_pause("You notice a photograph on the desk with a hidden safe behind it.")
    print_pause("You open the safe and find the classified documents.")
    escape()

def escape():
    print_pause("With the documents secured, you need to find a way out.")
    print_pause("As you make your way towards the exit, alarms blare.")
    print_pause("Guards are converging on your location.")
    action = input("What will you do? Please enter number:\n"
                   "1. Find an alternative exit\n"
                   "2. Fight your way out\n")
    if action == '1':
        find_alternative_exit()
    elif action == '2':
        fight_your_way_out()
    else:
        escape()

def find_alternative_exit():
    print_pause("You remember an alternative exit mentioned in the briefing.")
    print_pause("You make your way towards the secondary exit.")
    print_pause("With some quick thinking, you manage to evade the guards.")
    print_pause("You're almost out.")
    victory()

def fight_your_way_out():
    your_health = 100
    print_pause("You prepare for a fierce firefight with the guards.")
    for _ in range(3):
        guard_health = random.randint(20, 40)
        your_damage = random.randint(30, 50)
        print_pause(f"You engage the guards, inflicting {your_damage} damage.")
        guard_health -= your_damage
        if guard_health > 0:
            print_pause(f"The guard retaliates, but you dodge the shots.")
            print_pause(f"The guard's health: {guard_health}")
            print_pause(f"Your health: {your_health}")
            your_health -= random.randint(10, 30)
            if your_health <= 0:
                print_pause("You've been overwhelmed by the guards...")
                print_pause("MISSION FAILED.")
                break
        else:
            print_pause("You take out the guards one by one.")
    if your_health > 0:
        victory()

def victory():
    print_pause("You've successfully secured the classified documents!")
    print_pause("You make a swift exit, leaving the enemy base behind.")
    print_pause("Back at headquarters, you're hailed as a hero.")
    print_pause("Congratulations! You've completed your mission!")

def replay():
    while True:
        play_again = input("Would you like to play again? (yes/no) ").lower()
        if play_again == "yes":
            print_pause("Restarting the game...")
            game()  
        elif play_again == "no":
            print_pause("Thanks for playing! Goodbye!")
            break  
        else:
            print_pause("Invalid input. Please enter 'yes' or 'no'.")



def game():
    intro()
    main_choice()
    replay()

if __name__ == "__main__":
    game() 