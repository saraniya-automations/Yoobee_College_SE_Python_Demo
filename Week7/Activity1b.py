class RentalManager:
    _instance = None
 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RentalManager, cls).__new__(cls)
            cls._instance.cars_available = ["Toyota", "Honda", "Ford"]
        return cls._instance
 
    def rent_car(self, car_name):
        if car_name in self.cars_available:
            self.cars_available.remove(car_name)
            print(f"{car_name} has been rented.")
        else:
            print(f"{car_name} is not available.")
 
    def show_available_cars(self):
        print("Available cars:", self.cars_available)
        print("memory location :",id(self.cars_available))
 
 
manager1 = RentalManager()
manager2 = RentalManager()

car_name = input("Enter car name : ")
manager1.rent_car(car_name)
manager2.show_available_cars()  
 
print("Are both managers the same object?", manager1 is manager2)
print("car name location :",id(car_name))
print("manager 2 location :",id(manager2))
print("manager 1 location :",id(manager1))

 