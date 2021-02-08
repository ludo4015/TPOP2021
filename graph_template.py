import numpy as np
from matplotlib import pyplot as plt

class GraphTemplate:
    
    def __init__(self, Title="insérer un Titre", Xname="insérer un nom d'axe", Xunits = "unités", Yname="insérer un nom d'axe", Yunits = "unités"):
        self.Title = Title
        self.Xname = Xname
        self.Xunits = Xunits
        self.Yunits = Yunits
        self.Yname = Yname
        self.plotlist = []
    
    def AddData(self, data_x, data_y, label):
        if len(data_x) != len(data_y):
            raise ValueError("il doit y avoir le même nombre de données dans chaque argument data")
        if len(self.plotlist) == 6:
            raise IndexError("ce code peut seulement prendre 6 différentes séries de données pour le moment")
        if isinstance(label, str) == False:
            raise TypeError("le label doit être une chaîne de caractères")
        self.plotlist.append((data_x,data_y, label))
    
    def Plot(self):
        liste_styles = [("o", "k", "k"), ("o", "k", "w"), ("^", "k", "k"), ("^", "k", "w"), ("s", "k", "k"), ("s", "k", "w")]
        for ordre,data in enumerate(self.plotlist):
            plt.plot(data[0], data[1], liste_styles[ordre][0], color = liste_styles[ordre][1], mfc = liste_styles[ordre][2],label =f"{data[2]}")
        plt.xlabel(f'{self.Xname} [{self.Xunits}]')
        plt.ylabel(f'{self.Yname} [{self.Yunits}]')
        plt.title(self.Title)
        plt.legend(loc = "lower right")
        plt.show()

Test = GraphTemplate()
Test.AddData([1,2,3,4,5],[1,2,3,4,5],"label1")
Test.AddData([2,3,4,5,6],[1,2,3,4,5],"label2")
Test.AddData([3,4,5,6,7],[1,2,3,4,5],"label3")
Test.AddData([4,5,6,7,8],[1,2,3,4,5],"label4")
Test.AddData([5,6,7,8,9],[1,2,3,4,5],"label5")
Test.AddData([6,7,8,9,10],[1,2,3,4,5],"label6")
Test.Plot()
        