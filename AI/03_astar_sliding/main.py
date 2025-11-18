import heapq

class Puzzle:
    def __init__(self, initial_state):
        self.initial = initial_state
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # 0 represents the blank

    def get_neighbors(self, state):
        neighbors = []
        blank = state.index(0)
        row, col = divmod(blank, 3)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_blank = new_row * 3 + new_col
                new_state = state[:]
                new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
                neighbors.append(new_state)

        return neighbors

    def heuristic(self, state):
        # Manhattan distance
        distance = 0
        for i in range(9):
            if state[i] != 0:
                goal_row, goal_col = divmod(self.goal.index(state[i]), 3)
                curr_row, curr_col = divmod(i, 3)
                distance += abs(goal_row - curr_row) + abs(goal_col - curr_col)
        return distance

    def a_star(self):
        start = tuple(self.initial)
        goal = tuple(self.goal)

        frontier = []
        heapq.heappush(frontier, (0, start, []))  # (priority, state, path)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while frontier:
            current_priority, current, path = heapq.heappop(frontier)

            if current == goal:
                return path + [list(current)]

            for neighbor in self.get_neighbors(list(current)):
                new_cost = cost_so_far[current] + 1
                neighbor_tuple = tuple(neighbor)
                if neighbor_tuple not in cost_so_far or new_cost < cost_so_far[neighbor_tuple]:
                    cost_so_far[neighbor_tuple] = new_cost
                    priority = new_cost + self.heuristic(neighbor)
                    heapq.heappush(frontier, (priority, neighbor_tuple, path + [list(current)]))
                    came_from[neighbor_tuple] = current

        return None

# Example usage
if __name__ == "__main__":
    initial = [1, 2, 3, 4, 0, 6, 7, 5, 8]  # Example puzzle state
    puzzle = Puzzle(initial)
    solution = puzzle.a_star()
    if solution:
        print("Solution found:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
