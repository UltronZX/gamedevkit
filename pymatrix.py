class Matrix():
    def __init__(self,xlen,ylen,valuestr):
        self.create(xlen,ylen,valuestr)
        
    def create(self,xlen,ylen,valuestr):
        # global lst1,temp
        self.xlen = xlen
        self.ylen = ylen
        self.__lst1 = []
        for a in range(ylen):
            for b in range(xlen):
                self.__lst1.append(eval(valuestr))
        self.matrix = self.__lst1
    
    def xy(self,x,y):
        try:
            return self.matrix[x + ((self.ylen - 1 - y)*self.xlen)]
        except:
            return 'error'
    
    def set_xy(self,x,y,value):
        try:
            self.matrix[x + ((self.ylen - 1 - y)*self.xlen)] = value
        except:
            return 'error'
