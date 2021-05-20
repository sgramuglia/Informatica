class Gorriones:
    def __init__(self):
        #self.kms = kms
        self.maxkms = 0
        self.maxgrs = 0
        self.equilibrio = False

    def CSS(self, kms, gramos):
        if gramos > self.maxgrs:
            self.maxgrs = gramos
        if kms > self.maxkms:
            self.maxkms = kms
        rescss = kms / gramos
        if rescss >= 0.5 and rescss <= 2:
            self.equilibrio = True
        if gramos == 0: 
            return None
        else: 
            return rescss
    
    def CSSP(self):
        if self.maxgrs == 0: 
            return None
        else: 
           return self.maxkms / self.maxgrs
    
    #def CSSV(self):
        #no entendi que se supone que tiene que hacer este
