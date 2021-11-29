# coding: utf-8

# imports
import psycopg2


# functions
def Main():
    """
    """
    
    try:
        # step 1 - connect to postgre database
        Connection = psycopg2.connect(
            user="postgres",
            password="AM",
            host="localhost",
            port="5432",
            database="DojoSQL2")
        
        print("Connection réussi\n")
        
        # step 2 - create cursor
        Cursor = Connection.cursor()
        
        # # step 2bis - check database version
        # Query = "SELECT version()"
        # Cursor.execute(Query)
        # Results = Cursor.fetchone()
        # print(Results)
        
        # step 3 - get some data from DB
        Query = "SELECT * from vegetal"
        Cursor.execute(Query)
        Results = Cursor.fetchall()
        # print(Results)
        for Line in Results:
            for Data in Line:
                print(f"{Data} --- ", end="")
            print()
        
        
    except(Exception, psycopg2.Error) as error:
        print(f"Impossible de se connecter à la base Postgre\n{error}")
             
    
       


# code start
if __name__ == "__main__":
    print("\nDémo Python/Postgre\n")
    Main()
    print("\nAu revoir")