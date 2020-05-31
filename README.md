# Approximation for NP Complete problem (UC Berkeley CS170 final project)
Approximation algorithms to find a close to optional solution for 1000 inputs to an NP Complete problem. Final project for CS170 - "Efficient Algorithms and Intractable Problems" at UC Berkeley during the Spring 2020 semester.

General task was to find a tree-shaped dominating set in 1007 weighted directed graphs with up to 25, 50 and 100 vertices while minimizing the average pairwise distance between the vertices in the set.

The code was written from scratch. The project makes use of the NetworkX python library simplify graph algorithms. Note that this was a quick and dirty implementation, aimed to get as much progress in little time during the final exam period. It also relies on quite a bit of randomization to not get stuck in the same local minimum every time, and was hence run around the clock for more than a week.

> You are an engineer at HorizonWireless, a telecommunications company, and the CEO has tasked you with designing
a cell tower network which spans the major cities of the United States. You need to decide which cities to build cell
towers in and lay out the fiber network between cities.

[Project specifications as PDF](https://github.com/philipp-kurz/CS170_NP_Comp_Approx/files/4707438/spec.pdf)
