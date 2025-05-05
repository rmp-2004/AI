import heapq

class PuzzleState:
    def __init__(self, board, goal, move="", depth=0, previous=None):
        self.board = board
        self.goal = goal
        self.move = move
        self.depth = depth
        self.previous = previous
        self.zero_index = board.index(0)
        self.estimated_cost = self.depth + self.heuristic()

    def heuristic(self):
        # Manhattan Distance
        distance = 0
        for i in range(9):
            if self.board[i] != 0:
                correct_pos = self.goal.index(self.board[i])
                x1, y1 = i % 3, i // 3
                x2, y2 = correct_pos % 3, correct_pos // 3
                distance += abs(x1 - x2) + abs(y1 - y2)
        return distance

    def get_neighbors(self):
        neighbors = []
        moves = [(-1, 0, "Left"), (1, 0, "Right"), (0, -1, "Up"), (0, 1, "Down")]
        x, y = self.zero_index % 3, self.zero_index // 3

        for dx, dy, action in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_y * 3 + new_x
                new_board = self.board[:]
                new_board[self.zero_index], new_board[new_index] = new_board[new_index], new_board[self.zero_index]
                neighbors.append(PuzzleState(new_board, self.goal, action, self.depth + 1, self))
        return neighbors

    def __lt__(self, other):
        return self.estimated_cost < other.estimated_cost

    def is_goal(self):
        return self.board == self.goal

    def get_state_path(self):
        path = []
        state = self
        while state:
            path.append(state.board)
            state = state.previous
        return path[::-1]  # From initial to goal


def a_star(initial_board, goal_state):
    start = PuzzleState(initial_board, goal_state)
    open_list = []
    heapq.heappush(open_list, start)
    visited = set()

    while open_list:
        current = heapq.heappop(open_list)
        if tuple(current.board) in visited:
            continue
        visited.add(tuple(current.board))

        if current.is_goal():
            return current.get_state_path()

        for neighbor in current.get_neighbors():
            if tuple(neighbor.board) not in visited:
                heapq.heappush(open_list, neighbor)

    return None

initial_state = [1, 2, 3,
                 8, 0, 4,
                 7, 6, 5]

goal_state = [2, 8, 1,
              0, 4, 3,
              7, 6, 5]  # You can change this to any valid goal

solution_path = a_star(initial_state, goal_state)

if solution_path:
    print("Steps from initial to goal:")
    for i, board in enumerate(solution_path):
        print(f"\nStep {i}:")
        for j in range(0, 9, 3):
            print(board[j:j+3])
else:
    print("No solution found.")
