from django.conf import settings
from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .signals import object_viewed_signal
from .utils import get_client_ip
# Create your models here.

User = settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
	user 			= models.ForeignKey(User, blank=True, null=True) # User Instance
	ip_address		= models.CharField(max_length=220, blank=True, null=True) #IP Field
	content_type	= models.ForeignKey(ContentType) # AnyModel, OrderModel, Cart Model, Address Model
	object_id 		= models.PositiveIntegerField() #Anyid, OrderId
	content_object 	= GenericForeignKey('content_type', 'object_id')
	timestamp		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s viewed %s" %(self.content_object, self.timestamp)

	class Meta:
		ordering 			= ['-timestamp'] 
		verbose_name  		= 'Object viewed'
		verbose_name_plural = 'Objects viewed'


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
	c_type = ContentType.objects.get_for_model(sender) #instance.__class__
	print("this is sender" + sender)
	print("this is instance" + instance)
	print("this is request" + request)
	print("this is user" + request.user)

	new_view_obj = ObjectViewed.objects.create(
				user = request.user,
				content_type= c_type,
				object_id=instance.id,
				ip_address = get_client_ip(request)
		)

object_viewed_signal.connect(object_viewed_receiver)





