# Artificial Intelligence Lab

This repository contains week-wise Jupyter notebooks for the nine AI lab presentations. The original presentation files are preserved in `PPTs/`. The existing Python exercises and their original `outputs/` files are retained.

## Topics by week

| Week | Topics | Programs |
| --- | --- | ---: |
| 1 | Tic-Tac-Toe game trees and minimax; simple reflex and goal-based vacuum agents | 2 |
| 2 | 8-puzzle Depth-First Search (DFS); Iterative Deepening Search (IDS); BFS theory note | 2 |
| 3 | A* search for the 8-puzzle with misplaced-tile and Manhattan-distance heuristics | 1 (two heuristics) |
| 4 | Hill climbing for the 4-Queens / N-Queens problem | 1 |
| 5 | Simulated annealing for 8-Queens | 1 |
| 6 | Propositional syntax and semantics; truth-table enumeration; all observation-book entailment cases | 2 |
| 7 | First-order logic unification, substitutions and occurs check | 1 |
| 8 | First-order forward chaining and backward chaining for Horn clauses | 2 |
| 9 | First-order logic resolution, clauses, unification and refutation | 1 |

Each notebook explains the theory and objective, lists its imports and algorithm steps, gives complexity where applicable, and includes editable sample inputs, executed output and an explanation of the result. The implementations use Python's standard library; the notebooks retain `input()` calls for custom values.

## Installation

Install Python 3.10 or newer, then install the notebook tools:

```bash
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

The AI programs themselves require no third-party Python packages.

## Run the notebooks

From the project root, start JupyterLab:

```bash
jupyter lab
```

Open a notebook under `Notebooks/` and choose **Run → Run All Cells**. Each program runs a sample interaction by default. Edit the `SAMPLE_INPUTS` list in that program's code cell to try different values. To enter input live, remove the sample-input context at the bottom of the code cell and call `main()` directly.

For the 8-puzzle programs, enter nine numbers from 0 to 8, where 0 is the blank. Week 7 accepts predicate terms such as `Eats(x, Apple)`. Week 8 accepts Horn rules in `premises -> conclusion` form and semicolon-separated facts. Week 9 accepts clauses in disjunction form, with `~` for a negative literal.

## Screenshots

`screenshot/Week1/` through `screenshot/Week9/` contain week-wise PNG captures. Code captures show the notebook implementation; output captures render the corresponding stdout captured from the executed notebook cells. Filenames identify the program and distinguish code from output. The original CLI run screenshots and text transcripts remain in `outputs/`.

## Source presentations

The nine source decks are in `PPTs/Week1.pptx` through `PPTs/Week9.pptx`. `PPTs/Week5-SimulatedAnnealing-Reference.pdf` is the supplied supplementary reading for Week 5.
