from django.db import models

# Create your models here.
class Speaker(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=255)
	desc = models.TextField()

	def __unicode__(self):
		return '%s %s' % (self.name, self.desc)