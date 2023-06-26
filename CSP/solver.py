from typing import Dict
from CSP.Csp import MapColoringCSP, _adjacent_regions_constraint
from CSP.Inference import AC_3


def backtrack(assignment: Dict[str, str], csp: MapColoringCSP) -> Dict[str, str]:
    """
    Perform a backtracking search to solve the map-coloring CSP.
    """
    if csp.is_complete():
        return assignment

    # Select unassigned region with the fewest legal colors (Minimum Remaining Values heuristic)
    unassigned = [v for v in csp.get_variables() if v not in assignment]
    region = min(unassigned, key=lambda region: len(csp.get_domain(region)))

    for color in csp.get_domain(region):
        if is_valid_assignment(csp, assignment, region, color):
            csp.assign(region, color)
            assignment[region] = color

            result = backtrack(assignment, csp)

            if result is not None:
                return result

            csp.unassign(region)
            assignment.pop(region)

    return None


def is_valid_assignment(csp: MapColoringCSP, assignment: Dict[str, str], region: str, color: str) -> bool:
    """
    Check if the current assignment is valid.
    """
    for neighbor in csp.get_neighbors(region):
        if neighbor in assignment and not _adjacent_regions_constraint(region, color, neighbor, assignment[neighbor]):
            return False

    return True


def backtrack_AC_3(assignment: Dict[str, str], csp: MapColoringCSP) -> Dict[str, str]:
    """
    Perform a backtracking search to solve the map-coloring CSP.
    """

    # Apply AC-3 as a preprocessing step
    for region in csp.get_variables():
        if not AC_3(region, csp.get_domain(region)[0], csp):
            return None  # If AC-3 returns False, return None because there's no solution

    if csp.is_complete():
        return assignment

    # Select unassigned region with the fewest legal colors (Minimum Remaining Values heuristic)
    unassigned = [v for v in csp.get_variables() if v not in assignment]
    region = min(unassigned, key=lambda region: len(csp.get_domain(region)))

    for color in csp.get_domain(region):
        if is_valid_assignment(csp, assignment, region, color):
            csp.assign(region, color)
            assignment[region] = color

            result = backtrack(assignment, csp)

            if result is not None:
                return result

            csp.unassign(region)
            assignment.pop(region)

    return None
