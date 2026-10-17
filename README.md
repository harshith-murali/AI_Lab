# Artificial Intelligence Lab

Python programs for AI lab exercises covering intelligent agents, search, optimization, and propositional logic.

**Name:** Harshith M

**USN:** 1BM24CS113

## Programs and Outputs

Each program has an output screenshot and a text transcript containing the sample inputs and results.

| Week | Exercise | Source | Screenshot | Transcript |
| --- | --- | --- | --- | --- |
| 1 | Tic-Tac-Toe | [Code](1BM24CS113_Week1_TicTacToe.py) | [output.png](outputs/1BM24CS113_Week1_TicTacToe/output.png) | [output.txt](outputs/1BM24CS113_Week1_TicTacToe/output.txt) |
| 1 | Vacuum Cleaner: Simple Reflex and Goal-Based Agents | [Code](1BM24CS113_Week1_Vacuum_Cleaner.py) | [output.png](outputs/1BM24CS113_Week1_Vacuum_Cleaner/output.png) | [output.txt](outputs/1BM24CS113_Week1_Vacuum_Cleaner/output.txt) |
| 2 | 8-Puzzle: Depth-First Search (DFS) | [Code](1BM24CS113_Week2_8PuzzleDFS.py) | [output.png](outputs/1BM24CS113_Week2_8PuzzleDFS/output.png) | [output.txt](outputs/1BM24CS113_Week2_8PuzzleDFS/output.txt) |
| 2 | 8-Puzzle: Iterative Deepening Search (IDS) | [Code](1BM24CS113_Week2_8PuzzleIDLS.py) | [output.png](outputs/1BM24CS113_Week2_8PuzzleIDLS/output.png) | [output.txt](outputs/1BM24CS113_Week2_8PuzzleIDLS/output.txt) |
| 3 | 8-Puzzle: A* Search with Manhattan Distance | [Code](1BM24CS113_Week3_AStar.py) | [output.png](outputs/1BM24CS113_Week3_AStar/output.png) | [output.txt](outputs/1BM24CS113_Week3_AStar/output.txt) |
| 4 | N-Queens: Hill Climbing | [Code](Week4_Week4_HillClimb.py) | [output.png](outputs/Week4_Week4_HillClimb/output.png) | [output.txt](outputs/Week4_Week4_HillClimb/output.txt) |
| 5 | N-Queens: Simulated Annealing | [Code](Week5_Simulated_Annealing.py) | [output.png](outputs/Week5_Simulated_Annealing/output.png) | [output.txt](outputs/Week5_Simulated_Annealing/output.txt) |
| 6 | Propositional Logic: Truth Tables and Entailment | [Code](Week%206%20%E2%80%94%20Propositional%20Logic.py) | [output.png](outputs/Week%206%20%E2%80%94%20Propositional%20Logic/output.png) | [output.txt](outputs/Week%206%20%E2%80%94%20Propositional%20Logic/output.txt) |
| 6 | Observation Book Questions: Logical Entailment | [Code](Week%206%20%E2%80%94%20Observation%20Book%20Questions.py) | [output.png](outputs/Week%206%20%E2%80%94%20Observation%20Book%20Questions/output.png) | [output.txt](outputs/Week%206%20%E2%80%94%20Observation%20Book%20Questions/output.txt) |

## Running the Programs

Install Python 3. The programs use only the Python standard library; no additional packages are required.

From this folder, run a program and follow its input prompts:

```bash
python3 1BM24CS113_Week1_TicTacToe.py
```

Quote filenames that contain spaces:

```bash
python3 "Week 6 — Propositional Logic.py"
```

The first line of every program's output is:

```text
Harshith M : 1BM24CS113
```

## Input Guide

- **Tic-Tac-Toe:** Two players enter positions from `1` to `9` in turn.
- **Vacuum Cleaner:** Enter starting room `A` or `B`, then `Clean` or `Dirty` for each room.
- **8-Puzzle:** Enter nine space-separated numbers, using `0` for the blank. The goal is `1 2 3 4 5 6 7 8 0`. The saved examples start from `1 2 3 4 5 6 0 7 8`.
- **Hill Climbing:** Enter the number of queens, then a permutation of rows from `0` to `n-1`. Each position represents a column. The saved example uses `4` queens and `0 1 2 3`.
- **Simulated Annealing:** Enter the number of queens, the initial rows, a positive initial temperature, a cooling factor between `0` and `1`, and a positive minimum temperature. The saved example uses `4`, `1 3 0 0`, `5`, `0.9`, and `0.01`. Results can vary because the algorithm uses random moves.
- **Propositional Logic:** Enter proposition names, knowledge-base sentences, and a query. Use `~` for NOT, `&` for AND, `|` for OR, `>>` for implication, and `==` for equivalence. Use parentheses to make grouping explicit. The saved example uses propositions `P Q`, knowledge base `P >> Q` and `P`, and query `Q`.
- **Observation Book Questions:** Choose one of the three predefined problems and an available query. The saved example selects problem `1` and query `1`.

## Output Files

Outputs are organized by program name:

```text
outputs/
  <program name>/
    output.png
    output.txt
```

The PNG files show recorded sample runs. The corresponding text files preserve the same inputs and output for reference.
