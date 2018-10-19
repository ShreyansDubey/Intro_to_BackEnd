import cgi

def escaping_char(s) :
	return cgi.escape(s, quote = True)