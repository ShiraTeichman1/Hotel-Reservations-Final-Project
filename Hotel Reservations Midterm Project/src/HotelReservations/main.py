import pandas as pd
import numpy as np
import math
from data_analysis.cleaning import cleaning
from db.database_actions import create_tables_from_df
from  db.queries import get_top_agents_reservations_in_country, get_not_canceled_reserations_in_year_within_price_range, booking_method_for_year_with_most_cancellations

def main():
    #df_hotel= pd.read_csv(r'C:\Users\Shira\Desktop\Integralytics\EntranceProject\Hotel-Reservations-Final-Project\Hotel Reservations Midterm Project\src\HotelReservations\hotel_bookings.csv', na_values=['undefined', 'Undefined', 'none', 'None', '-', ''])
    #df_hotel = cleaning(df_hotel)
    #create_tables_from_df(df_hotel) l.105..6586
    
  
    choice = input(
        '''menu:\n If you would like to view the best agent\'s top 10 reservations and guest information for the country of yout choice, enter 1.\n If you would like to view reservations and guest information for reserations that were not canceled, for the price range and year of your choice, enter 2. \n If you would like to view the booking method for the cancellations in the year that had the most cancellations, enter 3''' 
    )
    if choice == '1':
        country = input('Which country would you like to see the reservations for?')
        reservations = get_top_agents_reservations_in_country(country)
        for r in reservations:
            print(r)
    elif choice == '2':
        min_price = input('What is the minimum price of a reservation you would like to see?')
        max_price = input('What is the maximum price of a reservation you would like to see?')
        year = input('What year would you like to see the reservations for?')
        reservations = get_not_canceled_reserations_in_year_within_price_range(year, min_price, max_price)
        for r in reservations:
            print(r)
    elif choice == '3':
        res = booking_method_for_year_with_most_cancellations()
        print(res)
    else:
        print('That is not a valid choice')


if __name__ == '__main__':
    main()