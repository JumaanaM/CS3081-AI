CS3081 Artificial Intelligence - Assignment 2: Resolution Hackathon

Overview
- This assignment solves "The Missing Exam Paper" logic puzzle using Propositional Logic, Conjunctive Normal Form (CNF), and Proof by Contradiction via Resolution.

Summary of Findings
- Level 01 (CNF Relay): Converted all 7 security clues into 9 CNF clauses (K1–K9).
- Level 02 (Resolution Dominoes): Matched 6 clause card pairs, applied factoring where duplicates appeared, and identified the trap pair (CARD_A and CARD_I) which yields a tautology rather than an empty clause.
- Level 03 (Solve the Case):
      Omar (KB ⊨ O): Guilty (derived empty clause).
      Sara ($KB ⊨ ¬S): Innocent (derived empty clause).
      Lina: Undetermined (neither L nor ¬L is entailed by the KB).
