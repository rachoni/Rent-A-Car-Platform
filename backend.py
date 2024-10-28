def initialize_cars():
    # List of car dictionaries with details and availability
    cars = [
        {"id": 1, "brand": "Toyota", "model": "Camry", "rental_price": 40, "available": True},
        {"id": 2, "brand": "Honda", "model": "Civic", "rental_price": 35, "available": True},
        {"id": 3, "brand": "Ford", "model": "Mustang", "rental_price": 55, "available": True},
    ]
    return cars

def rent_car(cars, car_id):
    for car in cars:
        if car["id"] == car_id and car["available"]:
            car["available"] = False
            return f"You have rented the {car['brand']} {car['model']}."
    return "Car is unavailable or invalid car ID."

def return_car(cars, car_id, rental_days):
    for car in cars:
        if car["id"] == car_id and not car["available"]:
            car["available"] = True
            total_cost = car["rental_price"] * rental_days
            return f"Car returned. Total cost: ${total_cost} for {rental_days} days."
    return "Car is already available or invalid car ID."