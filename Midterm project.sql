

	   --a)
	  

	   Select TOP 10 r.* , g.* from Reservation r
	   LEFT JOIN Guest g ON r.GuestId = g.GuestId 
	   WHERE country = 'PRT'
	   and agent = (
			Select TOP 1 agent  from Reservation as r
				LEFT JOIN Guest g ON r.GuestId = g.GuestId
			WHERE country = 'PRT'
			GROUP BY agent
			ORDER BY count(*) desc
	   )

	   --b)
	   SELECT r.* , g.* FROM Reservation r 
	   LEFT JOIN Guest g ON r.GuestId = g.GuestId
	   WHERE year(reservation_status_date) = '2015'
		AND adr BETWEEN 25 AND 120
		AND reservation_status != 'Canceled'

	--c)

	
	SELECT
		TOP 1  YEAR(reservation_status_date),
		CASE
			WHEN agent > 0 THEN 'agent'
			WHEN company > 0 THEN 'company'
			WHEN direct_booking = 'yes' THEN 'directly'
			ELSE 'None of the above'
		END
	FROM Reservation
	WHERE YEAR(reservation_status_date) = 
		(SELECT TOP 1  YEAR(reservation_status_date) from Reservation 
		WHERE reservation_status = 'canceled'
		GROUP BY year(reservation_status_date)
		ORDER BY count(reservation_status) DESC )




