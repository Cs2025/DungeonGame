# Character object for storing name, items, etc.

class Character:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.has_torch = False  # New attribute for torch

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def has_item(self, item):
        return item in self.items
