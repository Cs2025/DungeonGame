import os
import msvcrt


def choice4_option_1(self):
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

        choice4_1 = input("\nEnter your choice: ")

        if choice4_1 == "1":
            os.system("cls")
            self.type_text_slowly("You proceed through the left door...\n", 0.001)
            print("\nPress any key to continue...")
            msvcrt.getch()
            os.system("cls")
            break

        elif choice4_1 == "2":
            os.system("cls")
            self.type_text_slowly("You proceed through the center door...\n", 0.001)
            print("\nPress any key to continue...")
            msvcrt.getch()
            os.system("cls")
            break
        elif choice4_1 == "3":
            os.system("cls")
            self.type_text_slowly("You proceed through the right door...\n", 0.001)
            print("\nPress any key to continue...")
            msvcrt.getch()
            os.system("cls")
            break
        elif choice4_1.lower() == "i":
            os.system("cls")
            print("Inventory:")
            for item in self.character.get_inventory():
                print(f"- {item}")
            print("Coins: " + str(self.character.coins))
            print("\nPress any key to continue...")
            msvcrt.getch()
            os.system("cls")
        else:
            print("Invalid choice. Please try again.\n")