from datetime import date

class cars:
    def __init__(self,name,modelNo,ManufacturerYear,type):
        self.name = name
        self.modelNo = modelNo
        self.ManufacturerYear = ManufacturerYear
        self.type=type
        

    def carDetails(self):
        details= f"Name: {self.name}\nModel Number: {self.modelNo}\n Manufacture Year: {self.ManufacturerYear}\nType of Car: {self.type}"
        return details

    def totalYears(self):
        currentYear= date.today().year
        return currentYear - self.ManufacturerYear

car1=cars("Audi",5,2010,"Luxury")
car2=cars("Scorpio","N1",2022,"SUV")

print(car1.name)
print(car1.carDetails())
print(car1.totalYears())

print(car2.name)
print(car2.carDetails())
print(car2.totalYears())

    
