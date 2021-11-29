# coding: utf-8

# imports
from DBUtil import DBUtil
from Vegetal import Vegetal


# functions
def Main():
    """
    """
    
    # connect to DB
    DBUtil.Connect("DojoSQL2")
    
    # get vegetals
    Query = "SELECT * FROM vegetal"
    Results = DBUtil.ExecuteQuery(Query)
        
    # create vegetal collection
    for Line in Results:
        Vegetal(
            Line[0], 
            Line[1], 
            Line[2], 
            Line[3], 
            Line[4])
    
    # print model content
    for Element in Vegetal.List:
        print(Element)
             
    
    

# code start
if __name__ == "__main__":
    print("\nDémo Python/Postgre\n")
    Main()
    print("\nAu revoir\n")