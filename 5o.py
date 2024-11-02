class Literal:
    def __init__(self, name, sign=True):
        self.name = str(name)
        self.sign = sign
    
    def neg(self):
        return Literal(self.name, not self.sign)

def solve_sat(KB):
    # Convert KB to simple format: [{name: sign}]
    clauses = []
    for clause in KB:
        simple_clause = {}
        for lit in clause:
            simple_clause[lit.name] = lit.sign
        clauses.append(simple_clause)
    
    # Get all variables
    vars = set(lit.name for clause in KB for lit in clause)
    
    # Try all possible True/False combinations
    for i in range(2 ** len(vars)):
        # Create this attempt's assignments
        assignment = {}
        for j, var in enumerate(sorted(vars)):  # Sort variables for consistent ordering
            value = bool(i & (1 << j))
            if value:
                assignment[var] = True  # Changed to True instead of 'true'
            
        # Check if this assignment works
        works = True
        for clause in clauses:
            # Check each clause
            clause_works = False
            for var, should_be_true in clause.items():
                is_true = var in assignment and assignment[var]
                if is_true == should_be_true:
                    clause_works = True
                    break
            if not clause_works:
                works = False
                break
        
        # If we found a working assignment, return it
        if works:
            # Mark unused variables as 'free'
            result = {}
            for var in vars:
                if var in assignment:
                    result[var] = True  # Use True instead of 'true'
                else:
                    result[var] = 'free'
            return [True, result]
            
    return False

# Test it
A = Literal('A')
B = Literal('B')
C = Literal('C')
D = Literal('D')
KB = [{A, B}, {A.neg(), C.neg()}, {A.neg(), B, D}]
print(solve_sat(KB))