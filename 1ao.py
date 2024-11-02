from collections import deque

class Solution:
    def solve(self, board):
        start = tuple(sum(board, []))
        target = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        
        if start == target:
            return 0

        moves = [
            [1, 3], [0, 2, 4], [1, 5],
            [0, 4, 6], [1, 3, 5, 7],
            [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]
        ]

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            state, steps = queue.popleft()
            zero_pos = state.index(0)

            for move in moves[zero_pos]:
                new_state = list(state)
                new_state[zero_pos], new_state[move] = new_state[move], new_state[zero_pos]
                new_state = tuple(new_state)
                
                if new_state == target:
                    return steps + 1
                
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
        
        return -1

# Example usage
ob = Solution()
matrix = [
    [3, 1, 2],
    [4, 7, 5],
    [6, 8, 0]
]
print("NO OF MOVES==", ob.solve(matrix))
