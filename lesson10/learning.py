
class Person():
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