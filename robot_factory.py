""" robot_factory module.

Contains the RobotFactory class for creating a new robot.
"""

import random

from robot import Robot, LeapingRobot

class RobotFactory:
    def __init__(self, grid, candidate_names=[], prev_id=-1):
        """ Constructor for RobotFactory.

        Args:
            grid (Grid): The grid where the robot will be located
            candidate_names (list): List of possible names for the robot. 
                Will always name the robot as "Robot" if not provided.
            prev_id (int): The ID of the last robot created. Defaults to -1.
        """
        self.grid = grid
        self.names = candidate_names
        self.prev_id = prev_id
        
        
    def create_robots(self, count=1):
        """ Create multiple robot instances.

        Each robot will be initialised with a random robot name, ID, and 
        initial position and direction.

        Args:
            count (int) : The number of robots to create (defaults to 1)
            
        Returns:
            list[Robot]
        """
        robots = []
        for i in range(count):
            robots.append(self.create_robot())
        return robots
    
    
    def create_robot(self):
        """ Create a new robot instance.

        The robot will be initialised with a random robot name, ID, and 
        initial position and direction.

        Returns:
            Robot
        """
        name = self._generate_name()
        identifier = self._generate_id()
        initial_position = self._generate_position()
        initial_direction = self._generate_direction()

        choice = random.randint(0, 1)
        
        if choice == 0:
            return Robot(identifier=identifier, 
                         name=name, 
                         position=initial_position,
                         direction=initial_direction,
                         grid=self.grid)
        else:
            return LeapingRobot(identifier=identifier, 
                         name=name, 
                         position=initial_position,
                         direction=initial_direction,
                         grid=self.grid)

    def _generate_name(self):
        """ Select a robot's name at random from a given list

        Returns:
            str : Robot name
        """
        if len(self.names) > 0:
            return random.choice(self.names)
        else:
            return "Robot"
            


    def _generate_id(self):
        """ Generate a unique ID for the robot. 

        If prev_id is given and is >=0, the function will return prev_id+1
        Otherwise, the function will generate a random number between 1 to 1,000,000 as an ID.

        Returns:
            int : robot ID
        """
        if self.prev_id >= 0:
            self.prev_id += 1
            return self.prev_id
        else:
            return random.randint(1, 1000000)


    def _generate_position(self):
        """ Generate a random (row, col) position for the robot.

        The coordinates will be between 0 to self.grid.size.

        Returns:
            int : row coordinates
            int : column coordinates
        """
        return self.grid.generate_random_position()


    def _generate_direction(self):
        """ Generate a random direction for the robot.

        Returns:
            str : direction ("n", "s", "e" or "w")
        """
        return random.choice(["n", "s", "e", "w"])

