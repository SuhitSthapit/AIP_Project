from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL
# Create your models here.
class LiquorList(models.Model):  ##to save data in database
	owner = models.ForeignKey(User)  ##class_instance.model_set.all()
	name = models.CharField(max_length = 150)
	category = models.CharField(max_length = 150, null = True, blank = True)
	price = models.FloatField(default = 0.0)
	can_or_bottle = models.CharField(max_length = 150, default = 'bottle')
	timestamp = models.DateTimeField (auto_now_add = True)   ### timestamp cannot be changed
	updated = models.DateTimeField (auto_now = True)    ##when the data is updated 
	slug = models.SlugField(null = True, blank = True)
	
	def __str__(self):
		return self.name            ##Return's name field when the object is referenced


	def get_absolute_url(self): ##get_absolute url   ##when successully data is added
		return reverse ('liquors:detail', kwargs = {'slug':self.slug})	

	@property              ### title is alias for name field
	def title(self):
		return self.name
 
def liquor_pre_save_receiver(sender, instance, *args, **kwargs):
	#print ('Saving...')
	#print (instance.timestamp)  #####save the slug when an object is created
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

#def liquor_post_save_receiver(sender, instance, created, *args, **kwargs):
#	print ('Saved')
#	print (instance.timestamp)

pre_save.connect(liquor_pre_save_receiver, sender = LiquorList )

#post_save.connect(liquor_post_save_receiver, sender = LiquorList )


# for data about alcohols 
#### https://bws.com.au/