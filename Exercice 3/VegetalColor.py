# coding: utf-8

# imports

# class
from Vegetal import Vegetal
from Color import Color


class VegetalColor:
    """
        Model for VegetalColor table (n-n)
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
                    VegetalID : foreign key to vegetal table
                    ColorID : foreign key to color table
        """
        
        # native properties
        self.VegetalID = Data[0]
        self.ColorID = Data[1]
        
        # calculated properties
        self.VegetalName = [
            Element.Name
            for Element
            in Vegetal.List
            if Element.ID == self.VegetalID][0]
        self.ColorName = [
            Element.Name
            for Element
            in Color.List
            if Element.ID == self.ColorID][0]
        
        # add object to collection
        VegetalColor.List.append(self)


    def __str__(self) -> str:
        """
            Override data representation
            
            return string
        """

        return f"({self.VegetalID}) {self.VegetalName} - ({self.ColorID}) {self.ColorName}"


    @classmethod
    def GetRelation(
        cls,
        VegetalID : int = None,
        ColorID : int = None) -> list[object]:       
        """
            Get all objects matching specified ID
        """
        
        Result = None
        if VegetalID:
            Result = [
                Color.GetElement(Element.ColorID).Name
                for Element 
                in cls.List
                if Element.VegetalID == VegetalID]
        elif ColorID:
            Result = [
                Vegetal.GetElement(Element.VegetalID).Name 
                for Element 
                in cls.List
                if Element.ColorID == ColorID]
            
        return Result
