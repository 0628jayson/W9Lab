#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:14:35 2024

@author: jeasonzhang
"""

import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, empty_patches):
        if empty_patches: 
            self.x, self.y = random.choice(empty_patches)  

class World:
    def __init__(self, width, height, num_agents):
        self.width = width
        self.height = height
        self.agents = [Agent(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(num_agents)]
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        for agent in self.agents:
            self.grid[agent.x][agent.y] = agent  

    def find_empty_patches(self):
        return [(x, y) for x in range(self.width) for y in range(self.height) if self.grid[x][y] is None]

    def update(self):
        for agent in self.agents:
            empty_patches = self.find_empty_patches()
            agent.move(empty_patches)
            self.grid = [[None for _ in range(self.width)] for _ in range(height)]  # Clear the grid
            for agent in self.agents:
                self.grid[agent.x][agent.y] = agent  

def main():
    world = World(10, 10, 5)
    for _ in range(10):  
        world.update()

if __name__ == "__main__":
    main()
