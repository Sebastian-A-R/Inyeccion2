from servicioenvio1 import ServicioEnvio1
from serviciopdf1 import ServicioPDF1

class ServicioImpre:

    #servicioA = ServicioEnvio1()
    #servicioB = ServicioPDF1()

    def __init__(self,servicioA,servicioB):
        self._servicioA=servicioA
        self._servicioB=servicioB

    @property
    def servicioA(self):
        return self._servicioA

    @servicioA.setter
    def setServicioA(self,servicioA):
        self._servicioA=servicioA

    @property
    def servicioB(self):
        return self._servicioB

    @servicioB.setter
    def setServicioB(self,servicioB):
        self._servicioB=servicioB


    def imprimir(self):
        self.servicioA.enviar()
        self.servicioB.pdf()