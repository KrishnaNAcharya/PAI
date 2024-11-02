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
    vars = sorted(set(lit.name for clause in KB for lit in clause))
    
    # Try all possible True/False combinations
    for i in range(2 ** len(vars)):
        # Create this attempt's assignments
        assignment = {}
        for j, var in enumerate(vars):
            value = bool(i & (1 << j))
            assignment[var] = 'true' if value else 'false'
            
        # Check if this assignment works
        works = True
        for clause in clauses:
            # Check each clause
            clause_works = False
            for var, should_be_true in clause.items():
                is_true = assignment[var] == 'true'
                if is_true == should_be_true:
                    clause_works = True
                    break
            if not clause_works:
                works = False
                break
        
        # If we found a working assignment, return it
        if works:
            # Mark unused variables as 'free'
            for var in vars:
                if var not in assignment:
                    assignment[var] = 'free'
            return [True, {v: assignment[v] for v in vars}]
    
    return [False]

# Test it
A = Literal('A')
B = Literal('B')
C = Literal('C')
D = Literal('D')
KB = [{A, B}, {A.neg(), C.neg()}, {A.neg(), B, D}]
print(solve_sat(KB))
