from entities.Reservation import Reservation
from db.database_actions import query

def get_top_agents_reservations_in_country(country):
	
    query = f'''
	Select TOP 10 r.* , g.* from Reservation r
	   LEFT JOIN Guest g ON r.GuestId = g.GuestId 
	   WHERE country = 'PRT'
	   and agent = (
			Select TOP 1 agent  from Reservation as r
				LEFT JOIN Guest g ON r.GuestId = g.GuestId
			WHERE country = {country}
			GROUP BY agent
			ORDER BY count(*) desc
	   )'''
    return reservations(query)


def get_not_canceled_reserations_in_year_within_price_range(year, min_price, max_price):
	   
       query = f'''	   
	   SELECT r.* , g.* FROM Reservation r 
	   LEFT JOIN Guest g ON r.GuestId = g.GuestId
	   WHERE year(reservation_status_date) = {year}
		AND adr BETWEEN {min_price} AND {max_price}
		AND reservation_status !=  'Canceled' '''  
       return reservations(query)         


def booking_method_for_year_with_most_cancellations():
    
    sql_query = '''
    SELECT
		TOP 1 YEAR(reservation_status_date),
		CASE
			WHEN agent > 0 THEN 'agent'
			WHEN company > 0 THEN 'company'
			WHEN direct_booking = 'yes' THEN 'directly'
			ELSE 'None of the above'
		END
	FROM Reservation
	WHERE YEAR(reservation_status_date) = 
		(
            SELECT TOP 1  YEAR(reservation_status_date) from Reservation 
		WHERE reservation_status = 'canceled'
		GROUP BY year(reservation_status_date)
		ORDER BY count(reservation_status) DESC 
        )'''
    return query(sql_query)

def reservations(sql_query):
        df = query(sql_query)
        reservation_list = []
        for index, row in df.iterrows():
            reservation_list.append(Reservation(row))
        return reservation_list
