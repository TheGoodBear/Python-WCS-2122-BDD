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
        Query: str) -> list[tuple]:
        """
            Execute specified query

            Args:
                Query : Query to execute
                
            Returns a list of tuples
        """

        if cls.Connection is None:
            return

        # get cursor
        Cursor = cls.Connection.cursor()
        
        # execute query
        Query = Query
        Cursor.execute(Query)
        Results = Cursor.fetchall()
        
        # close cursor
        Cursor.close()

        # return results
        return Results


    @classmethod
    def GetAllDataFromDB(cls,
        Models: tuple[str]):
        """
            Get all data with standard SQL queries to fill local model lists

            Args:
                Models : list of models to fill in order
        """
        
        for Model in Models:
            cls.FillModelCollection(f"SELECT * FROM {Model.lower()}", eval(Model))


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
        