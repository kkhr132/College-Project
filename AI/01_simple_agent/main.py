import random

class Environment:
    def __init__(self, size=5):
        self.size = size
        self.grid = [['clean' for _ in range(size)] for _ in range(size)]
        # Randomly place dirt
        for _ in range(size):
            x, y = random.randint(0, size-1), random.randint(0, size-1)
            self.grid[x][y] = 'dirty'

    def get_percept(self, position):
        x, y = position
        return self.grid[x][y]

    def clean(self, position):
        x, y = position
        if self.grid[x][y] == 'dirty':
            self.grid[x][y] = 'clean'
            return True
        return False

    def is_clean(self):
        return all(cell == 'clean' for row in self.grid for cell in row)

class SimpleAgent:
    def __init__(self, env):
        self.env = env
        self.position = (0, 0)
        self.actions = 0

    def act(self):
        percept = self.env.get_percept(self.position)
        if percept == 'dirty':
            self.env.clean(self.position)
            print(f"Cleaned position {self.position}")
        else:
            # Move to a random adjacent position
            x, y = self.position
            moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            valid_moves = [(nx, ny) for nx, ny in moves if 0 <= nx < self.env.size and 0 <= ny < self.env.size]
            if valid_moves:
                self.position = random.choice(valid_moves)
                print(f"Moved to {self.position}")
        self.actions += 1

    def run(self, max_steps=100):
        while not self.env.is_clean() and self.actions < max_steps:
            self.act()
        if self.env.is_clean():
            print("Environment is clean!")
        else:
            print("Max steps reached, environment not fully clean.")

if __name__ == "__main__":
    env = Environment()
    agent = SimpleAgent(env)
    agent.run()
