import random

class Solution:

    def __init__(self, n_rows, n_cols):
        self.rows = n_rows
        self.cols = n_cols
        self.visit = set()
        
    def flip(self):
        while True:
            r = random.randint(0,self.rows-1)
            c = random.randint(0,self.cols-1)
            if(r,c) not in self.visit:
                self.visit.add((r,c))
                return [r,c]
            
    def reset(self):
        self.visit = set()
