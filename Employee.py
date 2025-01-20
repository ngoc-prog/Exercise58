class Employee:
    def __init__(self, last_name, first_name, num_products):
        self.last_name = last_name
        self.first_name = first_name
        self.num_products = max(0, num_products)

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_num_products(self):
        return self.num_products

    def set_num_products(self, num_products):
        self.num_products = max(0, num_products)

    def getsalary(self):
        if 1 <= self.num_products <= 199:
            unit_price = 0.5
        elif 200 <= self.num_products <= 399:
            unit_price = 0.55
        elif 400 <= self.num_products <= 599:
            unit_price = 0.6
        else:
            unit_price = 0.65
        return self.num_products * unit_price

    def IsHigher(self, emp2):
        return self.num_products > emp2.num_products
