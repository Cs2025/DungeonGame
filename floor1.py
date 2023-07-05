import os
import msvcrt
import sys
from ascii_art import diamond_art, coin_art


def choice_option_1(self):
    self.type_text_slowly("After entering the door on the left, you encounter\n"
                          "a grassy enclosure with a large hole in the center.\n"
                          "On the left, there is a small cave, but the entrance\n"
                          "is blocked by roots. Straight ahead, there is another\n"
                          "cave entrance that is unobstructed.", 0.001)

    print("\nPress any key to continue...")
    msvcrt.getch()
    os.system("cls")

    while True:
        print("What will you do now?\n")
        if self.character.has_torch:
            print("1. Jump over the hole")
            print("2. Maneuver past the hole")
            print("3. \x1b[32mAttempt to burn roots\x1b[0m")
            print("I. Show inventory")
        else:
            print("1. Jump over the hole")
            print("2. Maneuver past the hole")
            print("I. Show inventory")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            os.system("cls")
            self.type_text_slowly("You attempt to jump over the hole."
                                  "You did not make it. The end.", 0.001)
            print("\nPress any key to continue...")
            sys.exit()

        elif choice == "2":
            os.system("cls")
            self.type_text_slowly("You make it past the hole, into the cave entrance.", 0.001)
            print("\nPress any key to continue...")
            msvcrt.getch()
            os.system("cls")
            break
        elif choice == "3" and self.character.has_torch:
            os.system("cls")
            self.type_text_slowly("You head left towards the blocked cave entrance.\n", 0.001)
            print("\nPress any key to continue...")
            msvcrt.getch()
            os.system("cls")

            self.type_text_slowly("You burn down the roots and head into the cave.\n"
                                  "Inside, you find a pedestal with a large, shiny jewel\n"
                                  "on a pedestal. Your torch is used up in the process.\n\n"
                                  "Torch removed from inventory.", 0.001)
            self.character.has_torch = False  # Remove torch from inventory
            print("\nPress any key to continue...")
            msvcrt.getch()
            os.system("cls")

            while True:
                print("What will you do now?\n")
                print("1. Turn back")
                if not self.character.has_diamond:
                    print("2. Take the diamond")
                choice = input("Enter your choice: ")
                if choice == "1":
                    os.system("cls")
                    self.type_text_slowly("You turn back around and exit the cave.", 0.001)
                    print("\nPress any key to continue...")
                    msvcrt.getch()
                    os.system("cls")
                    break
                elif choice == "2" and not self.character.has_diamond:
                    os.system("cls")
                    self.type_text_slowly("You grab the diamond.", 0.001)
                    self.character.has_diamond = True
                    print(diamond_art)
                    print("\nPress any key to continue...")
                    msvcrt.getch()
                    os.system("cls")
                elif choice.lower() == "i":
                    os.system("cls")
                    print("Inventory:")
                    for item in self.character.get_inventory():
                        print(f"- {item}")
                    if self.character.has_diamond:
                        print("- Diamond")
                    print("Coins: " + str(self.character.coins))
                    print("\nPress any key to continue...")
                    msvcrt.getch()
                    os.system("cls")
                else:
                    os.system("cls")
                    print("Invalid choice. Please try again.\n")
            continue  # Go back to the beginning of the loop
        elif choice.lower() == "i":
            os.system("cls")
            print("Inventory:")
            for item in self.character.get_inventory():
                print(f"- {item}")
            print("Coins: " + str(self.character.coins))
            print("\nPress any key to continue...")
            msvcrt.getch()
            os.system("cls")
        else:
            os.system("cls")
            print("Invalid choice. Please try again.\n")


def choice_option_2(self):
    self.type_text_slowly("You try to open the second door, however you quickly\n"
                          "realize that the 'door' is actually just a picture of one.\n"
                          "You move the picture aside and find a safe on the wall.", 0.001)

    print("\nPress any key to continue...")
    msvcrt.getch()
    os.system("cls")

    while True:
        safe_opened = False
        print("What will you do now?\n")
        if safe_opened:
            print("1. Turn around")
            print("I. Show inventory")
        else:
            print("1. Turn around")
            print("2. Try unlocking the safe")
            print("I. Show inventory")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            os.system("cls")
            self.type_text_slowly("You turn back around.\n", 0.001)
            os.system("cls")
            break
        if choice == "2" and not safe_opened:
            os.system("cls")
            self.type_text_slowly("You try opening the safe, and to your surprise\n"
                                  "the safe is already unlocked! Inside you find 5 golden coins.", 0.001)
            self.character.add_coins(5)  # Grab five coins
            safe_opened = True
            print(coin_art + '  x5')  # Print out coin ASCII art

            print("\nPress any key to continue...")
            msvcrt.getch()  # Wait for a keypress
            os.system("cls")  # Clear the console screen
            continue

        elif choice.lower() == "i":
            os.system("cls")
            print("Inventory:")
            for item in self.character.get_inventory():
                print(f"- {item}")
            print("Coins: " + str(self.character.coins))
            print("\nPress any key to continue...")
            msvcrt.getch()
            os.system("cls")
        else:
            os.system("cls")
            print("Invalid choice. Please try again.\n")


def choice_option_3(self):
    pass


def choice_option_4(self):
    pass
