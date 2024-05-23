class shapes():
    def __init__(self):
        pass


    def calc_area(self):
        pass


    def calc_perimeter(self):
        pass
    

class rectangle(shapes):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def calc_area(self):
        return super().calc_area()
    
    def calc_perimeter(self):
        return super().calc_perimeter()







