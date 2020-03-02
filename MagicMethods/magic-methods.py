class Box():
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth
        self.area = width * depth
    
    def __str__(self):
        return 'Box height: {}, width: {}, depth: {}'.format(self.height, self.width, self.depth)
        

if __name__ == "__main__":
    box = Box(2, 4, 5)
    print(box)