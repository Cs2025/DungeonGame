# DungeonGame created by Chris Shenton
# Project began on: 7/3/2023

import msvcrt
import os
import time
import sys
from character import Character
from ascii_art import torch_art


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
                self.type_text_slowly("You go down the left tunnel...\n", 0.001)
                print("\nPress any key to continue...")
                msvcrt.getch()  # Wait for a keypress
                os.system("cls")  # Clear the console screen
                break
            elif choice == "2":
                self.type_text_slowly("You go down the right tunnel...\n", 0.001)
                print("\nPress any key to continue...")
                msvcrt.getch()  # Wait for a keypress
                os.system("cls")  # Clear the console screen
                break
            elif choice == "3" and not self.character.has_torch:  # Check if the character does not have the torch
                self.character.has_torch = True  # Grab the torch
                self.type_text_slowly("You grab the torch.\n", 0.001)
                print(torch_art)
                print("\nPress any key to continue...")
                msvcrt.getch()  # Wait for a keypress
                os.system("cls")  # Clear the console screen
                continue
            else:
                print("Invalid choice. Please try again.\n")

        self.dungeon_start(choice)

    def dungeon_start(self, choice):
        if choice == "1":
            self.type_text_slowly("After walking down the left tunnel for several minutes\n"
                                  "You encounter a large monster with furry, flammable-looking\n"
                                  "fur.?\n", 0.001)
            print("\nPress any key to continue...")
            msvcrt.getch()  # Wait for a keypress
            os.system("cls")  # Clear the console screen

            while True:
                if not self.character.has_torch:  # Check if the character has the torch
                    print("What will you do now?\n1. Run Away\n2. Attack")
                    choice2 = input("Enter your choice: ")
                else:
                    print("What will you do now?\n1. Run Away\n2. Attack\n3. Burn the monster\n")
                    choice2 = input("Enter your choice: ")

                if choice2 == "1":
                    os.system("cls")  # Clear the console screen
                    self.type_text_slowly("You tried your best to run away, to no avail.\n"
                                          "You were eaten alive feet-first. The end.\n", 0.001)
                    print("\nPress any key to continue...")
                    msvcrt.getch()  # Wait for a keypress
                    sys.exit()

                if choice2 == "2":
                    os.system("cls")  # Clear the console screen
                    self.type_text_slowly("You tried your best to attack the monster, to no avail.\n"
                                          "You were picked up and swallowed whole. The end.\n", 0.001)
                    print("\nPress any key to continue...")
                    msvcrt.getch()  # Wait for a keypress
                    sys.exit()

        else:
            self.type_text_slowly("After walking down the right tunnel for several minutes\n"
                                  "You find a vast room, filled with nothing but a small chest.\n", 0.001)
            print("\nPress any key to continue...")
            msvcrt.getch()  # Wait for a keypress
            os.system("cls")  # Clear the console screen

    def main(self):
        self.ask_name()
        self.enter_dungeon()


if __name__ == '__main__':
    game = Main()
    game.main()