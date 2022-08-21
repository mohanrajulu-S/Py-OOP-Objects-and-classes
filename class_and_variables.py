class cars:
    # class variable
    car_name = 'BMW'

    def __init__(self,name,colour):
        self.name = name
        self.colour = colour

# create objects
car1 = cars('BMW','blue')
car2 = cars('benz','black')

print('before')
print(car1.name, car1.colour, car1.car_name)
print(car2.name, car2.colour, car2.car_name)

#modify class variable using object reference
car1.car_name = 'Audi'
print('After')
print(car1.name, car1.colour, car1.car_name)
print(car2.name, car2.colour, car2.car_name)
