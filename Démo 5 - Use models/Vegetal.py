# coding: utf-8

# imports
from Category import Category


# class
class Vegetal:
    """
        Model for vegetal table
    """
    
    # class properties
    List = []
    
    # methods
    def __init__(self, 
        Data: tuple):
        """
            Constructor

            Args:
                Data : contains all columns
                    ID : primary key
                    Name : name
                    Image : image URL
                    Comment : comments
                    CategoryID : foreign key to Category model
        """
        
        # model properties
        self.ID = Data[0]
        self.Name = Data[1]
        self.Image = Data[2]
        self.Comment = Data[3]
        self.CategoryID = Data[4]
        
        # calculated properties
        self.CategoryName = [
            Element.Name 
            for Element 
            in Category.List 
            if Element.ID == self.CategoryID][0]
        
        # add object to collection
        Vegetal.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.ID}) {self.Name} (famille des {self.CategoryName}){' ' + self.Comment if self.Comment else ''}"
