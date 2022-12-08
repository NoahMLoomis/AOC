class Highest:
    def __init__(self):
        self.highest_score = 0
        self.f = open("data/day8.txt")
        self.grid = [i[:-1] for i in self.f.readlines()]
        self.trees_count = len(self.grid)*2 + len(self.grid[0])*2 - 4
        
        
    def run(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                # Boundaries
                if row != 0 and row != len(self.grid)-1 and col != 0 and col != len(self.grid[0])-1:
                    tree = int(self.grid[row][col])
                    if self.is_tree_visible(tree, row, col):
                        self.trees_count += 1
                        
                        
    def is_tree_visible(self, tree, row, col):
        # This is really dumb
        tree_visible_left = False
        tree_visible_top = False
        tree_visible_right = False
        tree_visible_bottom = False
        
        left_multiplier = 0
        top_multiplier = 0
        right_multiplier = 0
        bottom_multiplier = 0

        for row_above in range(row):
            grid_item = int(self.grid[row_above][col])
            if grid_item < tree:
                tree_visible_top = True
                top_multiplier += 1
            else:
                tree_visible_top = False
        for col_to_left in range(col):
            grid_item = int(self.grid[row][col_to_left])
            if grid_item < tree:
                tree_visible_left = True
                left_multiplier += 1
            else:
                tree_visible_left = False
        for row_below in range(row + 1, len(self.grid)):
            grid_item = int(self.grid[row_below][col])
            if grid_item < tree:
                tree_visible_bottom = True
                bottom_multiplier += 1
            else:
                tree_visible_bottom = False
        for col_to_right in range(col + 1, len(self.grid[0])):
            grid_item = int(self.grid[row][col_to_right])
            if grid_item < tree:
                tree_visible_right = True
                right_multiplier += 1
            else:
                tree_visible_right = False

        if top_multiplier * bottom_multiplier * left_multiplier * right_multiplier > self.highest_score:
            self.highest_score = top_multiplier * bottom_multiplier * left_multiplier * right_multiplier
            
        return tree_visible_bottom or tree_visible_right or tree_visible_top or tree_visible_left


h = Highest()
h.run()
print(h.highest_score)