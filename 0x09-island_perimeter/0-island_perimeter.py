#!/usr/bin/python3
"""
Define island_perimeter function that finds the perimeter
of an island in a body of water
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.
    The grid is represented as a list of lists of integers where:
    - 0 represents water
    - 1 represents land
    The island is surrounded by water and is formed by connecting
    adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are surrounded by water.
    Args:
        grid (list of list of int): A 2D grid representing the map
        of the island and water.
    Returns:
        int: The perimeter of the island.
    """

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # If this cell is land
                # Check the four possible directions
                if i == 0 or grid[i - 1][j] == 0:  # Check top
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Check bottom
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Check left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Check right
                    perimeter += 1

    return perimeter
