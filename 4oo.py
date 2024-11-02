from constraint import Problem

# Define the variables and their domains
VARIABLES = ["csc", "maths", "phy", "che", "tam", "eng", "bio"]
DOMAIN = ["Monday", "Tuesday", "Wednesday"]

# Define the constraints
def no_conflict(csc, maths, phy, che, tam, eng, bio):
    # Define the constraints based on your original constraints
    return (
        (csc != maths) and
        (csc != phy) and
        (maths != phy) and
        (maths != che) and
        (maths != tam) and
        (phy != tam) and
        (phy != eng) and
        (che != eng) and
        (tam != eng) and
        (tam != bio) and
        (eng != bio)
    )

# Create a problem instance
problem = Problem()

# Add variables with their domains
problem.addVariables(VARIABLES, DOMAIN)

# Add the constraints
problem.addConstraint(no_conflict, VARIABLES)

# Solve the problem and get the solutions
solution = problem.getSolutions()

# Print the first solution (if any)
if solution:
    print(solution[0])  # Print the first solution
else:
    print("No solution found")
