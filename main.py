from connect4_MCTS.simulation import *


if __name__ == '__main__':

    show_match(MCTS(),MCTS())





"""

parameters used for testing:

    params_list = [
    {
        'selection_method': 'random',
        'iterations_per_simulation': 1,
        'max_runtime': 5,
        'cap_method': 'time'
    },

    {
        'selection_method': 'random',
        'iterations_per_simulation': 10,
        'max_runtime': 5,
        'cap_method': 'time'
    },

    {
        'selection_method': 'random',
        'iterations_per_simulation': 100,
        'max_runtime': 5,
        'cap_method': 'time'
    }
]


    params_list = [
    # Low exploration, single simulation per iteration
    {
        'max_iter': 10000,
        'C': 1.0,
        'selection_method': 'uct',
        'iterations_per_simulation': 1
    },

    # High exploration, single simulation per iteration
    {
        'max_iter': 10000,
        'C': None,
        'selection_method': 'random',
        'iterations_per_simulation': 1
    },

    # Random selection, single simulation
    {
        'max_iter': 1000,
        'C': None,
        'selection_method': 'random',
        'iterations_per_simulation': 10
    },

    # Multiple simulations per iteration
    {
        'max_iter': 15000,
        'C': 5.0,
        'selection_method': 'uct',
        'iterations_per_simulation': 50
    },

    # High exploration with multiple simulations
    {
        'max_iter': 20000,
        'C': 20.0,
        'selection_method': 'uct',
        'iterations_per_simulation': 100
    },

    # Random selection with multiple simulations
    {
        'max_iter': 25000,
        'C': None,
        'selection_method': 'random',
        'iterations_per_simulation': 50
    }
]
"""

