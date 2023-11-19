#import enums.CustomerType as ct # import CustomerType

class Guest:
    def __init__(self, row):
        self.guest_id = row['GuestId']
        self.customer_type = row['customer_type']
        #self.customer_type =  ct.CustomerType[row['customer_type']]
        self.country = row['country']
        self.market_segment = row['market_segment']
        self.adr = row['adr']
        self.adults = row['adults']
        self.children = row['children']
        self.babies = row['babies']
        self.is_repeated_guest = row['is_repeated_guest']
        self.previous_cancellations = row['previous_cancellations']
        self.previous_bookings_not_canceled = row['previous_bookings_not_canceled']

    def __str__(self):
        return f'''This guest is {self.customer_type}, from {self.country}. He is from the market segment of {self.market_segment} 
        and has an average daily rate of {self.adr}. He had {self.previous_cancellations} previous cancellations and 
        {self.previous_bookings_not_canceled} previous bookings that were not cancelled.
        He has {self.adults} adults, {self.children} children, and {self.babies} babies with him. '''


    
