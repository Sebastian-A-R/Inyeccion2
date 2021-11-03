
from servicioenvio1 import ServicioEnvio1
from servicioimpre import ServicioImpre
from serviciopdf1 import ServicioPDF1



if __name__ == "__main__":

    servi1=ServicioEnvio1()
    servi2=ServicioPDF1()

    miServi= ServicioImpre(servi1,servi2)
    miServi.imprimir()
