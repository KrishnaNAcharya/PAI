from constraint import *

def create_schedule():
    # Create the constraint solver
    problem = Problem()

    # Define the variables and their possible values
    subjects = ["csc", "maths", "phy", "che", "tam", "eng", "bio"]
    days = ["Monday", "Tuesday", "Wednesday"]
    
    # Add variables to the problem
    problem.addVariables(subjects, days)
    
    # Add constraints - subjects that can't be on the same day
    conflicts = [
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
    
    # Add the constraints to the problem
    for subject1, subject2 in conflicts:
        problem.addConstraint(lambda x, y: x != y, (subject1, subject2))

    # Get the first solution
    solution = problem.getSolution()
    return solution

# Run the scheduler
schedule = create_schedule()
print(schedule)