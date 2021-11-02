from televisores.tv import *

class Control:
    
    def enlazar(self, tv):
        self.tv = tv
        tv.control = self
        
    def getTv(self):
        return self.tv
    
    def setTv(self, tv):
        self.tv = tv
    
    def turnOn(self):
        self.tv.estado = True
            
    def turnOff(self):
        self.tv.estado = False
    
    def canalUp(self):
        self.tv.canalUp()
        
    def canalDown(self):
        self.tv.canalDown()
                
    def volumenUp(self):
        self.tv.volumenUp()
    
    def volumenDown(self):
        self.tv.volumenDown()
                
    def setCanal(self, canal):
        self.tv.setCanal(canal)
