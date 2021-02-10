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
        self.fig = None
    
    def AddData(self, data_x, data_y, label="Insérez une légende", model=False):
        if len(data_x) != len(data_y):
            raise ValueError("il doit y avoir le même nombre de données dans chaque argument data")
        if len(self.plotlist) == 6:
            raise IndexError("ce code peut seulement prendre 6 différentes séries de données pour le moment")
        if isinstance(label, str) == False:
            raise TypeError("le label doit être une chaîne de caractères")
        self.plotlist.append((data_x,data_y, label, model))
    
    def Plot(self, MajXTicks = None, MajYTicks = None, MinXTicks = None, MinYTicks =None, AdjustLegend = 1.45):
        Xmax = None
        Ymax = None
        fig,ax = plt.subplots()
        liste_styles = [("o", "k", "k"), ("o", "k", "w"), ("^", "k", "k"), ("^", "k", "w"), ("s", "k", "k"), ("s", "k", "w")]
        for ordre,data in enumerate(self.plotlist):
            if data[3] == True:
                print(data[2])
                plt.plot(data[0], data[1], liste_styles[ordre][0], color = liste_styles[ordre][1], mfc = liste_styles[ordre][2],linestyle='solid', linewidth=2, markersize=1,label=f"{data[2]}")
            else:
                plt.plot(data[0], data[1], liste_styles[ordre][0], color = liste_styles[ordre][1], mfc = liste_styles[ordre][2],label =f"{data[2]}")

            if Xmax == None or max(data[0]) > Xmax:
                Xmax = max(data[0])
            if Ymax == None or max(data[1]) > Ymax:
                Ymax = max(data[1])
        if self.Xunits == False:
            plt.xlabel(f'{self.Xname}',fontsize=12)
        else:
            plt.xlabel(f'{self.Xname} [{self.Xunits}]',fontsize=12)
        if self.Yunits == False:
            plt.ylabel(f'{self.Yname}',fontsize=12)
        else:
            plt.ylabel(f'{self.Yname} [{self.Yunits}]',fontsize=12)
        plt.title(self.Title, fontweight = "bold",fontsize=12)
        plt.legend(loc = "lower right",bbox_to_anchor=(AdjustLegend, 0.1),fancybox=True, shadow=True)
        if MajXTicks != None:
            plt.xticks(np.arange(0,Xmax,MajXTicks))
        if MinXTicks != None:
            ax.set_xticks(np.arange(0,Xmax + Xmax / 20, MinXTicks), minor=True)
        if MajYTicks != None:
            plt.yticks(np.arange(0,Ymax,MajYTicks))
        if MinYTicks != None:
            ax.set_yticks(np.arange(0,Ymax + Ymax / 20, MinYTicks), minor=True)
        plt.show(fig)
        self.fig = fig
    
    def Save(self, name, format = "png", dpival = 600):
        if format == "png":
            self.fig.savefig(f'{name}.png',bbox_inches='tight',dpi=dpival)
        if format == "pdf":
            self.fig.savefig(f"{name}.pdf",bbox_inches='tight')



