def display_cars(cars):
    print("\nAvailable Cars:")
    for car in cars:
        status = "Available" if car["available"] else "Rented"
        print(f"ID: {car['id']} - {car['brand']} {car['model']} - ${car['rental_price']}/day - {status}")

def main_menu():
    print("\nWelcome to RentACar!")
    print("1. View Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")
    return input("Please choose an option (1-4): ")

def get_car_id():
    try:
        return int(input("Enter the Car ID: "))
    except ValueError:
        print("Invalid input. Please enter a valid car ID.")
        return None

def get_rental_days():
    try:
        return int(input("Enter the number of rental days: "))
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")
        return None