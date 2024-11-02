from itertools import permutations

def solve(word1, word2, result):
    letters = set(word1 + word2 + result)
    if len(result) > max(len(word1), len(word2)) + 1 or len(letters) > 10:
        print('0 Solutions!')
        return
    
    solutions = []
    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        if all(assignment[word[0]] != 0 for word in [word1, word2, result]):
            num1 = int("".join(str(assignment[char]) for char in word1))
            num2 = int("".join(str(assignment[char]) for char in word2))
            num_result = int("".join(str(assignment[char]) for char in result))
            if num1 + num2 == num_result:
                solutions.append(f"{num1} + {num2} = {num_result}")

    if solutions:
        print("\nSolutions:")
        for sol in solutions:
            print(sol)
    else:
        print("No solutions found!")

# Example usage
print('CRYPTARITHMETIC PUZZLE SOLVER')
word1 = input('Enter WORD1: ').upper()
word2 = input('Enter WORD2: ').upper()
result = input('Enter RESULT: ').upper()
solve(word1, word2, result)
