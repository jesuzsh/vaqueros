# Implementation of the receipt class.
class Receipt:
    # Constructor for the Receipt class
    def __init__(self):
        # A receipt will have a list of items being added
        self.item = None
        self.cost = None
        self.frequency = None

    # Add an item to the receipt
    def set_item(self, x):
        self.item = x

    # Add a cost to the item
    def set_cost(self, c):
        self.cost = c

    # Add the frequency which the cost will occur
    def set_frequency(self, f):
        self.cost = f

    # Below are the getters of the class
    def get_item(self):
        return self.item

    def get_cost(self):
        return self.cost

    def get_frequency(self):
        return self.frequency
