class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500

    def add_customer(self, name, purchases):
        if name in self.customers.keys():
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name, purchase):
        self.add_customer(name, [purchase])

    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)

    def get_total_cost(self, purchases):
        a = 0
        for z in purchases:
            if z['price'] > self.tax_threshold:
                taxed_price = z['price'] * (1 + self.tax_rate)
                a += taxed_price
            else:
                a += z['price']
        return a

    def generate_report(self):
        for customer, purchases in self.customers.items():
            total_cost = self.get_total_cost(purchases)
            
            print(customer)
            if total_cost > self.discount_threshold:
                print("Eligible for discount")
            else:
                if total_cost > 300:
                    print("Potential future discount customer")
                else:
                    print("No discount")
            if total_cost > 1000:
                print("VIP Customer!")
            else:
                if total_cost > 800:
                    print("Priority Customer")

    def calculate_shipping_fee(self, purchases):
        if contains_heavy_item(purchases):
            return 50
        else:
            return 20

def contains_fragile_item(purchases):
    for purchase in purchases:
        if purchase.get('fragile', False):
            return True
    return False

def contains_heavy_item(purchases):
    for purchase in purchases:
        if purchase.get('weight', 0) > 20:
            return True
    return False

def calculate_shipping_fee_for_heavy_items(purchases):
    if containts_heavy_item(purchases):
        return 50
    return 20
            
def calculate_shipping_fee_for_fragile_items(purchases):
    if contains_fragile_item(purchases):
        return 60
    return 25