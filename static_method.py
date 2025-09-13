class Vehicle:
    # define the class level attributes
    company = "Mahindra & Mahindra"
    fuel_type = "diesel"

    # initialize the instace atributes
    def __init__(self, **kwargs):
        # define atributes/properties
        self.name = kwargs['name']
        self.model = kwargs['model']
        self.type = kwargs['type']
        self.cost = kwargs['cost']

    # define class methods
    # class method can access class properties & methods
    @classmethod
    def start(cls, integrated_app=False):
        if integrated_app:
            print(f'Your {cls.company} vehicle started with mobile app')
        else:
            print(f'Your {cls.company} vehicle started with Key manually')

    # define static method
    # Static method can't/shouldn't access instance / class properties & methods
    # Static method can/should access only arguments passed to the method if any or ..
    # variables created within the method to manipulate / evaluate
    @staticmethod
    def apply_break(EBS=False):
        if EBS:
            print(f'Applied breaks using Electronic breaking system')
        else:
            print(f'Applied breaks manually')

    @staticmethod
    def stop(integrated_app=False):
        if integrated_app:
            print(f'Your vehicle stopped with mobile app')
        else:
            print(f'Your vehicle stopped with Key manually')

    @staticmethod
    # an example to show that instance members & class members can't be accessible
    def example_method(integrated_app=False):
        if integrated_app:
            # observe you can't access instance properties/methods (self is unresolved)
            print(f'Your {self.company} vehicle started with mobile app')
        else:
            # observe you can't access class properties/methods (cls is unresolved)
            print(f'Your {cls.company} vehicle started with Key manually')

    # define class methods
    # class method can access class properties & methods
    @classmethod
    def fill_fuel(cls, qty_ltrs):
        print(f'{cls.company} Vehicle got filled with {qty_ltrs} ltrs {cls.fuel_type}')

    # define instance method
    # Instance method can access instance properties & methods
    def show_details_pretty(self, **kwargs):
        vehicle_details = f'name:{self.name}\ncompany:{self.company}\ntype:{self.type}\ncost:{self.cost}\
        \nfuel_type:{self.fuel_type}'
        if kwargs:
            for name, value in kwargs.items():
                vehicle_details += f"\n{name}:{value}"

        print('\nvehicle details')
        print(vehicle_details)


# only need to pass instance properties / attributes
# class properties / attributes same for all the instances
car = Vehicle(name="XUV 700", model=2023,
              type="4 wheeler", cost=2545000)
car.show_details_pretty(wheels_type="Alloy", brakes="disk", sunroof="Yes", ADAS="Yes")
# class methods can be accessed with instance or class name
car.fill_fuel(30)
car.start()
# static methods can be accessed with instance or class name
car.apply_break(True)
car.stop(True)

bike = Vehicle(name="Jumbo", model=2019,
              type="2 wheeler", cost=165000)
bike.show_details_pretty(wheels_type="Alloy", brakes="disk")
# class methods can be accessed with instance or class name
Vehicle.fill_fuel(10)
Vehicle.start()
# static methods can be accessed with instance or class name
Vehicle.apply_break(True)
Vehicle.stop()

truck = Vehicle(name="Maximo Truck", model=2024,
              type="8 wheeler", cost=4500000)
truck.show_details_pretty(brakes="drum")
truck.fill_fuel(100)
truck.start()
# static methods can be accessed with instance or class name
truck.apply_break()
truck.stop()


