from django.db import models

class Liquor(models.Model):
	"""This class represents the Liquor model."""
	name = models.CharField(max_length=255, blank=False, unique=True)
	category = models.CharField(max_length = 150, null = True, blank = True)
	price = models.FloatField(default = 0.0)
	can_or_bottle = models.CharField(max_length = 150, default = 'bottle')
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""Return a human readable representation of the model instance."""
		return "{}".format(self.name)