from televisores.marca import *
from televisores.control import *

class TV:
	
    numTV = 0      

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.numTV += 1
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        TV.numTV = TV.numTV + 1

    def getNumTV():
        return TV.numTV
        
    def getMarca(self):
        return self.marca

    def getControl(self):
        return self.control
    
    def getPrecio(self):
        return self.precio
    
    def getVolumen(self):
        return self.volumen
    
    def getCanal(self):
        return self.canal
    
    def setMarca(self, marca):
        self.marca = marca
        
    def setControl(self, control):
        self.control = control
        
    def setPrecio(self, precio):
        self.precio = precio
        
        
    def setVolumen(self, volumen):
       if self.estado == True:
           if (volumen<=7) & (volumen>=1):
               self.volumen = volumen
                
    
    def setCanal(self, canal):
        if self.estado == True:
            if (canal<=120) & (canal>=1): 
                self.canal = canal

        
    def getNumTV():
        return TV.numTV

    def setNumTV(numTV):
        TV.numTV = numTV
    
    def turnOn(self):
        self.estado = True
            
    def turnOff(self):
        self.estado = False
    
    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.estado == True:
            if self.canal < 120:
                self.canal = self.canal + 1
        
    def canalDown(self):
        if self.estado == True:
            if self.canal > 1:
                self.canal = self.canal - 1
        
    def volumenUp(self):
        if self.estado == True:
            if self.volumen < 7:
                self.volumen = self.volumen + 1
    
    def volumenDown(self):
        if self.estado == True:
            if self.volumen > 1:
                self.volumen = self.volumen - 1
    
