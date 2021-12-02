# coding: utf-8

# imports

# class
class Color:
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
        
        self.ID = Data[0]
        self.Name = Data[1]
        
        # add object to collection
        Color.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.ID}) {self.Name}"



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
