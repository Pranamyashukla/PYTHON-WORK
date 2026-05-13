class RideBooking:
    def __init__(self, customer, location):
        self.customer = customer
        self.location = location

    def booking_details(self):
        print(f"customer: {self.customer}")
        print(f"pickup location: {self.location}")


class BikeRide(RideBooking):
    def fare(self, km):
        amount = km * 10
        print(f"bike ride fare: ₹{amount}")


class AutoRide(RideBooking):
    def fare(self, km):
        amount = km * 15
        print(f"auto ride fare: ₹{amount}")


class CabRide(RideBooking):
    def fare(self, km):
        amount = km * 20
        print(f"cab ride fare: ₹{amount}")


r1 = BikeRide("rahul", "beach road")
r2 = AutoRide("aarav", "railway station")
r3 = CabRide("aryan", "airport")


r1.booking_details()
r1.fare(5)

print()

r2.booking_details()
r2.fare(5)

print()

r3.booking_details()
r3.fare(5)
