class Employee:
    """Stores employee details"""

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_increase=5000):
        """stores the salary increase"""
        self.salary += salary_increase

    def full_name(self):
        """Return Employee's full name"""
        return f"{self.first_name} {self.last_name}"

    def get_salary(self):
        """Returns the salary"""
        return self.salary
