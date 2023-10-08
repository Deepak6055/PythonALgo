"""
You are planning a road trip in a car with a limited fuel tank capacity.
Along your route, there are gas stations where you can refuel your car. 
Your goal is to determine the minimum number of refills required to reach your destination 
or, if it's not possible to reach the destination, to identify that it's not possible.

1. Implement a class CarFuel with the following methods:
    a. __init__(self, max_dist, mileage, stops): Initialize the instance with maximum distance the
    car can travel (max_dist), car's mileage on a full tank (mileage), and list of distances to 
    gas stations and the destination (stops).

    b.calculate_min_refills(self): Calculate the minimum number of refills needed to reach 
    the destination or return -1 if not possible.

2. Traverse the list of gas stations and destinations stored in stops.

3. Track current mileage available and the number of refills required.

4. If the car runs out of mileage without reaching the next gas station or destination, return -1.

5. Update current mileage if reaching the next station is possible without running out of fuel.

6. Return the minimum number of refills needed to reach the destination.
"""

class CarFuel:
    def __init__(self, max_dist, mileage, stops):
        """
        Initialize a CarFuel instance.

        Args:
            max_dist (int): The maximum distance the car can travel.
            mileage (int): The car's mileage on a full tank.
            stops (list): A list of distances from the starting point to gas stations.
        """
        self.max_dist = max_dist
        self.mileage = mileage
        self.stops = stops

    def calculate_min_refills(self):
        """
        Calculate the minimum number of refills needed to reach a destination.

        Returns:
            int: The minimum number of refills needed. Returns -1 if it's not possible to reach the destination.
        """
        refuel = self.mileage
        count = 0
        i = 0

        while i < len(self.stops) - 1:
            if self.mileage >= (self.stops[i + 1] - self.stops[i]):
                self.mileage -= (self.stops[i + 1] - self.stops[i])
            else:
                self.mileage = refuel - (self.stops[i + 1] - self.stops[i])
                if self.mileage < 0:
                    return -1
                else:
                    count += 1
            i += 1

        return count

# Example doctests
def car_fuel_example_tests():
    """
    >>> car = CarFuel(400, 200, [200, 375, 550, 750])
    >>> car.calculate_min_refills()
    2

    >>> car = CarFuel(3, 1, [1, 2, 5, 9])
    >>> car.calculate_min_refills()
    -1

    >>> car = CarFuel(250, 100, [100, 150])
    >>> car.calculate_min_refills()
    0
    """
    pass  # Pass is used here because the tests are in the docstring

# Run the example doctests when the script is executed
if __name__ == "__main__":
    import doctest
    doctest.testmod()
