# coding: utf-8

# imports
from DBUtil import DBUtil
from Vegetal import Vegetal
from Category import Category


# functions
def Main():
    """
    """
    
    # connect to DB
    DBUtil.Connect("DojoSQL2")
   
    # get categories
    DBUtil.FillModelCollection("SELECT * FROM category", Category)
    DBUtil.FillModelCollection("SELECT * FROM vegetal", Vegetal)
 
    # close DB
    DBUtil.Close()
  
    # print model content
    PrintCollection(Vegetal)
    PrintCollection(Category)
   
    
    
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