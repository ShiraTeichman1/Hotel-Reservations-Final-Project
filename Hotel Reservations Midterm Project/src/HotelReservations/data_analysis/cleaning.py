import math 

def cleaning(df_hotel_bookings):
    df_hotel_bookings = df_hotel_bookings.astype({'is_canceled' : 'bool', 'is_repeated_guest' : 'bool', 'reservation_status_date' : 'datetime64[ns]' })
    df_hotel_bookings = df_hotel_bookings.assign(arrival_date = lambda x: df_hotel_bookings['arrival_date_year'].astype(str) + '-' + df_hotel_bookings['arrival_date_month'] + '-' + df_hotel_bookings['arrival_date_day_of_month'].astype(str))
    df_hotel_bookings['arrival_date'] = df_hotel_bookings['arrival_date'].astype('datetime64[ns]')
    df_hotel_bookings = df_hotel_bookings.drop(['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month'], axis = 1)
    df_hotel_bookings['direct_booking'] = df_hotel_bookings.apply(lambda row: 'yes' if math.isnan(row['agent']) and math.isnan(row['company']) else 'no', axis = 1)
    df_hotel_bookings['children'] = df_hotel_bookings['children'].fillna(round(df_hotel_bookings['children'].mean()))
    df_hotel_bookings[['meal', 'country', 'market_segment', 'distribution_channel']] = df_hotel_bookings[['meal', 'country', 'market_segment', 'distribution_channel']].fillna(method = 'ffill')
    df_hotel_bookings[['agent', 'company']] = df_hotel_bookings[['agent', 'company']].fillna(0)
    return df_hotel_bookings
    




