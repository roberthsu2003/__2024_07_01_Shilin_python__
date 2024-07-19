
import random
class Person():
    @staticmethod
    def getPerson(name:str):
        height = random.randint(150,190)
        weight = random.randint(50,90)
        return Person(n=name,h=height,w=weight)
    
    @classmethod
    def getPerson1(cls,name:str):
        height = random.randint(150,190)
        weight = random.randint(50,90)
        return Person(n=name,h=height,w=weight)

    def __init__(self,n:str,h:int,w:int):
        self._name = n
        self._height = h
        self._weight = w

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def height(self)->int:
        return self._height
    
    @property
    def weight(self)->int:
        return self._weight

    def getBmi(self) -> float:
        return self.weight / (self.height/100) ** 2
    
    def get_status(self) -> str:
        bmi:float = self.getBmi()
        if bmi >= 35:
            return '重度肥胖'
        elif bmi >= 30:
            return '中度肥胖'
        elif bmi >= 27:
            return '輕度肥胖'
        elif bmi >= 24:
            return '體重過重'
        elif bmi >= 18.5:
            return '體重正常'
        else:
            return '體重過輕'
        
    def bmi_print(self)->str:
        return f"{self.name}你好\n身高是：{self.height}公分\n體重是：{self.weight}公斤\nBMI:{round(self.getBmi(),ndigits=2)}\n{self.get_status()}"

def getPerson(name:str) -> Person:
    height = random.randint(150,190)
    weight = random.randint(50,90)
    return Person(n=name,h=height,w=weight)

