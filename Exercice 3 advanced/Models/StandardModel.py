# coding: utf-8

# imports

# class
class StandardModel:
    """
        Stand model
    """
    
    # class properties
    
    # methods
    def __init__(self, 
        Data: tuple):
        """
            Constructor

            Args:
                Data : contains all columns
                    ID : primary key
        """
        
        # model properties
        self.ID = Data[0]
        self.Name = Data[1]
        
        # calculated properties


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

    
    @classmethod
    def PrintAll(cls):
        """
            Print collection

            Args:
                Model : model collection to print  
        """
        
        for Element in cls.List:
            print(Element)
        print()
