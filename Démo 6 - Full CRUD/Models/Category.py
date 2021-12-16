# coding: utf-8

# imports
from Models.StandardModel import StandardModel

# class
class Category(StandardModel):
    """
        Model for category table
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
                    ParentCategoryID : foreign key to Category model (recursive)
        """
        
        # native properties
        self.ParentCategoryID = Data[2]
        
        # calculated properties
        self.ParentCategory = None
        
        # call parent constructor
        super().__init__(Data[:2])
        
        # add object to collection
        Category.List.append(self)
        


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.ID}) {self.Name} {'(enfant de ' + str(self.ParentCategoryID) + ')' if self.ParentCategoryID else ''}"


    def GetHierarchyNames(self,
        Separator = " → ") -> str:
        """
            Get all names for parent elements
            
            Args:
                Separator: separator for names

            Returns:
                str: a string containing all names separated by separator
        """
        
        Result = self.Name
        
        CurrentCategory = self
        while CurrentCategory.ParentCategoryID:
            CurrentCategory = Category.GetElement(CurrentCategory.ParentCategoryID)
            Result += f"{Separator}{CurrentCategory.Name}"
            
        return Result
        

    @classmethod
    def CompleteData(cls):
        """
            Complete calculated properties
        """
        
        for Element in cls.List:
            Element.ParentCategory = cls.GetElement(Element.ParentCategoryID)
