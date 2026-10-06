""" grid module.

Contains the Grid class.
"""

import random

class Grid:
    def __init__(self, size):
        """ Constructor for Grid.

        Args:
            size (int): Length of grid (assume square)
        """
        self.size = size
        
        # initialise each cell to empty list to save on checking later
        # cells[(0, 2)] will contain a list of drinks in that cell.
        self._cells = {(row, col): [] 
            for row in range(size) for col in range(size)
        }
        
    def add_drink(self, drink, cell_position):
        """ Add a Drink to at a given cell grid

        Args:
            drink (Drink): The drink to add to cell
            cell_position (tuple): (row, col) coordinates
        """
        
        try:
            self._cells[cell_position].append(drink)
        except KeyError:
            print(f"Warning: Can't add drink to {cell_position} because the position is out of bounds. Drink not added")
            
    def add_drink_at_random_corner(self, drink):
        """ Add a Drink at a random corner cell

        Args:
            drink (Drink): The drink to add to cell
        """
        
        position = self.generate_random_corner_position()
        self.add_drink(drink, position)

    def get_drinks_at_cell(self, cell_position):
        """ Retrieve a list of Drinks at a given cell grid.
        
        Will return an empty list if cell_position is out of bounds.

        Args:
            cell_position (tuple): (row, col) coordinates
        """
        
        try:
            return self._cells[cell_position]
        except KeyError:
            return []

    def get_owner_drink(self, position, owner_id):
        """ Return an owner's drink at cell position (if it exists).
        
        Args:
            position (tuple): (row, col) coordinates
            owner_id (int): ID for owner
        
        Returns:
            Drink : or None if no drink for owner at position
        """
        drinks = self.get_drinks_at_cell(position)
        for drink in drinks:
            if drink.owner_id == owner_id:
                return drink
        return None
    
    def generate_random_position(self):
        """ Generate a random (row, col) position for the robot.

        The coordinates will be between 0 to self.grid.size.

        Returns:
            tuple[int, int] : (row, col) coordinates
        """
        row = random.randint(0, self.size-1) 
        col = random.randint(0, self.size-1)
        return (row, col)
        
    def generate_random_corner_position(self):
        """ Generate a random cell located at one of the 4 corners of grid.

        Returns:
            tuple[int, int] : (row, col) coordinates
        """
        
        # set row and col to either 0 or grid_size-1
        row = random.choice([0, self.size-1])
        col = random.choice([0, self.size-1])
        return (row, col)
    

def test_add_out_of_bounds():
    grid = Grid(size=5)
    drink = Drink("Ribena", "1000")
    grid.add_drink(drink, (6,7))
    drinks_at_cell = grid.get_drinks_at_cell((6,7))
    assert drinks_at_cell == []
    
    
def test_grid():
    grid = Grid(size=5)
    assert grid.size == 5
    
    drink = Drink("Ribena", "1000")
    grid.add_drink(drink, (2, 2))
    drink = Drink("Dr Pepper", "1000")
    grid.add_drink(drink, (2, 2))
    drink = Drink("Fanta", "1000")
    grid.add_drink(drink, (3, 2))
    
    drinks = grid.get_drinks_at_cell((2, 2))
    assert len(drinks) == 2
    drinks = grid.get_drinks_at_cell((3, 2))
    assert len(drinks) == 1 
    drinks = grid.get_drinks_at_cell((0, 1))
    assert len(drinks) == 0 
    
    
if __name__ == "__main__":
    from drink import Drink
    test_grid()
