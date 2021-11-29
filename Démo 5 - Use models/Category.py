# coding: utf-8

# imports

# class
class Category:
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
        
        self.ID = Data[0]
        self.Name = Data[1]
        self.ParentCategoryID = Data[2]
        
        # add object to collection
        Category.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.ID}) {self.Name} {'(enfant de ' + str(self.ParentCategoryID) + ')' if self.ParentCategoryID else ''}"
