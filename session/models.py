from django.db import models
from speaker.models import *

# Create your models here.
class Session(models.Model):
	title = models.CharField(max_length=100)
	speaker = models.ForeignKey(Speaker, related_name='+')
	desc = models.TextField()

	def __unicode__(self):
		return '%s %s' % (self.title, self.speaker)