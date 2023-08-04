# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 13:58:46 2023

@author: Administrator
"""

import unittest
from chandrayaan import Chandrayaan

class TestChandrayaan(unittest.TestCase):
    def setUp(self):
        self.spacecraft = Chandrayaan((0, 0, 0), 'N')
        
    def test_initial_position_and_direction(self):
        self.assertEqual(self.spacecraft.position, (0, 0, 0))
        self.assertEqual(self.spacecraft.direction, 'N')

    def test_move_forward(self):
        self.spacecraft.execute_command('f')
        self.assertEqual(self.spacecraft.position, (0, 1, 0))
        self.assertEqual(self.spacecraft.direction, 'N')
    
    def test_move_backward(self):
        self.spacecraft.execute_command('b')
        assert self.spacecraft.position == (0, -1, 0)
        assert self.spacecraft.direction == 'N'

    def test_rotate_left(self):
        self.spacecraft.execute_command('l')
        assert self.spacecraft.position == (0, 0, 0)
        assert self.spacecraft.direction == 'W'

    def test_rotate_right(self):
        self.spacecraft.execute_command('r')
        assert self.spacecraft.position == (0, 0, 0)
        assert self.spacecraft.direction == 'E'

    def test_rotate_up(self):
        self.spacecraft.execute_command('u')
        assert self.spacecraft.position == (0, 0, 0)
        assert self.spacecraft.direction == 'U'
    
    def test_rotate_down(self):
        self.spacecraft.execute_command('d')
        assert self.spacecraft.position == (0, 0, 0)
        assert self.spacecraft.direction == 'D'
    
    def test_multiple_commands(self):
        self.spacecraft.execute_command('f')
        self.spacecraft.execute_command('r')
        self.spacecraft.execute_command('u')
        self.spacecraft.execute_command('b')
        self.spacecraft.execute_command('l')
        assert self.spacecraft.position == (0, 1, -1)
        assert self.spacecraft.direction == 'W'
    
    def test_multiple_commands2(self):
        self.spacecraft.execute_command('f')
        self.spacecraft.execute_command('f')
        self.spacecraft.execute_command('r')
        self.spacecraft.execute_command('r')
        self.spacecraft.execute_command('f')
        self.spacecraft.execute_command('u')
        self.spacecraft.execute_command('b')
        self.spacecraft.execute_command('u')
        self.spacecraft.execute_command('b')
        assert self.spacecraft.position == (0, 0, -1)
        assert self.spacecraft.direction == 'N'
    
    def test_multiple_commands_loop(self):
        command = ['f', 'r', 'u', 'b', 'l']
        for i in command:
            self.spacecraft.execute_command(i)
        assert self.spacecraft.position == (0, 1, -1)
        assert self.spacecraft.direction == 'W'

if __name__ == '__main__':        
    unittest.main(exit = False)
       