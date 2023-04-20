from Csp import MapColoringCSP


def MRV(csp: MapColoringCSP):
    """
    Select the next unassigned variable with the minimum remaining values (MRV).
    :param csp: MapColoringCSP
    """
    unassigned = [var for var in csp.variables if not csp.is_assigned(var)]
    if not unassigned:
        return None
    return min(unassigned, key=lambda var: len(csp.domains[var]))


def select_variable_md(csp: MapColoringCSP):
    variables = csp.get_variables()
    max_var = None
    max_degree = -1

    for var in variables:
        if not csp.is_assigned(var):
            degree = len([n for n in csp.get_neighbors(var) if not csp.is_assigned(n)])
            if degree > max_degree:
                max_var = var
                max_degree = degree
    return max_var
