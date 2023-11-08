Index(['hotel', 'is_canceled', 'lead_time', 'arrival_date_week_number',
       'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'children',
       'babies', 'meal', 'country', 'market_segment', 'distribution_channel',
       'is_repeated_guest', 'previous_cancellations',
       'previous_bookings_not_canceled', 'reserved_room_type',
       'assigned_room_type', 'booking_changes', 'deposit_type', 'agent',
       'company', 'days_in_waiting_list', 'customer_type', 'adr',
       'required_car_parking_spaces', 'total_of_special_requests',
       'reservation_status', 'reservation_status_date', 'arrival_date',
       'direct_booking'],

	   --a)
	   --Select TOP 1 agent from df
	   --WHERE country == 'United States'
	   --GROUP BY country
	   --ORDER BY agent desc

	   Select TOP 10 r.* , g.* from Reservation r
	   LEFT JOIN Guest g ON r.guest_id = g.guest_id 
	   -- this join doesn't seem great, 1 guest can be on multiple reservations, then what? 
	   WHERE country == 'United States'
	   GROUP BY country
	   ORDER BY agent desc

	   --b)
	   SELECT r.* , g.* FROM Reservation r 
	   LEFT JOIN Guest g ON r.guest_id = g.guest_id
	   WHERE reservation_status_date LIKE '%2019'
		AND adr BETWEEN 75 AND 120
		AND reservation_status != 'canceled'

	   
