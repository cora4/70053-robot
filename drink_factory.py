""" drink_factory module.

Contains the DrinkFactory class to generate drinks.
"""

import random

from drink import Drink

class DrinkFactory:
    def __init__(self, candidate_names=[]):
        """ Constructor for DrinkFactory.

        Args:
            candidate_names (str): Name options for drink
            owner_id (int): ID of the owner of the drink
        """
        if len(candidate_names) > 0:
            self.names = candidate_names 
        else:
            self.names = self._get_default_names()

        
    def _get_default_names(self):
        return ["Ribena", "Dr Pepper", "Fanta", "Lucozade", "J2O",
                "Tropicana"]
    
    def create_drink(self, owner_id=None):
        name = random.choice(self.names)
        return Drink(name, owner_id)