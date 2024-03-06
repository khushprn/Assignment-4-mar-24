class Car:
    def __init__(self, regnum, maxspeed):
        self.reg = regnum
        self.ms = maxspeed
        self.cs = 0
        self.td = 0

newcar = Car("XYZ-456", 180)

print("Registration Number:", newcar.reg)
print("Maximum Speed:", newcar.ms, "km/h")
print("Current Speed:", newcar.cs, "km/h")
print("Travelled Distance:", newcar.td, "km")