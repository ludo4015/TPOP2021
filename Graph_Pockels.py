import numpy as np
from matplotlib import pyplot as plt
from graph_template import GraphTemplate

#data
#Tension (V) : Signal (mV)
"""
15 : 540\\
30 : 520\\
45 : 490\\
60 : 440\\
75 : 405\\
90 : 380\\
105 : 370\\
120 : 290\\
135 : 220\\
150 : 195\\
165 : 160\\
180 : 95\\
195 : 90\\
210 : 30\\
225 : genre 20\\
240 : 10\\
255 : 30\\
270 : 60\\
285 : 80\\
300 : 100\\
315 : 140\\
330 : 180\\
345 : 220\\
360 : 240\\
375 : 360\\
390 : 390
"""
data_x = [15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345,360,375,390]
data_y = [540,520,490,440,405,380,370,290,220,195,160,95,90,30,20,10,30,60,80,100,140,180,220,240,460,390]

Pockels = GraphTemplate(Title = "Signal de la photodiode en fonction de la tension DC appliquée à la cellule de Pockels",
                        Xname = "Tension DC appliquée à la cellule de Pockels",
                        Xunits = "V",
                        Yname = "Signal affiché sur l'oscilloscope",
                        Yunits = False
                        )
Pockels.AddData(data_x, data_y, label="Signal de la photodiode")
Pockels.Plot(MajXTicks=60,MinXTicks=15,MajYTicks=60,MinYTicks=15)
Pockels.Save(name="Pockels1",format="pdf")
