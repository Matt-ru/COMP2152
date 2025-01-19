# Sample Coding Questions 02 Week 02.
# Matthew Zygiel

try:

    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

    # Rolling
    weaponRoll = random.randint(1, 6)

    equippedWeapon = weapons[weaponRoll - 1]
    print(f"Weapon rolled: {equippedWeapon}")

    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend")
    elif weaponRoll <= 4:
        print("Your weapon is meh")
    else:
        print("Nice weapon, friend!")

    if equippedWeapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

except ValueError:
    print("Error: Invalid input detected. Pleasure ensure inputs are integers.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

