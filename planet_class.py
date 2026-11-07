class Planet:
    def __init__(self, name, planet_type, star):
        variables = (name, planet_type, star)

        if not all(isinstance(var, str) for var in variables):
            raise TypeError("name, planet type, and star must be strings")
        if not name or not planet_type or not star:
            raise ValueError("name, planet_type, and star must be non-empty strings")
        
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

planet_1 = Planet("mars", "circle", "sun")
planet_2 = Planet("earth", "circle", "moon")
planet_3 = Planet("Jipiter", "saturn", "sun")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.__str__())
print(planet_2.__str__())
print(planet_3.__str__())

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
