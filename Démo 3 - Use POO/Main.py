# coding: utf-8

# imports
from DBUtil import DBUtil


# functions
def Main():
    """
    """
    
    DBUtil.Connect("DojoSQL2")
    Query = "SELECT * FROM vegetal"
    Results = DBUtil.ExecuteQuery(Query)
    DBUtil.PrintResults(Results)
    
    
# code start
if __name__ == "__main__":
    print("\nDémo Python/Postgre\n")
    Main()
    print("\nAu revoir\n")