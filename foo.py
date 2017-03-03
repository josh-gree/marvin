class dir_array(object):

    def __init__(self):
        self.deg = []
        self.dir = []
        
        for i in range(360):
            self.deg.append(i)
        
        for d in self.deg:
            pass

    def boo(self):
        print(self.deg)
    
    def __len__(self):
        return 999

    def __add__(self,other):
        

new_dir = dir_array()
new_dir2 = dir_array()

print(new_dir.deg)

print(len(new_dir))

print(new_dir + new_dir2)
