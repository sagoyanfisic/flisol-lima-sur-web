import os
import urllib
import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

class MainHandler(webapp2.RequestHandler):
    def get(self):
      template = JINJA_ENVIRONMENT.get_template('index.html')
      self.response.headers.add_header("Access-Control-Allow-Origin", "*")
      self.response.write(template.render())
        
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)