class Chandrayaan:
    def __init__(self, initial_position, initial_direction):
        self.position = initial_position
        self.direction = initial_direction

    def forward(self):
        if self.direction == 'N':
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.direction == 'S':
                self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif self.direction == 'E':
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.direction == 'W':
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.direction == 'U':
            self.position = (self.position[0], self.position[1], self.position[2] + 1)
        elif self.direction == 'D':
                self.position = (self.position[0], self.position[1], self.position[2] - 1) 

    def backward(self):
        if self.direction == 'N':
            self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif self.direction == 'S':
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.direction == 'E':
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.direction == 'W':
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.direction == 'U':
            self.position = (self.position[0], self.position[1], self.position[2] - 1)
        elif self.direction == 'D':
            self.position = (self.position[0], self.position[1], self.position[2] + 1)
        
    def left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'U':
            self.direction = 'W'
        elif self.direction == 'D':
            self.direction = 'S'

    def right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'
        elif self.direction == 'U':
            self.direction = 'S'
        elif self.direction == 'D':
            self.direction = 'N'

    def up(self):
        if self.direction in ['N', 'E', 'W', 'S']:
            self.direction = 'U'
        elif self.direction == 'D':
            self.direction = 'S'
        elif self.direction == 'U':
            self.direction = 'N'
    
    def down(self):
        if self.direction in ['N', 'E', 'W', 'S']:
            self.direction = 'D'
        elif self.direction == 'U':
            self.direction = 'N'
        elif self.direction == 'D':
            self.direction = 'S'

    def execute_command(self, command):
        if command == 'f':
            self.forward()
            
        elif command == 'b':
            self.backward()
            
        elif command == 'l':
            self.left()

        elif command == 'r':
            self.right()

        elif command == 'u':
            self.up()
            
        elif command == 'd':
            self.down()

           