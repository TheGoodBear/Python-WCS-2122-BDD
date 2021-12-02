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
        self.Category = Category.GetElement(self.CategoryID)
        self.Colors = []
        
        # add object to collection
        Vegetal.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        # CategoryNames = [self.Category.Name]
        # if self.Category.ParentCategoryID:
        #     CategoryNames.append(self.Category.ParentCategory.Name)
        # Family = f"{' → '.join(CategoryNames)}"
        CategoryNames = Category.GetHierarchyNames(self.Category, ", ")

        return (
            f"({self.ID}) {self.Name}" + 
            f" (espèce {CategoryNames})" + 
            f"{' ' + self.Comment if self.Comment else ''}" + 
            f"\n\t{', '.join(self.Colors) if self.Colors else 'Aucune couleur associée'}")


    @classmethod
    def GetElement(cls,
        ID: int) -> object:
        """
            Return the element matching specified ID
            (Read one du CRUD)

            Args:
                ID: ID of element

            Returns:
                object: of model type
        """
    
        try:
            return [
                Element
                for Element
                in cls.List
                if Element.ID == ID][0]
        
        except:
            return None
