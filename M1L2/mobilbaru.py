class Mobil:

    def __init__(self, car_color, car_brand):
        self.color = car_color
        self.brand = car_brand

    def drive(self):
        print("Jalan")

    def stop(self):
        print("Berhenti")

    def about_car(self):
        print("warna mobil adalah: ", self.color, ", merek mobil tersebut adalah: ", self.brand)


sport = Mobil("merah", "Ferrari")
truck = Mobil(car_brand = "Honda", car_color = "putih")

sport.about_car()
truck.about_car()