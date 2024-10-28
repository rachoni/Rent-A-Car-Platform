from backend import initialize_cars, rent_car, return_car
from frontend import display_cars, main_menu, get_car_id, get_rental_days


def run_app():
    cars = initialize_cars()

    while True:
        option = main_menu()

        if option == "1":
            display_cars(cars)

        elif option == "2":
            car_id = get_car_id()
            if car_id is not None:
                message = rent_car(cars, car_id)
                print(message)

        elif option == "3":
            car_id = get_car_id()
            if car_id is not None:
                rental_days = get_rental_days()
                if rental_days is not None:
                    message = return_car(cars, car_id, rental_days)
                    print(message)

        elif option == "4":
            print("Exiting RentACar. Thank you!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    run_app()