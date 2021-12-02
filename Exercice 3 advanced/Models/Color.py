# coding: utf-8

# imports
from Models.StandardModel import StandardModel

# class
class Color(StandardModel):
    """
        Model for color table
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
        """
        
        # call parent constructor
        super().__init__(Data[:2])
        
        # add object to collection
        Color.List.append(self)
        

    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.ID}) {self.Name}"
