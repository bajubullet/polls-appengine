import jinja2
import os
import webapp2

from google.appengine.api import users
from google.appengine.ext import db


jinja_environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class Poll(db.Model):
    """Models an individual Poll entry with an author, question and date."""
    author = db.UserProperty()
    question = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            template = jinja_environment.get_template('index.html')
            polls = db.GqlQuery("SELECT * "
                                "FROM Poll "
                                "ORDER BY date DESC LIMIT 10")
            template_values = {'polls': polls}
            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))


class AddPoll(webapp2.RequestHandler):
    def post(self):
        question = self.request.get('question')
        poll = Poll()
        poll.question = question
        if users.get_current_user():
            poll.author = users.get_current_user()
        poll.put()
        self.redirect('/')



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/addpoll/', AddPoll),
], debug=True)

