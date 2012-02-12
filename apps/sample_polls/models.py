# Polls Application Models
# ------------------------
#
# <strong>models.py</strong>

# Import the Django base model
from django.db import models

# The Poll model consists of a question and publication date.
# There's nothing fancy going on here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Implement the __unicode__ method to prevent Django from
    # displaying useless output in several places.
    def __unicode__(self):
        return self.question


# The Choice model shows and example of a one-to-many
# relationship and is otherwise dirt-simple.
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)

    # You might someday want to document an individual field.
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice