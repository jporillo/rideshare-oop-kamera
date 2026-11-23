from ride import Ride

class PremiumRide(Ride):
    def __init__(self, distance_km, snack):
        super().__init__(distance_km)

    def calculate_fare(self):
        pass

    def start_ride(self):
        print(f"Starting VIP Premium Ride. Enjoy your snacks!")

    def complete_ride(self):
        print(f"=== VIP RECEIPT ===\nFare: php {self.calculate_fare():.2f}")
