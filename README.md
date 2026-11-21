# Artificial Intelligence Lab

Week-wise Jupyter notebooks for the Artificial Intelligence lab. Each notebook contains beginner-friendly theory notes, algorithm steps, interactive Python implementations, sample inputs and captured outputs.

## Notebooks and topics

| Week | Notebook | Topics |
| --- | --- | --- |
| 1 | `Week1_TicTacToe_VacuumAgents.ipynb` | Tic-Tac-Toe minimax; reflex and goal-based vacuum agents |
| 2 | `Week2_8Puzzle_DFS_IDS.ipynb` | 8-puzzle DFS and IDS; BFS theory |
| 3 | `Week3_8Puzzle_AStar.ipynb` | A* with misplaced-tile and Manhattan heuristics |
| 4 | `Week4_NQueens_HillClimbing.ipynb` | Hill climbing for N-Queens |
| 5 | `Week5_NQueens_SimulatedAnnealing.ipynb` | Simulated annealing for 8-Queens |
| 6 | `Week6_PropositionalLogic_TruthTables.ipynb` | Propositional logic, truth tables and entailment |
| 7 | `Week7_FOL_Unification.ipynb` | First-order logic unification |
| 8 | `Week8_FOL_ForwardBackwardChaining.ipynb` | First-order forward and backward chaining |
| 9 | `Week9_FOL_Resolution.ipynb` | First-order resolution and refutation |

## Installation and use

Install Python 3.10 or newer and the notebook dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
jupyter lab
```

Open any notebook in `Notebooks/` and select **Run → Run All Cells**. Programs use the Python standard library. They run sample interactions by default; edit `SAMPLE_INPUTS` to try other values. For live input, remove the sample-input context at the end of a code cell and call `main()` directly.

The notebooks expect custom values such as 8-puzzle tiles, predicate expressions, Horn rules and first-order clauses. They validate the inputs needed by each exercise.

## Screenshots

`screenshot/Week1/` through `screenshot/Week9/` contain PNG captures of each notebook program's code and executed output.

The original presentation files are not included in this repository. The root-level `IBM-Certificate.pdf` is retained.
