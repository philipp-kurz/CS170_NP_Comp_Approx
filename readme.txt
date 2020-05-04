Instructions on how to run the different parts of the solver
============================================================

Expected folder format:
/project: Main folder
/project/inputs: Holds all 1006 project input files
/project/outputs: Holds all 1006 project output files


I. Run solver.py on single input file
   >>> python3 solver.py small-1.in

II. Run solver indefinitely on single input file
    >>> python3 run_solver_on_single_input.py small-1.in

III. Run solver on all files in input folder once
     >>> python3 run_solver_on_inputs.py False

III. Run solver on all files in input foler indefinitely
     >>> python3 run_solver_on_inputs.py True

IV. Visualize graph of input
    >>> python3 visualizeGraph.py small-1.in

V. Generate scores.obj file
   >>> python3 generateScores.py

VI. Generate firstPositions.obj file
    >>> python3 parseLeaderboardData.py
    (requires html code of team's leaderboard scores:
     Using Chrome, inspect page's source code and copy entire body element)

VII. Show how often every output file has been updated with a better solution
     >>> python3 viewUpdates.py


