importsympy

# Define propositional variables
p = sympy.symbols('p')
q = sympy.symbols('q')
r = sympy.symbols('r')

# Define propositions
prop1 = p
prop2 = sympy.Not(q)
prop3 = sympy.And(p, q)
prop4 = sympy.Or(p, q)
prop5 = sympy.Implies(p, q)
prop6 = sympy.Eq(p, q)

prop7 = sympy.Not(p)
prop8 = sympy.And(p, p)  # p AND p is equivalent to p
prop9 = sympy.Or(p, p)   # p OR p is equivalent to p
prop10 = sympy.Or(p, sympy.Not(p))  # p OR NOT p is always True (Law of Excluded Middle)
prop11 = sympy.And(p, sympy.Not(p))  # p AND NOT p is always False (Law of Non-Contradiction)
prop12 = sympy.Implies(p, q).simplify()  # Simplified form of p IMPLIES q (Modus Ponens)

prop15 = sympy.Eq(sympy.Or(p, q), sympy.Or(q, p))  # Commutative Law for OR
prop16 = sympy.Eq(sympy.And(p, q), sympy.And(q, p))  # Commutative Law for AND
prop17 = sympy.Eq(sympy.Or(p, sympy.Or(q, r)), sympy.Or(sympy.Or(p, q), r))  # Associative Law for OR
prop18 = sympy.Eq(sympy.And(p, sympy.And(q, r)), sympy.And(sympy.And(p, q), r))  # Associative Law for AND
prop19 = sympy.Eq(sympy.Or(p, sympy.And(q, r)), sympy.And(sympy.Or(p, q), sympy.Or(p, r)))  # Distributive Law

# Define some additional propositions for testing
prop13 = sympy.Or(p, q, r)
prop14 = sympy.And(p, q, r)

# Define values for propositional variables
p_value = True
q_value = False

print(f"p = {p_value}, q = {q_value}")
print(f"prop1 (p): {prop1.subs({p: p_value})}")
print(f"prop2 (not q): {prop2.subs({q: q_value})}")
print(f"prop3 (p and q): {prop3.subs({p: p_value, q: q_value})}")
print(f"prop4 (p or q): {prop4.subs({p: p_value, q: q_value})}")
print(f"prop5 (p implies q): {prop5.subs({p: p_value, q: q_value})}")
print(f"prop6 (p is equivalent to q): {prop6.subs({p: p_value, q: q_value})}")
print(f"prop7 (not p): {prop7.subs({p: p_value})}")
print(f"prop8 (p and p): {prop8.subs({p: p_value})}")
print(f"prop9 (p or p): {prop9.subs({p: p_value})}")
print(f"prop10 (p or not p): {prop10.subs({p: p_value})}")
print(f"prop11 (p and not p): {prop11.subs({p: p_value})}")
print(f"prop12 (Modus Ponens): {prop12.subs({p: p_value, q: q_value})}")
print(f"prop15 (Commutative Law for OR): {prop15.subs({p: p_value, q: q_value})}")
print(f"prop16 (Commutative Law for AND): {prop16.subs({p: p_value, q: q_value})}")
print(f"prop17 (Associative Law for OR): {prop17.subs({p: p_value, q: q_value, r: p_value})}")
print(f"prop18 (Associative Law for AND): {prop18.subs({p: p_value, q: q_value, r: p_value})}")
print(f"prop19 (Distributive Law): {prop19.subs({p: p_value, q: q_value, r: p_value})}")

# Check for validity
defis_valid(proposition):
    returnall(proposition.subs({p: p_val, q: q_val}) forp_valin [True, False] forq_valin [True, False])

print(f"Is prop1 valid? {is_valid(prop1)}")
print(f"Is prop2 valid? {is_valid(prop2)}")
print(f"Is prop3 valid? {is_valid(prop3)}")
print(f"Is prop4 valid? {is_valid(prop4)}")
print(f"Is prop5 valid? {is_valid(prop5)}")
print(f"Is prop6 valid? {is_valid(prop6)}")

# Check for satisfiability
print(f"Is prop1 satisfiable? {sympy.satisfiable(prop1)}")
print(f"Is prop2 satisfiable? {sympy.satisfiable(prop2)}")
print(f"Is prop3 satisfiable? {sympy.satisfiable(prop3)}")
print(f"Is prop4 satisfiable? {sympy.satisfiable(prop4)}")

# Check for entailment
print(f"Does prop1 entail prop2? {sympy.ask(sympy.Implies(prop1, prop2))}")

# Convert propositions to DNF and CNF
print(f"prop13 (p or q or r) in DNF: {sympy.to_dnf(prop13)}")
print(f"prop13 (p or q or r) in CNF: {sympy.to_cnf(prop13)}")
print(f"prop14 (p and q and r) in DNF: {sympy.to_dnf(prop14)}")
print(f"prop14 (p and q and r) in CNF: {sympy.to_cnf(prop14)}")
