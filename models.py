from google.appengine.ext import db


class Poll(db.Model):
    author = db.UserProperty()
    question = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

    @property
    def db_key(self):
        return self.key()


class Choice(db.Model):
    poll = db.ReferenceProperty(Poll)
    content = db.StringProperty(multiline=True)
    votes = db.IntegerProperty(default=0)
