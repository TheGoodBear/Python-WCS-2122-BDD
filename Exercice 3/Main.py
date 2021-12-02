# coding: utf-8

# imports
from DBUtil import DBUtil
from Vegetal import Vegetal
from Category import Category
from Color import Color
from VegetalColor import VegetalColor


# functions
def Main():
    """
    """
    
    # connect to DB
    DBUtil.Connect("DojoSQL2")
   
    # get data from DB
    DBUtil.FillModelCollection("SELECT * FROM category", Category)
    DBUtil.FillModelCollection("SELECT * FROM vegetal", Vegetal)
    DBUtil.FillModelCollection("SELECT * FROM color", Color)
    DBUtil.FillModelCollection("SELECT * FROM vegetalcolor", VegetalColor)
 
    # close DB
    DBUtil.Close()
 
    # complete missing data for n-n relations
    for Element in Vegetal.List:
        Element.Colors = VegetalColor.GetRelation(Element.ID)
    Category.CompleteData()
    
  
    # print model content
    PrintCollection(Vegetal)
    PrintCollection(Category)
    PrintCollection(Color)
    PrintCollection(VegetalColor)
    
    # print specified vegetal
    print("----------------")
    Vegetal1 = Vegetal.GetElement(3)
    print(Vegetal1)
    Vegetal2 = Vegetal.GetElement(18)
    print(Vegetal2)
    
    # print vegetals with specified color
    ColorID = None
    while ColorID != "":
        try:
            ColorID = input("\nEntrer l'ID d'une couleur (vide pour quitter) : ")
            ColorID = int(ColorID)
            print(f"Liste des végétaux ayant la couleur {Color.GetElement(ColorID).Name} : {', '.join(VegetalColor.GetRelation(ColorID=ColorID))}")
        except:
            if ColorID != "":
                print("Ceci n'est pas un ID")
   
    
    
def PrintCollection(Model: object):
    """
        Print collection

        Args:
            Model : model colelction to print  
    """
    
    for Element in Model.List:
        print(Element)
    print()
    
    

# code start
if __name__ == "__main__":
    print("\nDémo Python/Postgre\n")
    Main()
    print("\nAu revoir\n")