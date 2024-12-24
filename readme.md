# Connect4 with Bitboard Representation and MCTS

This project implements a Connect4 game using a bitboard representation for efficient game state management. The AI for the game is built using the Monte Carlo Tree Search (MCTS) algorithm. The repository is structured to allow for easy experimentation and includes features for running matches, visualizing gameplay, and conducting tournaments.

---
## Table of Contents

## Features

- **Bitboard Representation**: Efficiently encodes game states using binary operations.
- **Monte Carlo Tree Search (MCTS)**: Implements an AI player for Connect4.
- **Game Visualization**: Uses Pygame to display the Connect4 grid and gameplay.
- **Tournament Simulation**: Allows multiple AI configurations to compete against each other.
- **Parallel Execution**: Leverages Python's `concurrent.futures` for running matches in parallel.

---

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/beloof/connect4_MCTS
   ```
2. Install dependencies:
   ```
   cd connect4_MCTS
   pip install .
   ```

---

## Usage

### Running a Match
To play a single match between two AI players:
```
from connect4_MCTS import show_match
show_match(MCTS(), MCTS())
```

### Tournament Simulation
To run a tournament among multiple AI configurations:
```
from connect4_MCTS import tournament

params_list = [
    {
        'selection_method': 'random',
        'iterations_per_simulation': 1,
        'runtime': 5,
        'cap_method': 'time'
    },
    {
        'selection_method': 'uct',
        'iterations_per_simulation': 100,
        'runtime': 10,
        'cap_method': 'iterations'
    }
]

tournement(params_list)
```

### Visualizing Matches
To visualize gameplay between two AI players:
```
from connect4_MCTS import show_match, MCTS
show_match(MCTS(),MCTS())
```
![image](/images/Screenshot.png)
---

## File Structure

```
.
├── connect4_MCTS/
│   ├── __init__.py          
│   ├── bitboard.py          # Bitboard implementation for Connect4
│   ├── simulation.py        # basic functions to show/play matches
│   └── MCTS_bitboard.py     # MCTS algorithm implementation
├── docs/                    # html documentation
├── images/                  # readme image
├── results/                 # readme image
│   └── study.pdf            # final thoughts/results
├── main.py                  # Main script for running matches and tournaments
├── setup.py                 # Python setup file
└── README.md                # Documentation
```

---

## How It Works

### Bitboard Representation
The game board is represented as a 7x6 grid encoded into a 49-bit integer for each player. Binary operations are used to calculate valid moves, check for wins, and update game states efficiently.

The positions on the board are as follows:
```
.  .  .  .  .  .  .
5 12 19 26 33 40 47
4 11 18 25 32 39 46
3 10 17 24 31 38 45
2  9 16 23 30 37 44
1  8 15 22 29 36 43
0  7 14 21 28 35 42 
```

check [this](http://blog.gamesolver.org/solving-connect-four/06-bitboard/) for more detail
### Monte Carlo Tree Search (MCTS)
The MCTS algorithm uses the following steps to determine the best move:
1. **Selection**: Traverses the game tree using a selection strategy (e.g., UCT).
2. **Expansion**: Adds a new node to the tree.
3. **Simulation**: Simulates random playouts from the new node.
4. **Backpropagation**: Updates the node values based on the simulation outcomes.

### Tournament Simulation
A tournament is run by pairing different AI configurations and letting them play multiple matches. Results are saved in `.npy` and `.txt` formats for analysis.

---

## Dependencies

- `pygame`
- `numpy`
- `matplotlib`

Install dependencies using:
```
pip install .
```
---
## Documentation

Full documentation [here](https://github.com/beloof/connect4_MCTS/tree/master/docs/build/html)
 
---

## Future Work
- Add a human vs. AI mode.
- Implement advanced heuristics for MCTS simulations.
- Enhance visualization with real-time statistics.
- Optimize bitboard operations for larger grids.
---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
Special thanks to [PascalPons](http://blog.gamesolver.org/solving-connect-four/06-bitboard/) and [Qi Wang](https://www.harrycodes.com/blog/monte-carlo-tree-search) for sharing insights

