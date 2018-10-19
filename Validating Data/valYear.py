def valid_year(year) :
	if year.isdigit() :
		if int(year) in range(1901,2020) :
			return int(year)