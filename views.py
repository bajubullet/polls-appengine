import webapp2

from google.appengine.api import users
from models import Poll
from utils import render


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            polls = Poll.all()
            self.response.write(render('index.html', {'polls': polls}))
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


class DetailPoll(webapp2.RequestHandler):
    def get(self, key):
        user = users.get_current_user()

        if user:
            poll = Poll.get(key)
            self.response.write(poll.question)
        else:
            self.redirect(users.create_login_url(self.request.uri))