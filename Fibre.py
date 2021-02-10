import numpy as np
from matplotlib import pyplot as plt
from graph_template import GraphTemplate

div = 0.00065
f = 0.0045
lambd = 0.0000006328
w0 = 0.000315
z = np.linspace(0,1,1000)
def T(x):
    w1 = (lambd*f)/(np.pi*(w0*np.sqrt(1+(x*div/w0)**2)))
    return (2*w1*0.000002204/(w1**2 + 0.000002204**2))
intensité = []
for el in z:
    intensité.append(T(el))

Fibre = GraphTemplate(Title = "Taux d'intensité en fonction de la distance Z",
                        Xname = "Tension DC appliquée à la cellule de Pockels",
                        Xunits = "V",
                        Yname = "Signal affiché sur l'oscilloscope",
                        Yunits = False
                        )
Fibre.AddData(z, intensité,"intensité T",model=True)
Fibre.Plot(AdjustLegend=1.27)
Fibre.Save("fibre",format="pdf")