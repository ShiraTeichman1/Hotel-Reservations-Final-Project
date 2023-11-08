class Guest:
    def __init__(self, row):
        self.customer_type = row['customer_type']
        self.country = row['country']
        self.market_segment = row['market_segment']
        self.adr = row['adr']
        self.arrival_date = row['arrival_date']
        self.arrival_date_week_number = row['arrival_date_week_number']
        self.adults = row['adults']
        self.children = row['children']
        self.babies = row['babies']

    def __str__(self):
            return f'Person({self.first_name},{self.last_name},{self.age})'

        
