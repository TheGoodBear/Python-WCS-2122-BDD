# coding: utf-8

# imports
from DBUtil import DBUtil
from Models.Vegetal import Vegetal
from Models.Category import Category
from Models.Color import Color
from Models.VegetalColor import VegetalColor


# functions
def Main():
    """
    """
    
    # connect to DB
    DBUtil.Connect("DojoSQL2")
   
    # get data from DB
    DBUtil.GetAllDataFromDB(("Category", "Vegetal", "Color", "VegetalColor"))
 
    # close DB
    DBUtil.Close()
 
    # complete missing data for n-n and recursive relations
    for Element in Vegetal.List:
        Element.Colors = VegetalColor.GetRelation(Element.ID)
    Category.CompleteData()
    
  
    # print model content
    Vegetal.PrintAll()
    Category.PrintAll()
    Color.PrintAll()
    
    # # print specified vegetal
    # print("----------------")
    # Vegetal1 = Vegetal.GetElement(3)
    # print(Vegetal1)
    # Vegetal2 = Vegetal.GetElement(18)
    # print(Vegetal2)
    
    # print vegetals with specified color
    ColorID = None
    while ColorID != "":
        try:
            ColorID = input("\nEntrer l'ID d'une couleur (vide pour quitter) : ")
            ColorID = int(ColorID)
            Colors = VegetalColor.GetRelation(ColorID=ColorID)
            print(f"Liste des végétaux ayant la couleur {Color.GetElement(ColorID).Name} : {', '.join(Colors) if Colors else 'aucune plante de cette couleur'}")
        except:
            if ColorID != "":
                print("Ceci n'est pas un ID")
    
    

# code start
if __name__ == "__main__":
    print("\nDémo Python/Postgre\n")
    Main()
    print("\nAu revoir\n")