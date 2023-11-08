import pandas as pd
import numpy as np
import math
from data_analysis import cleaning
from sql.database_actions import create_tables_from_df

def main():
    df_hotel= pd.read_csv('hotel_bookings.csv', na_values=['undefined', 'Undefined', 'none', 'None', '-', ''])
    df_hotel = cleaning(df_hotel)
    create_tables_from_df(df_hotel)
if __name__ == '__main__':
    main()