from car import Car
from database import (
    initialize_database,
    import_cars,
    add_car,
    get_all_cars,
    get_car_by_id,
    update_car,
    delete_car,
    search_cars
)


def show_menu():
    print("\n" + "=" * 40)
    print("   🚗 CAR DEALERSHIP MANAGER")
    print("=" * 40)
    print("1. Add Car")
    print("2. View All Cars")
    print("3. Update Car")
    print("4. Delete Car")
    print("5. Search Cars")
    print("6. Exit")
    return input("Enter your choice (1-6): ").strip()


def add_car_flow():
    print("\n--- Add New Car ---")
    try:
        make = input("Enter make: ").strip()
        model = input("Enter model: ").strip()
        year = int(input("Enter year: ").strip())
        price = float(input("Enter price: ").strip())
        mileage = int(input("Enter mileage: ").strip())

        car = Car(make=make, model=model, year=year, price=price, mileage=mileage)
        add_car(car)

        print(f"✅ Car added successfully with ID {car.id}")
        print(car)

    except ValueError as e:
        print(f"❌ Invalid input: {e}")


def view_all_cars_flow():
    print("\n--- All Cars ---")
    cars = get_all_cars()

    if not cars:
        print("No cars in inventory.")
        return

    for car in cars:
        print(car)


def update_car_flow():
    print("\n--- Update Car ---")
    try:
        car_id = int(input("Enter car ID to update: ").strip())
        car = get_car_by_id(car_id)

        if car is None:
            print("❌ Car not found.")
            return

        print("Current details:")
        print(car)
        print("Press Enter to keep the current value.")

        new_make = input(f"Make [{car.make}]: ").strip()
        if new_make:
            car.make = new_make

        new_model = input(f"Model [{car.model}]: ").strip()
        if new_model:
            car.model = new_model

        new_year = input(f"Year [{car.year}]: ").strip()
        if new_year:
            car.year = int(new_year)
            if car.year < 0:
                raise ValueError("Year cannot be negative.")

        new_price = input(f"Price [{car.price}]: ").strip()
        if new_price:
            car.price = float(new_price)
            if car.price < 0:
                raise ValueError("Price cannot be negative.")

        new_mileage = input(f"Mileage [{car.mileage}]: ").strip()
        if new_mileage:
            car.mileage = int(new_mileage)
            if car.mileage < 0:
                raise ValueError("Mileage cannot be negative.")

        update_car(car)
        print("✅ Car updated successfully.")
        print(car)

    except ValueError as e:
        print(f"❌ Invalid input: {e}")


def delete_car_flow():
    print("\n--- Delete Car ---")
    try:
        car_id = int(input("Enter car ID to delete: ").strip())
        car = get_car_by_id(car_id)

        if car is None:
            print("❌ Car not found.")
            return

        print("Car to delete:")
        print(car)

        confirm = input("Are you sure you want to delete this car? (y/n): ").strip().lower()
        if confirm == "y":
            deleted = delete_car(car_id)
            if deleted:
                print("✅ Car deleted successfully.")
            else:
                print("❌ Car not found.")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("❌ Invalid ID. Please enter a number.")


def search_cars_flow():
    print("\n--- Search Cars ---")
    keyword = input("Enter make, model, or year to search: ").strip()

    results = search_cars(keyword)
    print(f"Found {len(results)} car(s).")

    if not results:
        return

    for car in results:
        print(car)


def main():
    initialize_database()
    import_cars()

    while True:
        choice = show_menu()

        if choice == "1":
            add_car_flow()
        elif choice == "2":
            view_all_cars_flow()
        elif choice == "3":
            update_car_flow()
        elif choice == "4":
            delete_car_flow()
        elif choice == "5":
            search_cars_flow()
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
