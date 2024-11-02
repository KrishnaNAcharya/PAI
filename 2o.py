from collections import deque

def swap_adjacent(word, i):
    word_list = list(word)
    word_list[i], word_list[i + 1] = word_list[i + 1], word_list[i]
    return ''.join(word_list)

def simple_solver(start, goal):
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path
        
        for i in range(len(current) - 1):
            new_word = swap_adjacent(current, i)
            if new_word not in visited:
                visited.add(new_word)
                queue.append((new_word, path + [new_word]))
    
    return None

# Example usage
start_word = "secure"
goal_word = "rescue"
solution_path = simple_solver(start_word, goal_word)

if solution_path:
    print("Solution path:")
    for i, step in enumerate(solution_path):
        print(f"{i}) {step}")
else:
    print(f"Goal '{goal_word}' is not reachable from '{start_word}'.")
