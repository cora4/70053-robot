""" robot module.
"""

class Robot:
    """ Robot representation. """
    
    def __init__(self, identifier, name, position, direction, grid):
        """ Initialise the robot's properties.

        Args:
            identifier (int) : Robot ID
            name (str) : Robot Name
            position (tuple) : Robot's (row, col) coordinate
            direction (str) : Robot's direction ("n", "s", "e", or "w")
            grid (Grid) : Grid in which robot can navigate
        """
        self.id = identifier
        self.name = name
        self.position = position
        self.direction = direction
        self.grid = grid

    def greet(self):
        print(f"Hello. My name is {self.name}. My ID is {self.id}.")

    def step_forward(self):
        """ Make robot move one step forward in the current direction.
        """
        grid_size = self.grid.size
        
        direction = self.direction
        row = self.position[0]
        col = self.position[1]
        
        if direction == "n":
            if row > 0:
                row -= 1
        elif direction == "s":
            if row < grid_size - 1:
                row += 1
        elif direction == "w":
            if col > 0:
                col -= 1
        elif direction == "e":
            if col < grid_size - 1:
                col += 1

        self.report_step()
        self.position = (row, col)

    def report_step(self):
        print("Moving one step forward.")
        
    def report_turn_right(self):
        print("Turning 90 degrees clockwise.")

    def turn_right(self):
        """ Turn robot right
        """
        self.report_turn_right()
        
        # Using a dictionary to replace an "if else" statement
        # Much faster, shorter and easier to read!
        # Get rotated direction given current direction
        clockwise_dict = {"n": "e", "e": "s", "s": "w", "w": "n"}
        self.direction = clockwise_dict[self.direction]
        
    def is_facing_wall(self):
        """ Check if robot is currently facing a wall

        Returns:
            bool
        """
        row = self.position[0]
        col = self.position[1]
        direction = self.direction
        grid_size = self.grid.size
        
        return (direction == "w" and col == 0
               or direction == "e" and col == grid_size-1
               or direction == "n" and row == 0
               or direction == "s" and row == grid_size-1)

    def is_at_target(self, target_position):
        """ Check if robot is at a certain target grid cell.

        Args:
            target_position (tuple) : (row, column) coordinate

        Returns:
            bool
        """
        return (self.position[0] == target_position[0] and 
            self.position[1] == target_position[1])
            
    def get_drink(self):
        """ Gets robot's drink at current position (if found).

        Returns:
            Drink : or None if not found
        """
        drink = self.grid.get_owner_drink(self.position, self.id)
        return drink

            
    def move_forward_to_wall(self):
        """ Move robot forward in the current direction until it hits a wall.

        Returns:
            tuple : (row, column) coordinate after hitting a wall
        """
        while not self.is_facing_wall():
            self.step_forward()   
            self.report_location()

    def report_start(self):
        print(f"{self.name} is searching for its drink.")
        
    def report_location(self):
        direction_string = self._generate_direction_string(self.direction)
        print(f"I am currently at ({self.position[0]}, {self.position[1]}), facing {direction_string}.")
        
    def drink(self, drink):
        print(f"I am drinking {drink.name}! I am happy!")

    def report_wall(self):
        print("I have a wall in front of me!")

    def _generate_direction_string(self, direction):
        """ Convert the shorthand direction to its full string representation.
        
        Args:
            direction (str) : current direction
            
        Returns:
            str : the full string representation of direction
        """
        # A good use of a dictionary to replace an "if else" statement
        # Much faster, shorter and easier to read!
        direction_mapping = {
            "n": "North", 
            "s": "South", 
            "e": "East", 
            "w": "West"
        }
        return direction_mapping.get(direction, "North")
        
    def navigate_to_drink(self):
        """ Automatically navigate to a drink assigned to robot.
        """
        self.report_start()
        self.report_location()
        
        drink = self.get_drink()
        while drink is None:
            self.move_forward_to_wall()

            drink = self.get_drink()
            if drink is not None:
                break
            
            self.report_wall()  
            self.turn_right()
            self.report_location()
            
        self.drink(drink)


def _test_robot_init():
    name = "Bender"
    identifier = 1000
    position = (3, 5)
    direction = "n"
    
    robot = Robot(identifier, name, position, direction)
    assert isinstance(robot, Robot)
    assert robot.id == identifier
    assert robot.name == name
    assert robot.position == position
    assert robot.direction == direction
    
    
class LeapingRobot(Robot):
    """ Robot that leaps straight to the edge of a grid. """
    def leap_forward(self):
        """ Make robot leap forward to the edge in the direction it is facing."""
        
        direction = self.direction
        row = self.position[0]
        col = self.position[1]
        
        if direction == "n":
            self.position = (0, col)
        elif direction == "s":
            self.position = (self.grid.size - 1, col)
        elif direction == "w":
            self.position = (row, 0)
        elif direction == "e":
            self.position = (row, self.grid.size - 1)

        self.report_leap()
    
    def report_leap(self):
        print("Leaping forward to the edge.")
        
    def move_forward_to_wall(self):
        """ Move robot forward in the current direction until it hits a wall.

        Returns:
            tuple : (row, column) coordinate after hitting a wall
        """
        self.leap_forward()   
        self.report_location()


if __name__ == "__main__":
    _test_robot_init()