import webapp2
import views


app = webapp2.WSGIApplication([
    (r'/$', views.MainPage),
    (r'^/addpoll/$', views.AddPoll),
    (r'^/polls/([^/]+)?/$', views.DetailPoll),
], debug=True)

