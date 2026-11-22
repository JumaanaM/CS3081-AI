from logic import * 

AKnight = Symbol ("A is a knight")
AKnave = Symbol ("A is a knave")

BKnight = Symbol ("B is a knight")
BKnave = Symbol ("B is a knave")

CKnight = Symbol ("C is a knight")
CKnave = Symbol ("C is a knave")

# Puzzle 0
# A says "I am both a knight and a knave."
statement0 = And(AKnight, AKnave)
knowledge0 = And(
    # A is either a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # What A says
    Implication(AKnight, statement0),
    Implication(AKnave, Not(statement0))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
statement1 = And(AKnave, BKnave)
knowledge1 = And(
    # Rules for A and B
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # What A says
    Implication(AKnight, statement1),
    Implication(AKnave, Not(statement1))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
statement2_A = Or(And(AKnight, BKnight), And(AKnave, BKnave))
statement2_B = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    # Rules for A and B
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # What A says
    Implication(AKnight, statement2_A),
    Implication(AKnave, Not(statement2_A)),
    # What B says
    Implication(BKnight, statement2_B),
    Implication(BKnave, Not(statement2_B))
)

# Puzzle 3 (Bonus)
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Rules for A, B, and C
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A says either "I am a knight." or "I am a knave."
    Or(
        And(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight))),
        And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))
    ),

    # B says "A said 'I am a knave'."
    Implication(BKnight, And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))),
    Implication(BKnave, Not(And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))))),

    # B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C says "A is a knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")


if __name__ == "__main__":
    main()