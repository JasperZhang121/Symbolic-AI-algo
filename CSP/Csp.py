from typing import Dict, List, Tuple


def _adjacent_regions_constraint(region1: str, color1: str, region2: str, color2: str) -> bool:
    """
    Check if two adjacent regions have the same color.
    """
    return color1 != color2


class MapColoringCSP:

    def __init__(self, regions: List[str], colors: List[str], neighbors: Dict[str, List[str]]):
        self.variables = regions
        self.domains = {region: colors for region in regions}
        self.neighbors = neighbors
        self.constraints = []

        for region1 in self.variables:
            for region2 in self.neighbors[region1]:
                self.constraints.append((region1, region2, _adjacent_regions_constraint))

    def assign(self, region: str, color: str):
        """
        Assign a color to a region and propagate constraints to its neighbors.
        """
        self.domains[region] = [color]
        for neighbor in self.neighbors[region]:
            if color in self.domains[neighbor]:
                self.domains[neighbor].remove(color)

    def unassign(self, region: str):
        """
        Unassign a color from a region and restore its original domain.
        """
        self.domains[region] = [c for c in self.domains[region] if all(c not in self.domains[neighbor] for neighbor in self.neighbors[region])]

    def is_assigned(self, region: str) -> bool:
        """
        Check if a region has been assigned a color.
        """
        return len(self.domains[region]) == 1

    def is_complete(self) -> bool:
        """
        Check if all regions have been assigned a color.
        """
        return all(self.is_assigned(region) for region in self.variables)

    def get_assignment(self) -> Dict[str, str]:
        """
        Return the current assignment of colors to regions.
        """
        return {region: self.domains[region][0] for region in self.variables if self.is_assigned(region)}

    def get_neighbors(self, region: str) -> List[str]:
        """
        Return the neighbors of a region.
        """
        return self.neighbors[region]

    def get_domain(self, region: str) -> List[str]:
        """
        Return the current domain of colors for a region.
        """
        return self.domains[region]

    def get_variables(self) -> List[str]:
        """
        Return the list of regions.
        """
        return self.variables