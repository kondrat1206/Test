base_rate = 40
price_per_km = 10
total_trip = 0



def calculate_trip_price(distance_km):
    global total_trip
    price = base_rate + price_per_km * distance_km
    total_trip += 1
    return price

price = calculate_trip_price(5)
print(price)
print(total_trip)