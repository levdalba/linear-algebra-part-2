import numpy as np
import os
import json_tricks

from pathlib import Path

home_dir = Path(__file__).parent.resolve()

answer = {
    "task1": {
        "det_A_terms": sorted([
            ### YOUR CODE HERE ###
            [1, -1]
        ]),
        "det_A_1_terms": sorted([
            ### YOUR CODE HERE ###
            [-2.0, 0]
        ]),
        "det_A_2_terms": sorted([
            ### YOUR CODE HERE ###
            [-2, 0]
        ]),
        "x": np.array(
            ### YOUR CODE HERE ###
            [1, 1]
        ),
        "cofactors": np.array(
            ### YOUR CODE HERE ###
            [[-1.0, -1.0], 
            [-1.0, 1.0]]
        ),
        "inverse": np.array(
            ### YOUR CODE HERE ###
            [[0.5, 0.5], 
            [0.5, -0.5]]
        )
    },
    "task2": {
        "det_A_terms": sorted([
            ### YOUR CODE HERE ###
            [2, 3]
        ]),
        "det_A_1_terms": sorted([
            ### YOUR CODE HERE ###
            [2, 8]
        ]),
        "det_A_2_terms": sorted([
            ### YOUR CODE HERE ###
            [-3, 8]
        ]),
        "x": np.array(
            ### YOUR CODE HERE ###
            [2.0, 1.0]
        ),
        "cofactors": np.array(
            ### YOUR CODE HERE ###
            [[2.0, -3.0], [1.0, 1.0]]
        ),
        "inverse": np.array(
            ### YOUR CODE HERE ###
            [[0.4, 0.2], [-0.6, 0.2]]
        )
    },
    "task3": {
        "det_A_terms": sorted([
            ### YOUR CODE HERE ###
            [-6, -2, -2, 1, 2, 3]
        ]),
        "det_A_1_terms": sorted([
            ### YOUR CODE HERE ###
            [-12, -4, 0, 0, 3, 9]
        ]),
        "det_A_2_terms": sorted([
            ### YOUR CODE HERE ###
            [-9, -4, 0, 0, 3, 6]
        ]),
        "x": np.array(
            ### YOUR CODE HERE ###
            [1, 1.0, -0.0]
        ),
        "cofactors": np.array(
            ### YOUR CODE HERE ###
            [[-8, 1.0, 3],
            [-0.0, 1.0, -1.0],
            [4.0, -2.0, -2.0]]
        ),
        "inverse": np.array(
            ### YOUR CODE HERE ###
            [[2.0, 0.0, -1.0],
             [-0.25, -0.25, 0.5],
             [-0.75, 0.25, 0.5]]
        )
    }
}

json_tricks.dump(
    answer, 
    open(home_dir/Path('.answer.json'), "w+"))