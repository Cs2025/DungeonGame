# Character object for storing name, items, etc.

class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.has_torch = False
        self.coins = 0

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def has_item(self, item):
        return item in self.inventory

    def add_coins(self, amount):
        self.coins += amount

    def remove_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
            return True
        return False

    def get_coins(self):
        return self.coins

    def get_inventory(self):
        return self.inventory
