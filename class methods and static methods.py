class cars:
    car_prize = 100000
    def __init__(self,brand,colour,model,Cartype):
        self.brand = brand
        self.colour = colour
        self.model = model
        self.Cartype = Cartype

    def prize(self,amount):
        self.prize = self.prize - amount

    @classmethod
    def change_prize(cls,amount):
        cls.prize = amount

    @staticmethod
    def numberOfcars(number):
        available_cars = [10,15,20,25,30]
        if number in available_cars:
            return "Car is available for sale"
        else:
            return "Car is not available for sale"

        
car1 = cars("BMW","Black","M1","EV")
car2 = cars("AUDI","Blue","A3","Petrol")
cars.change_prize = 50000
print(car1.change_prize)
print(car2.change_prize)

print(car1.numberOfcars(5))
print(car2.numberOfcars(10))
