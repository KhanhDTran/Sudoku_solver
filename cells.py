class Cell():

    def __init__(self, ordinal, row, column, x, y):
        self.ordinal = ordinal
        self.row = row
        self.column = column
        self.x = x
        self.y = y
        self.number = 0
        self.block = 0
        self.potential = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.eliminate = []
        self.clue = False
        self.chosen = False
        
        self.width = 0
        self.height = 0
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0