from Csp import MapColoringCSP


def Ar_3(region: str, color: str, gamma: MapColoringCSP) -> bool:
    """Perform arc consistency check (AC-3) on a MapColoringCSP object using Ar_3 algorithm.

    Args:
        region (str): The name of the region to check arc consistency for.
        color (str): The name of the color to check arc consistency for.
        gamma (MapColoringCSP): The MapColoringCSP object to perform AC-3 on.

    Returns:
        bool: True if the MapColoringCSP is arc consistent after the check, False otherwise.
    """

    # Initialize queue with all arcs emanating from `region`
    queue = [(neighbour, region) for neighbour in gamma.neighbors[region]]

    # Continue until there are no more arcs to process
    while queue:
        # Pop the first arc from the queue
        neigh, regi = queue.pop(0)

        # Perform arc consistency check for the popped arc
        revised = revise(neigh, regi, gamma)

        # Check if the domain of `neigh` is empty after the arc consistency check
        if not gamma.domains[neigh]:
            return False

        # If the domain of `neigh` has been revised, add all arcs emanating from `neigh` to the queue
        if revised:
            queue.extend([(neighbour, neigh) for neighbour in gamma.neighbors[neigh] if neighbour != regi])

    # The MapColoringCSP is arc consistent
    return True


def revise(neigh: str, regi: str, gamma: MapColoringCSP) -> bool:
    """Make variable `neigh` arc consistent with variable `regi` in the MapColoringCSP.

    Args:
        neigh (str): The name of the variable to make arc consistent with `regi`.
        regi (str): The name of the variable to make arc consistent with `neigh`.
        gamma (MapColoringCSP): The MapColoringCSP object.

    Returns:
        bool: True if the domain of `neigh` has been revised, False otherwise.
    """

    revised = False

    # Loop over all values in the domain of `neigh`
    for x in gamma.domains[neigh]:
        satisfies = False

        # Loop over all values in the domain of `regi`
        for y in gamma.domains[regi]:
            # Check if there is at least one constraint between `x` and `y`
            satisfies |= any(gamma.constraints(neigh, x, regi, y))

        # If there is no value in the domain of `regi` that satisfies the constraint between `x` and `y`,
        # remove `x` from the domain of `neigh`
        if not satisfies:
            gamma.domains[neigh].remove(x)
            revised = True

    return revised

