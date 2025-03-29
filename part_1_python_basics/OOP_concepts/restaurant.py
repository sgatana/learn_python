class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"The name of the restaurant is {self.restaurant_name} and it serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")


restaurant = Restaurant('KFC', 'Fast Food')
print(restaurant.restaurant_name)
