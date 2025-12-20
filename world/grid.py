
class Grid:
    """
    Grid class managing the spatial grid for the simulation.
    """

    def __init__(width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = {}
        
    def get_cell(self, x: float, y: float) -> Tuple[int, int]:
        return (int(x / self.cell_size), int(y / self.cell_size))
