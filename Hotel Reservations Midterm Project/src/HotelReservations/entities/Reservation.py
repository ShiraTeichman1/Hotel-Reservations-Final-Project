from .Guest import Guest
# from enums.AssignedRoomType import AssignedRoomType
# from enums.ReservedRoomType import ReservedRoomType
# from enums.DepositType import DepositType  

class Reservation:
    def __init__(self, row):
        self.hotel = row['hotel']
        self.is_canceled = row['is_canceled']
        self.lead_time = row['lead_time']
        self.stays_in_weekend_nights = row['stays_in_weekend_nights']
        self.stays_in_week_nights = row['stays_in_week_nights']
        self.meal = row['meal']
        self.distribution_channel = row['distribution_channel']
        self.arrival_date = row['arrival_date']
        self.arrival_date_week_number = row['arrival_date_week_number']
        #self.reserved_room_type =  ReservedRoomType[row['reserved_room_type']]
        self.reserved_room_type =  row['reserved_room_type']
        #self.assigned_room_type = AssignedRoomType[row['assigned_room_type']]
        self.assigned_room_type = row['assigned_room_type']
        self.booking_changes = row['booking_changes']
        #self.deposit_type = DepositType.row['deposit_type']
        self.deposit_type = row['deposit_type']
        self.agent = row['agent']
        self.company = row['company']
        self.days_in_waiting_list = row['days_in_waiting_list']
        self.reservation_status = row['reservation_status']
        self.reservation_status_date = row['reservation_status_date']
        self.direct_booking = row['direct_booking']
        self.guest = Guest(row)

    def __str__(self):
        return (f'''This reservation is at the hotel : {self.hotel}.
        The reservation is for {self.stays_in_week_nights } week nights and {self.stays_in_weekend_nights} weekend nights.
        The meal type for this reservation is {self.meal}. The guests arrived on {self.arrival_date}. The reserved room is of type {self.reserved_room_type}
        and an assigned room type of {self.assigned_room_type}. The guest information is as follows: {self.guest}. 
        Thank you for making a reservation with us. We hope you enjoy your stay.''')
        



 





        


