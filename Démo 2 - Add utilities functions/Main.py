# coding: utf-8

# imports
import psycopg2


# functions
def Main():
    """
    """
    
    Connection = DBConnect("DojoSQL2")
    Query = "SELECT * FROM vegetal"
    Results = ExecuteQuery(Query, Connection)
    PrintResults(Results)
    
             
    
def DBConnect(DBName: str) -> object:
    """
        Connect to named Postrgre database
        and return connection object
    """
    
    try:
        Connection = psycopg2.connect(
            user="postgres",
            password="AM",
            host="localhost",
            port="5432",
            database=DBName)
    
        return Connection
        
    except(Exception, psycopg2.Error) as error:
        print(f"Impossible de se connecter à la base Postgre {DBName}\n{error}")


def ExecuteQuery(
    Query: str, 
    Connection: object) -> list[tuple]:
    """
        Execute specified query

        Args:
            Query : Query to execute
            Connection : DB connection
            
        Returns a list of tuples
    """

    # get cursor
    Cursor = Connection.cursor()
    
    # execute query
    Query = Query
    Cursor.execute(Query)
    Results = Cursor.fetchall()
    
    # return results
    return Results


def PrintResults(
    Results: list[tuple], 
    Separator: str = ", "):
    """
        Print list of tuples

        Args:
            Results : data to print
            Separator : separator for tuples
    """

    for Line in Results:
        for Data in Line:
            print(f"{Data}{Separator}", end="")
        print()
    

# code start
if __name__ == "__main__":
    print("\nDémo Python/Postgre\n")
    Main()
    print("\nAu revoir\n")