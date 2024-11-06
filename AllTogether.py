import random

# Game data and variables
characters = ["Jedi", "Sith", "Bounty Hunter", "Smuggler"]
planets = ["Tatooine", "Hoth", "Endor", "Coruscant"]
enemies = {"Stormtrooper": 10, "Droid": 8, "Bounty Hunter": 12}

# Player stats
player = {
    "name": "",
    "character": "",
    "health": 100,
    "strength": 0,
    "credits": 50,
    "planet": "",
    "weapon": ""
}


# Function to handle errors and validate input
def get_choice(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        print("Invalid choice. Please try again.")


# Set up player character
def choose_character():
    print("Choose your character type:")
    for idx, char in enumerate(characters, 1):
        print(f"{idx}. {char}")

    try:
        choice = int(input("Enter the number of your character choice: ")) - 1
        if 0 <= choice < len(characters):
            player["character"] = characters[choice]
            player["strength"] = random.randint(10, 20)  # Set random strength
            print(f"You have chosen to be a {player['character']} with strength {player['strength']}.")
        else:
            print("Invalid number. Defaulting to Jedi.")
            player["character"] = "Jedi"
            player["strength"] = 15
    except ValueError:
        print("Error: Please enter a number.")
        player["character"] = "Jedi"
        player["strength"] = 15


# Set weapon based on character
def choose_weapon():
    if player["character"] in ["Jedi", "Sith"]:
        player["weapon"] = "Lightsaber"
    else:
        player["weapon"] = "Blaster"
    print(f"Your weapon is a {player['weapon']}.")


# Random event based on planet
def random_event():
    player["planet"] = random.choice(planets)
    print(f"You've landed on {player['planet']}.")
    encounter = random.choice(list(enemies.keys()))
    print(f"Uh-oh! A {encounter} is here!")
    fight(encounter)


# Fight sequence
def fight(enemy):
    enemy_health = enemies[enemy]
    while enemy_health > 0 and player["health"] > 0:
        action = get_choice("Do you want to (a)ttack or (r)un? ", ["a", "r"])
        if action == "a":
            # Calculate damage using modulo
            damage = (player["strength"] * random.randint(1, 5)) % 10
            print(f"You strike the {enemy} with your {player['weapon']} for {damage} damage!")
            enemy_health -= damage
            if enemy_health <= 0:
                print(f"You defeated the {enemy}!")
                player["credits"] += 10
                break
            else:
                print(f"The {enemy} has {enemy_health} health left.")
            # Enemy attack back
            enemy_damage = random.randint(1, 8)
            player["health"] -= enemy_damage
            print(f"The {enemy} attacks you back for {enemy_damage} damage! You have {player['health']} health left.")
        elif action == "r":
            print("You chose to run away!")
            break
    if player["health"] <= 0:
        print("You were defeated in battle... Game over.")
        exit()


# Main game loop
def main_game():
    print("Welcome to the Star Wars Adventure Game!")
    player["name"] = input("What is your name, traveler? ")
    choose_character()
    choose_weapon()

    # Game loop
    while player["health"] > 0:
        print("\nWhat would you like to do?")
        action = get_choice("(t)ravel to a new planet, (s)tatus check, or (q)uit: ", ["t", "s", "q"])

        if action == "t":
            random_event()
        elif action == "s":
            print(
                f"Name: {player['name']}, Character: {player['character']}, Health: {player['health']}, Credits: {player['credits']}, Weapon: {player['weapon']}")
        elif action == "q":
            print("Goodbye, and may the Force be with you!")
            break


# Run the game
if __name__ == "__main__":
    main_game()
