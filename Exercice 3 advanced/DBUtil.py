# coding: utf-8

# imports
import psycopg2

from Models.Vegetal import Vegetal
from Models.Category import Category
from Models.Color import Color
from Models.VegetalColor import VegetalColor


# class
class DBUtil:
    
    Connection = None
    
    @classmethod
    def Connect(
        cls, 
        DBName: str):
        """
            Connect to named Postgre database
            
            Args :
                DBName : database name
        """
        
        try:
            cls.Connection = psycopg2.connect(
                user="postgres",
                password="AM",
                host="localhost",
                port="5432",
                database=DBName)
                    
        except(Exception, psycopg2.Error) as error:
            print(f"Impossible de se connecter à la base Postgre {DBName}\n{error}")


    @classmethod
    def ExecuteQuery(
        cls,
        Query: str,
        Values: tuple = None) -> list[tuple]:
        """
            Execute specified query

            Args:
                Query : Query to execute
                
            Returns a list of tuples
        """

        if cls.Connection is None:
            return

        try:
            # get cursor
            Cursor = cls.Connection.cursor()
            
            # execute query
            Cursor.execute(Query, Values)
            
            if Query.upper().startswith("SELECT "):
                # Query = "SELECT * FROM color"
                Results = Cursor.fetchall()
            else:
                # Query = "INSERT INTO color (name) VALUES (v1)"
                # Query = "UPDATE color SET (name=v1) WHERE id=v"
                # Query = "DELETE FROM color WHERE id=vid"
                # # NE PAS FAIRE !!!
                    # v1 = "toto"
                    # vid = 5
                    # Query = f"UPDATE color SET (name={v1}) WHERE id={vid}"
                # FAIRE
                    # Query = "UPDATE color SET (name=%s) WHERE id=%s"
                    # Values = (v1, vid)
                
                Results = cls.Connection.commit()
                # print(f"Commit results : {Results}")
            
            # close cursor
            Cursor.close()

            # return results
            return Results
        
        except:
            print(f"\nERREUR lors de l'exécution de la requête\n{Query}")

    @classmethod
    def GetAllDataFromDB(cls,
        Models: tuple[str],
        OrderBy: tuple[str] = None):
        """
            Get all data with standard SQL queries to fill local model lists

            Args:
                Models : list of models to fill in order
        """
        
        for index, Model in enumerate(Models):
            Query = f"SELECT * FROM {Model.lower()}"
            if OrderBy is not None and OrderBy[index]:
                Query += f" ORDER BY {OrderBy[index]}"
            cls.FillModelCollection(Query, eval(Model))


    @classmethod
    def FillModelCollection(
        cls,
        Query: str,
        Model: object):
        """
            Fill model collection from SQL query
            
            Args :
                Query : SQL query
                Model : model to fill
        """
        
        # get data from query
        Results = cls.ExecuteQuery(Query)  
            
        # create model collection
        for Line in Results:
            Model(Line)
        

    @staticmethod
    def PrintResults(
        Results: list[tuple], 
        Separator: str = ", "):
        """
            Print list of tuples

            Args:
                Results : data to print
                Separator : separator for tuples
        """
        
        if Results is None:
            return

        for Line in Results:
            for Data in Line:
                print(f"{Data}{Separator}", end="")
            print()


    @classmethod
    def Close(cls):
        """
            Free resources
        """
        
        cls.Connection.close()
        