""" drink module.

Contains the Drink class that can be placed on the grid cell.
"""

class Drink:
    def __init__(self, name, owner_id):
        """ Constructor for Drink.

        Args:
            name (str): Name of the drink (e.g. Ribena)
            owner_id (int): ID of the owner of the drink
        """
        self.name = name
        self.owner_id = owner_id
        self.percent_filled = 1.0

        
    def is_full(self):
        return self.percent_filled == 1.
    
    def is_empty(self):
        return self.percent_filled == 0.
    
    def __str__(self):
        return f"Drink({self.name} for owner {self.owner_id})"