# -------------------------------
# INFERENTIAL LOGIC IN ONE FILE
# kanren + sympy + pyDatalog
# -------------------------------

print("\n=== INFERENTIAL LOGIC DEMO ===")

# =========================================================
# 1) KANREN (Relational Logic)
# =========================================================
print("\n[1] Using Kanren")

from kanren import Relation, facts, run, var

human = Relation()
mortal = Relation()

facts(human, ("Socrates",))

# Rule application
for person in ["Socrates"]:
    if run(1, var(), human(person)):
        facts(mortal, (person,))

x = var()
print("Kanren Infers Mortal:", run(0, x, mortal(x)))


# =========================================================
# 2) SYMPY (Symbolic Logic)
# =========================================================
print("\n[2] Using SymPy")

from sympy import symbols
from sympy.logic.boolalg import Implies

Human = symbols('Human')
Mortal = symbols('Mortal')

rule = Implies(Human, Mortal)

# Socrates is human ⇒ Human = True
inference = rule.subs(Human, True)

print("SymPy Infers Mortal:", inference)


# =========================================================
# 3) pyDatalog (Rule-Based Logic)
# =========================================================
print("\n[3] Using pyDatalog")

from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms('Human, Mortal, X')

+ Human('Socrates')
Mortal(X) <= Human(X)

print("pyDatalog Infers Mortal:")
print(Mortal(X))


print("\n=== END OF DEMO ===")
