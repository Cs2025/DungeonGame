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
