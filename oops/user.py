class AdminUser:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def get_name(self):
        name = self.name.upper()
        return f"User Name is: {name}"

    def age(self, current_year):
        age = (current_year - self.year)
        return f"Current Age is: {age}"


user = AdminUser("Krishna", 1987)
print(user.get_name())
print(user.age(2024))
