import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

hidden_html = """
<input type="hidden" name="food" value="%s">
"""

item_html = """
<li>%s</li>
"""

shoppingList_html = """
<br>
<br>
<h3>Shopping List</h3>
<ul>
	%s
</ul>
"""

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
		items = self.request.get_all('food')
		self.render('temp.html', items = items)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)