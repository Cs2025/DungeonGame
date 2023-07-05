# DungeonGame created by Chris Shenton
# Project began on: 7/3/2023

import msvcrt
import os
import time
import sys

import floor1
from character import Character
from ascii_art import torch_art, coin_art


class Main:
    def __init__(self):
        name = input("Please enter your name: ")
        self.character = Character(name)

    @staticmethod
    def type_text_slowly(text, delay):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)

    def ask_name(self):
        os.system("cls")
        print(f"Hello, {self.character.name}!")
        print("\nPress any key to continue...")
        msvcrt.getch()
        os.system("cls")
        intro_text = "In this game, you will enter a dungeon, collect loot, fight monsters, and \nattempt to make it " \
                     "through the tunnels and out the exit."
        self.type_text_slowly(intro_text + "\n", 0.001)

        print("\nPress any key to enter the dungeon...")
        msvcrt.getch()
        os.system("cls")

    def enter_dungeon(self):
        text1 = "You enter a room with two tunnels, as well as a torch on the wall.\nWhat will you choose to do?"
        self.type_text_slowly(text1 + "\n", 0.001)

        while True:
            print()

            if not self.character.has_torch:  # Check if the character has the torch
                print("1. Go left")
                print("2. Go right")
                print("3. Grab the torch\n")
                choice = input("Enter your choice: ")
            else:
                print("What will you do now?")
                print("1. Go left")
                print("2. Go right\n")

                choice = input("Enter your choice: ")

            if choice == "1":
                os.system("cls")
                self.type_text_slowly("You go down the left tunnel...\n", 0.001)
                print("\nPress any key to continue...")
                msvcrt.getch()  # Wait for a keypress
                os.system("cls")  # Clear the console screen
                break
            elif choice == "2":
                os.system("cls")
                self.type_text_slowly("You go down the right tunnel...\n", 0.001)
                print("\nPress any key to continue...")
                msvcrt.getch()  # Wait for a keypress
                os.system("cls")  # Clear the console screen
                break
            elif choice == "3" and not self.character.has_torch:
                os.system("cls")
                self.character.has_torch = True  # Grab the torch
                self.character.add_item("Torch")  # Add the torch to the inventory
                self.type_text_slowly("You grab the torch.\n", 0.001)
                print(torch_art)  # Print out torch ASCII art
                print("\nPress any key to continue...")
                msvcrt.getch()  # Wait for a keypress
                os.system("cls")  # Clear the console screen
                continue
            else:
                os.system("cls")
                print("Invalid choice. Please try again.\n")

        self.dungeon_start(choice)

    def dungeon_start(self, choice):
        if choice == "1":
            os.system("cls")
            self.type_text_slowly("After walking down the left tunnel for several minutes\n"
                                  "You encounter a large monster with furry, \x1b[1mflammable-looking\x1b[0m\n"
                                  "fur.\n", 0.001)
            print("\nPress any key to continue...")
            msvcrt.getch()  # Wait for a keypress
            os.system("cls")  # Clear the console screen

            while True:
                if not self.character.has_torch:  # Check if the character has the torch
                    print("What will you do now?\n1. Run Away\n2. Attack")
                else:
                    print("What will you do now?\n1. Run Away\n2. Attack\n\x1b[32m3. Burn the monster\x1b[0m\n")

                choice = input("Enter your choice: ")

                if choice == "1":
                    os.system("cls")  # Clear the console screen
                    self.type_text_slowly("You tried your best to run away, to no avail.\n"
                                          "You were eaten alive feet-first. The end.\n", 0.001)
                    print("\nPress any key to continue...")
                    msvcrt.getch()  # Wait for a keypress
                    sys.exit()

                elif choice == "2":
                    os.system("cls")  # Clear the console screen
                    self.type_text_slowly("You tried your best to attack the monster, to no avail.\n"
                                          "You were picked up and swallowed whole. The end.\n", 0.001)
                    print("\nPress any key to continue...")
                    msvcrt.getch()  # Wait for a keypress
                    sys.exit()
                elif choice == "3" and self.character.has_torch:  # Check if the character has the torch
                    os.system("cls")  # Clear the console screen
                    self.character.has_torch = False  # Use up the torch on the monster
                    self.character.remove_item("Torch")  # Remove torch from user's inventory
                    self.type_text_slowly("You attack the monster with your torch. The monster\n"
                                          "goes up in flames, however so does your torch.\n\n"
                                          "Torch has been removed from your inventory.", 0.001)
                else:
                    os.system("cls")
                    print("Invalid choice. Please try again.\n")

                    print("\nPress any key to continue...")
                    msvcrt.getch()  # Wait for a keypress
                    os.system("cls")  # Clear the console screen
                    break
        else:
            self.type_text_slowly("After walking down the right tunnel for several minutes\n"
                                  "You find a vast room, filled with nothing but a small chest.\n", 0.001)
            print("\nPress any key to continue...")
            msvcrt.getch()  # Wait for a keypress
            os.system("cls")  # Clear the console screen

            while True:
                if self.character.coins == 0:  # Check if the character has no coins
                    print("What will you do now?\n")
                    print("1. Continue")
                    print("2. Open the chest")

                else:
                    print("What will you do now?")
                    print("1. Continue")

                choice = input("\nEnter your choice: ")

                if choice == "1":
                    os.system("cls")
                    self.type_text_slowly("You continue through the dungeon...\n", 0.001)
                    print("\nPress any key to continue...")
                    msvcrt.getch()  # Wait for a keypress
                    os.system("cls")  # Clear the console screen
                    break

                elif choice == "2":
                    os.system("cls")
                    self.character.add_coins(10)  # Grab ten coins
                    self.type_text_slowly("You open the chest and find ten golden coins.\n", 0.001)
                    print(coin_art + '  x10')  # Print out coin ASCII art
                    print("\nPress any key to continue...")
                    msvcrt.getch()  # Wait for a keypress
                    os.system("cls")  # Clear the console screen
                    continue
                else:
                    os.system("cls")
                    print("Invalid choice. Please try again.\n")

    def dungeon_first_floor(self):
        print("You have reached the first floor of the dungeon!\n")
        print("New feature unlocked: Show inventory (press i)\n")

        while True:
            print("\nPress any key to continue... \nPress I for inventory")

            key = msvcrt.getch().decode().lower()  # Wait for a keypress and convert to lowercase

            if key == "i":
                os.system("cls")
                print("Inventory:")
                for item in self.character.get_inventory():
                    print(f"- {item}")
                print("Coins: " + str(self.character.coins))
                print("\nPress any key to continue...")
                msvcrt.getch()
                os.system("cls")
            else:
                break
        os.system("cls")
        self.type_text_slowly("Once you reach the first floor entrance, you notice\n"
                              "a shady merchant in the center of the room. Behind him are\n"
                              "three doors, each marked with a '?' sign.\n", 0.001)
        print("\nPress any key to continue...")
        msvcrt.getch()  # Wait for a keypress
        os.system("cls")  # Clear the console screen

        while True:
            print("What will you do now?\n")
            print("1. Go through the left door")
            print("2. Go through the center door")
            print("3. Go through the right door")
            print("4. Talk to the merchant\n")
            print("I. Show inventory")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                os.system("cls")
                self.type_text_slowly("You proceed through the left door...\n", 0.001)
                print("\nPress any key to continue...")
                msvcrt.getch()  # Wait for a keypress
                os.system("cls")  # Clear the console screen
                floor1.choice_option_1(self)  # Call the choice_option_1 method for the left door
                os.system("cls")
                break
            elif choice == "2":
                os.system("cls")
                self.type_text_slowly("You proceed towards the center door...\n", 0.001)
                print("\nPress any key to continue...")
                msvcrt.getch()
                os.system("cls")
                floor1.choice_option_2(self)  # Call the choice_option_2 method for the center door
                os.system("cls")
            elif choice == "3":
                os.system("cls")
                self.type_text_slowly("You proceed through the right door...\n", 0.001)
                print("\nPress any key to continue...")
                msvcrt.getch()  # Wait for a keypress
                os.system("cls")  # Clear the console screen
                break
            elif choice == "4":
                os.system("cls")
                floor1.choice_option_4(self)  # Call the choice_option_4 method for the merchant's shop
                os.system("cls")  # Clear the console screen
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

    def main(self):
        self.ask_name()
        self.enter_dungeon()
        self.dungeon_first_floor()


if __name__ == '__main__':
    game = Main()
    game.main()
