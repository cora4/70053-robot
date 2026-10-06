"""
My amazing robot!! (Refactored!)
"""

import random

from drink_factory import DrinkFactory
from grid import Grid
from robot import Robot
from robot_factory import RobotFactory 


def read_names_from_file(filepath=None):
    """ Read list of candidate names from a given file name

    Args:
        filepath (str): The path to the file 
        
    Returns:
        list : List of candidate names
    """
    
    names = []
    for line in open(filepath):
        name = line.strip()
        names.append(name)
    return names


def simulate_robot_navigation(grid_size=10, n_robots=3, namelist_path="robot_names.txt"):
    """ Starts a simulation session of a robot navigating to a target

    Args:
        grid_size (int) : The size of the grid. Defaults to 10.
        n_robots (int) : Number of robots to simulate. Defaults to 3.
        namelist_path (str) : The path to a text file containing candidate robot names. Defaults to "robot_names.txt".
    """
    
    # get list of candidate names that can be used
    candidate_names = read_names_from_file(namelist_path)
    
    # create new robots
    grid = Grid(grid_size)
    prev_id = 1000
    factory = RobotFactory(grid, candidate_names, prev_id)
    robots = factory.create_robots(count=n_robots)

    # each robot prints its greeting
    for robot in robots:
        robot.greet()
    
    print() # print a new line 
    
    # add drinks for each robot
    drink_factory = DrinkFactory()
    for robot in robots:
        drink = drink_factory.create_drink(robot.id)
        grid.add_drink_at_random_corner(drink)
            
    # each robot navigates to its drink
    for robot in robots:
        robot.navigate_to_drink()
        print() # print a new line to separate the different robots
        

# Robot program starts here!
grid_size = 10
n_robots = 3
namelist_path = "robot_names.txt"
simulate_robot_navigation(
    grid_size=grid_size, 
    n_robots=n_robots, 
    namelist_path=namelist_path
)

