import webapp2
import jinja2
import os

from rot13 import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler) :
	def write(self, *a, **kw) :
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params) :
		t = jinja_env.get_template(template)
		return t.render(params)                                 #Here render is a jinja func 

	def render(self, template, **kw) :
		self.write(self.render_str(template, **kw))

class MainPage(Handler) :
	
	def get(self) :
		text = ''
		self.render('rot.html', text = text)

	def post(self) :
		text = ''
		text = self.request.get('text')
		text = rot13(text)
		self.render('rot.html', text = text)

app = webapp2.WSGIApplication([('/', MainPage)], debug = True)

		

