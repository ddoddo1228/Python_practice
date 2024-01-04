class Car:
    def __init__(self, speed, sit):
        self.Speed = speed
        self.Sit = sit
        
    def speed_up(self, ospeed):
        print("속도가 " + self.Speed + "에서 " + ospeed + "으로 증가했습니다.")
        self.Speed = ospeed
        
    def speed_down(self, ospeed):
        print("속도가 " + self.Speed + "에서 " + ospeed + "으로 감소했습니다.")
        self.Speed = ospeed
        
    def about_car(self):
        print("승용차의 속도는 " + self.Speed + "km, 좌석수는 " + self.Sit + "개 입니다.")
        
class Truck(Car):
    def __init__(self, speed, sit, tspeed, weight):
        super().__init__(speed, sit)
        self.Tspeed = tspeed
        self.Weight = weight
    
    def about_car(self):
        super().about_car()
        print("트럭의 속도는 " + self.Tspeed + "km, 총중량은 " + self.Weight + "톤 입니다.")
    
s1speed = Car("60", "5")
s1speed.speed_up("80")
s1speed.speed_down("30")

otruck = Truck("100", "5", "80", "50")
otruck.about_car()
