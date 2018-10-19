import webapp2
from valMonth import *
from valYear import *
from valDate import *
from escChar import *

form="""<form method="post" action="/">
	<label> Date
		<input type="text" name="date" value="%(date)s">
	</label>
	<br>
	
	<label> Month
		<input type="text" name="month" value="%(month)s">
	</label>
	<br>
	
	<label> Year
		<input type="text" name="year" value="%(year)s">
	</label>
	<br>
	<div style="color :red">%(error)s</div>
	<input type="submit"> 
	</form>"""

class MainPage(webapp2.RequestHandler) :
	def write_form(self, error='', date='', month='', year='') :
		self.response.out.write(form % {'error' : error, 'date' : date, 'month' : month, 'year' : year})

	def get(self) :
		self.write_form()

	def post(self) :
		user_date = valid_date(self.request.get('date'))
		user_month = valid_month(self.request.get('month'))
		user_year = valid_year(self.request.get('year'))

		date = escaping_char(self.request.get('date'))
		month = escaping_char(self.request.get('month'))
		year = escaping_char(self.request.get('year'))


		if not (user_year and user_month and user_date) :
			self.write_form('Not Valid',date, month, year)
		
		else :
			self.redirect('/Thanks')

class ThanksHandler(webapp2.RequestHandler) :
	def get(self) :
		self.response.out.write('Thanks!!')



app = webapp2.WSGIApplication([('/', MainPage), ('/Thanks', ThanksHandler)], debug=True)