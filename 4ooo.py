from itertools import product

# Define variables and their domains
VARIABLES = ["csc", "maths", "phy", "che", "tam", "eng", "bio"]
DOMAIN = ["Monday", "Tuesday", "Wednesday"]

# Define constraints as pairs of variables
CONSTRAINTS = [
    ("csc", "maths"),
    ("csc", "phy"),
    ("maths", "phy"),
    ("maths", "che"),
    ("maths", "tam"),
    ("phy", "tam"),
    ("phy", "eng"),
    ("che", "eng"),
    ("tam", "eng"),
    ("tam", "bio"),
    ("eng", "bio")
]

def is_consistent(assignment):
    """Check if the current assignment is consistent with the constraints."""
    for var1, var2 in CONSTRAINTS:
        if var1 in assignment and var2 in assignment:
            if assignment[var1] == assignment[var2]:
                return False
    return True

def solve_csp():
    """Solve the CSP problem using backtracking."""
    for values in product(DOMAIN, repeat=len(VARIABLES)):
        assignment = dict(zip(VARIABLES, values))
        if is_consistent(assignment):
            return assignment
    return None

# Example usage
solution = solve_csp()
if solution:
    print(solution)
else:
    print("No solution found.")
