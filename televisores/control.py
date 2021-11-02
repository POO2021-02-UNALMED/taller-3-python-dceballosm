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
        if self.tv.estado == True:
            if self.tv.canal < 120:
                self.tv.canal = self.tv.canal + 1
        
    def canalDown(self):
        if self.tv.estado == True:
            if self.tv.canal > 1:
                self.tv.canal = self.tv.canal - 1
                
    def volumenUp(self):
        if self.tv.estado == True:
            if self.tv.volumen < 7:
                self.tv.volumen = self.tv.volumen + 1
    
    def volumenDown(self):
        if self.tv.estado == True:
            if self.tv.volumen > 1:
                self.tv.volumen = self.tv.volumen - 1
                
    def setCanal(self, canal):
        if isinstance(canal, int):
            if self.tv.estado == True:
                if (canal<120) & (canal>1): 
                    self.tv.canal = canal
                    
        else:
            raise TypeError("Expected int")
