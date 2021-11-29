# coding: utf-8

# imports

# class
class Vegetal:
    """
        Model for vegetal table
    """
    
    # class properties
    List = []
    
    # methods
    def __init__(self, 
        ID: int, 
        Name: str, 
        Image: str, 
        Comment: str, 
        CategoryID: int):
        """
            Constructor

            Args:
                ID : primary key
                Name : name
                Image : image URL
                Comment : comments
                CategoryID : foreign key to Category model
        """
        
        self.ID = ID
        self.Name = Name
        self.Image = Image
        self.Comment = Comment
        self.CategoryID = CategoryID
        
        # add object to collection
        Vegetal.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.ID}) {self.Name} (famille des {self.CategoryID}) {self.Comment if self.Comment else ''}"
