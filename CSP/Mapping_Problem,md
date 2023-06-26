# Map Coloring Constraint Satisfaction Problem (CSP)

This repository provides a solution for the classic Constraint Satisfaction Problem (CSP) of map coloring. The problem is defined specifically on the map of Australia, but the solver can be adapted for any map. In a map coloring problem, the goal is to assign colors to regions of a map such that no two adjacent regions share the same color.

## Structure

The project consists of the following main components:

1. **map_coloring_csp.py**: This file defines the MapColoringCSP class, encapsulating the map coloring problem. It includes the regions to be colored, the available colors, and the constraints (i.e., which regions are neighbors and cannot share the same color). The class offers methods to assign and unassign colors to regions, check if an assignment is complete, among others.

2. **backtrack.py**: This file contains the `backtrack` function, which solves the map coloring problem using backtracking search.

3. **Inference.py**: This file features the `AC_3` function, which performs an arc consistency check to enhance the efficiency of the backtracking search.

4. **heuristic.py**: This file includes the `MRV` heuristic function, which uses the Minimum Remaining Values (MRV) heuristic to select the variable to be assigned next.

## Usage

Here's an example on how to use the program:

```python
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
colors = ['red', 'green', 'blue',]
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}
csp = Csp.MapColoringCSP(regions, colors, neighbors)

# Using basic backtracking
assignment = {}
result = backtrack(assignment, csp)
print(result)

# Using AC-3 backtracking
csp = Csp.MapColoringCSP(regions, colors, neighbors)
assignment = {}
result = backtrack_AC_3(assignment, csp)
print(result)
