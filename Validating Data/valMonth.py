months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Decmember']
month_abbr = dict((month[:3].lower(), month) for month in months)

def valid_month(month) :
	if month :
		month_short = month[:3].lower()
		return month_abbr.get(month_short)

print valid_month('d') 
