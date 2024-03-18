class GamePlanBlock:
    def __init__(self, x, y, edges={'top': 'transparent', 'bottom': 'transparent', 'left': 'transparent', 'right': 'transparent'}, artifact=None):
        self.x = x
        self.y = y
        self.edges = edges
        self.artifact = artifact

    def __repr__(self):
        return f"Block({self.x}, {self.y}, edges={self.edges}, artifact={self.artifact})"

    def __str__(self):
        return f"Block on possition {self.x}, {self.y} with edges {self.edges} and artifact {self.artifact}"

class GamePlan:
    def __init__(self):
        self.blocks = {}  # Using a dictionary to store blocks

    def add_block(self, x, y, edges, artifact=None):
        self.blocks[(x, y)] = GamePlanBlock(x, y, edges, artifact)

    def get_block(self, x, y):
        return self.blocks.get((x, y))  # Returns None if block does not exist

    def can_move(self, x, y, direction):
        """
        Returns True if one can move in direction indicated by the direction parameter, otherwise returns False
        Direction can be up, down, left or right
        """
        current_block = self.get_block(x, y)
        if not current_block:
            return False  # No block at the starting coordinates

        # Determine the coordinates of the adjacent block based on the direction
        if direction == 'up':
            adjacent_coords = (x, y-1)
            my_edge, their_edge = 'top', 'bottom'
        elif direction == 'down':
            adjacent_coords = (x, y+1)
            my_edge, their_edge = 'bottom', 'top'
        elif direction == 'left':
            adjacent_coords = (x-1, y)
            my_edge, their_edge = 'left', 'right'
        elif direction == 'right':
            adjacent_coords = (x+1, y)
            my_edge, their_edge = 'right', 'left'
        else:
            raise Exception(f"Invalid direction: {direction}")

        adjacent_block = self.get_block(*adjacent_coords)
        if not adjacent_block:
            return False  # No block in the desired direction

        # Check if both adjacent edges are transparent
        return current_block.edges[my_edge] == 'transparent' and adjacent_block.edges[their_edge] == 'transparent'

    def __repr__(self):
        return f"Surface(blocks={self.blocks})"
