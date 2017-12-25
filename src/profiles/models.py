from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from properties.models import PropertyItem

User = settings.AUTH_USER_MODEL
class Item(models.Model):

	# associations
	user 			= models.ForeignKey(User)
	propertyitem 	= models.ForeignKey(PropertyItem) 
	# item stuff
	itemtype		= models.CharField(max_length=120)
	itemdesc 		= models.TextField(help_text='seperate each item by comma') 
	itemnote 		= models.TextField(blank=True, null=True, help_text='seperate each item by comma') 
	public 			= models.BooleanField(default=True)
	#image_url (Add Image to be discussed later)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.itemtype

	def get_absolute_url(self):
		return reverse('profiles:detail', kwargs= {'pk': self.pk})


	class Meta:
		#reverse updated, reverse timestamp. 
		#get the most recently updated first that is why the '-' sign
		ordering = ['-updated', 'timestamp']

	def get_itemdesc(self):
		return self.itemdesc.split(",")

	def get_itemnote(self):
		return self.itemnote.split(",")





