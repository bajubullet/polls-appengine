import webapp2

from google.appengine.api import users
from google.appengine.ext import db


class Poll(db.Model):
    """Models an individual Poll entry with an author, question and date."""
    author = db.UserProperty()
    question = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        self.response.headers['Content-type'] = 'text/plain'
        if user:
            self.response.write('Hello ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

