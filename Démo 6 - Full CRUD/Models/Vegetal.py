# coding: utf-8

# imports
from Models.StandardModel import StandardModel
from Models.Category import Category


# class
class Vegetal(StandardModel):
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
        self.Image = Data[2]
        self.Comment = Data[3]
        self.CategoryID = Data[4]
        
        # calculated properties
        self.Category = Category.GetElement(self.CategoryID)
        self.Colors = []
                
        # call parent constructor
        super().__init__(Data[:2])
        
        # add object to collection
        Vegetal.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        CategoryNames = Category.GetHierarchyNames(self.Category)
        Comment = f"\n  {self.Comment}" if self.Comment else ""
        Colors = f"{', '.join(self.Colors) if self.Colors else 'aucune couleur associée'}"
        
        return (
            f"({self.ID}) {self.Name}" +
            f"\n  espèce : {CategoryNames}" +
            f"{Comment}" +
            f"\n  couleurs : {Colors}")
