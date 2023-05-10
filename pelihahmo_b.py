"""
Game character B

Often in video games there are multiple characters who have some kind of
interaction with each other. Often this is violent, but not always. The
caracters in a game can, for example, pass items between each other or have a
fight. In the program the character has hitpoints and items and the weapons
have an amount that causes damage to other character's hitpoints. If the
hitpoints go under zero, the character is destroyed.

Writer of the program: EILeh

"""

class Character:
    """
    This class defines what a character is int he game and what
    he or she can do.
    """

    def __init__(self, character_name, hitpoints,
                 starting_items = None):

        self.__name = character_name

        # Initializes an empty dictionary if the character doesn't have any
        # items.
        if starting_items is None:
            starting_items = {}

        self.__item_dict = starting_items

        self.__hitpoints = hitpoints

    def printout(self):

        # If character doesn't have items, only character's name is printed.
        if not self.__item_dict:
            print("Name:", self.__name)
            print("  --nothing--")

        else:
            print("Name:", self.__name)
            print("Hitpoints:", self.__hitpoints)

            # Goes through the character's item that are in a dictionary and
            # prints the item and the amount of items.
            for item in sorted(self.__item_dict):
                print(" ", self.__item_dict[item], item)

    def get_name(self):

        return self.__name

    def give_item(self, test_item):

        # If character already has the given item, the item's value is grown
        # by one.
        if test_item in self.__item_dict:
            self.__item_dict[test_item] += 1

        # If character doesn't have the given item, a new key-value pair it
        # added to the dictionary __items.
        else:
            self.__item_dict[test_item] = 1

    def remove_item(self, item_to_be_removed):

        # If character already has the given item, the item's value is reduced
        # by one.
        if item_to_be_removed in self.__item_dict:
            self.__item_dict[item_to_be_removed] -= 1

            # If character had only one of the items that was reduced,
            # the item itself is removed from the dictionary.
            if self.__item_dict[item_to_be_removed] == 0:
                self.__item_dict.pop(item_to_be_removed)

    def has_item(self, test_item):

        if test_item in self.__item_dict:
            return True

        else:
            return False

    def how_many(self, amount_of_test_items):

        # If character doesn't have the item in the dictionary then zero it
        # returned.
        if amount_of_test_items not in self.__item_dict:
            return 0

        # Otherwise the item's value is returned.
        else:
            return self.__item_dict.get(amount_of_test_items)

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """

        if item in self.__item_dict:

            # If character already has the given item, the item's value is grown
            # by one.
            if item in target.__item_dict:
                target.__item_dict[item] += 1

            # If character doesn't have the given item, a new key-value pair it
            # added to the dictionary __items_dict.
            else:
                target.__item_dict[item] = 1

            if item in self.__item_dict:
                # If character already has the given item, the item's value
                # is reduced by one.
                self.__item_dict[item] -= 1

                # If character had only one of the items that was reduced,
                # the item itself is removed from the dictionary.
                if self.__item_dict[item] == 0:
                    self.__item_dict.pop(item)

            return True

        return False

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """

        if weapon not in WEAPONS:
            print(f"Attack fails: unknown weapon \"{weapon}\".")
            return

        elif self.__name == target.__name:
            print(f"Attack fails: {self.__name} can't attack him/herself.")
            return

        elif weapon not in self.__item_dict:
            print(f"Attack fails: {self.__name} doesn't have \"{weapon}\".")
            return

        else:
            print(f"{self.__name} attacks {target.__name} delivering "
                  f"{WEAPONS[weapon]} damage.")

            # Weapons damage is reduced from the character's hitpoints.
            target.__hitpoints -= WEAPONS[weapon]

            if target.__hitpoints < 0:
                print(f"{self.__name} successfully defeats {target.__name}.")


WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}

def main():

    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)

    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()

    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    # Conan doesn't have a sword.
    conan.attack(deadpool, "sword")

    # A character is not allowed to attack himself.
    conan.attack(conan, "gun")

    # Pen is not a known weapon in WEAPONS dict.
    conan.attack(conan, "pen")

    # Attack with a gun.
    conan.attack(deadpool, "gun")

    # Deadpool retaliates
    # Deadpool has a sword.
    deadpool.attack(conan, "sword")

    # Conan's 2nd turn
    # Attack with a gun again.
    conan.attack(deadpool, "gun")

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()

if __name__ == "__main__":
    main()