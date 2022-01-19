class Vehicle:
    def __init__(self, color: str, motor_type: str):
        self.color = color
        self.motor_type = motor_type

    def describe(self):
        return f'Vehicle is {self.color} and the motor is {self.motor_type}'

class DestinationMixin:
    def travel_to(self, destination: str) -> str:
        return f'Traveling to {destination}'

    def create_stop(self, stop_name: str, coordinates: list):
        return f'Stoping at {stop_name}. Located in {coordinates[0]}, {coordinates[1]}'


class Tesla(Vehicle, DestinationMixin):
    def __init__(self, range: int, top_speed: int, color: str, motor_type: str):
        super().__init__(color, motor_type)
        self.range = range
        self.top_speed = top_speed

    def customize(self, interior: str, performance: bool, auto_drive: str) -> dict:
        return {interior: interior, performance: performance, auto_drive: auto_drive}


class Nissan(Vehicle, DestinationMixin):
    def __init__(self, model: str, zero_hundred_time: float, color: str, motor_type: str):
        super().__init__(color, motor_type)
        self.model = model
        self.zero_hundred_time = zero_hundred_time

    def personalizations(self, turbo: bool, nitro: bool):
        def zero_hundred_update():
            less_speed = 0
            if turbo:
                less_speed += 0.2
            if nitro:
                less_speed += 0.1
            return less_speed
        return self.zero_hundred_time - zero_hundred_update()

class SpeedBoat(Vehicle, DestinationMixin):
    def __init__(self, color: str, motor_type: str):
        super().__init__(color, motor_type)


nissan_gtr = Nissan("R34", 4.9, "purple", "mecanic") 
tesla = Tesla(512, 217, "black", "electric")
boat = SpeedBoat("boat", "mecanic")


print('======== Nissan ======')
print(nissan_gtr.travel_to("California"))
print(nissan_gtr.create_stop("Nevada", [-0.1213, 1.1231]))

print('======== Tesla ======')
print(tesla.customize("white", True, "Total"))
print(tesla.travel_to("Barcelona"))

print('======== Boat ======')
print(boat.travel_to("Ibiza"))