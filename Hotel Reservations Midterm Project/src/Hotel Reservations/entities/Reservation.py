import Guest

class Reservation:
    def __init__(self, row):
        self.hotel = row['hotel']
        self.is_canceled = row['is_canceled']
        self.lead_time = row['lead_time']
        self.stays_in_weekend_nights = row['stays_in_weekend_nights']
        self.stays_in_week_nights = row['stays_in_week_nights']
        self.meal = row['meal']
        self.distribution_channel = row['distribution_channel']
        self.is_repeated_guest = row['is_repeated_guest']
        self.previous_cancellations = row['previous_cancellations']
        self.previous_bookings_not_canceled = row['previous_bookings_not_canceled']
        self.reserved_room_type = row['reserved_room_type']
        self.assigned_room_type = row['assigned_room_type']
        self.booking_changes = row['booking_changes']
        self.deposit_type = row['deposit_type']
        self.agent = row['agent']
        self.company = row['company']
        self.days_in_waiting_list = row['days_in_waiting_list']
        self.reservation_status = row['reservation_status']
        self.reservation_status_date = row['reservation_status_date']
        self.direct_booking = row['direct_booking']
        self.guest = Guest(row)

        def __str__(self):
            return f'Person({self.first_name},{self.last_name},{self.age})'

from enum import Enum
 
class ReservedRoomType(Enum):
    C = 1
    A = 2
    D = 3
    E = 4
    G = 5
    F = 6
    H = 7
    L = 8
    P = 9
    B = 10
class AssignedRoomType(Enum):
    C = 1
    A = 2
    D = 3
    E = 4
    G = 5
    F = 6
    I = 7
    B = 8
    H = 9
    P = 10
    L = 11
    K = 12

class DepositType(Enum):
    NO_DEPOSIT = 1
    REFUNDABLE = 2
    NON_REFUND = 3

class CustomerType(Enum):
    TRANSIENT = 1
    CONTRACT = 2
    TRANSIENT_PARTY = 3
    GROUP = 4
        


