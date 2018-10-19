def valid_date(date) :
	if date.isdigit() :
		if int(date) in range(1,32) :
			return int(date)