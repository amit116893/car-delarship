class Car:
    def __init__(self, make, model, year, price, mileage, id=None):
        if not make or not make.strip():
            raise ValueError("Make cannot be empty.")
        if not model or not model.strip():
            raise ValueError("Model cannot be empty.")
        if year < 0:
            raise ValueError("Year cannot be negative.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if mileage < 0:
            raise ValueError("Mileage cannot be negative.")

        self.id = id
        self.make = make.strip()
        self.model = model.strip()
        self.year = year
        self.price = price
        self.mileage = mileage

    def __str__(self):
        return f"[ID: {self.id}] {self.year} {self.make} {self.model} | ${self.price:,.2f} | {self.mileage:,} km"

    def to_tuple(self):
        return (self.make, self.model, self.year, self.price, self.mileage)
