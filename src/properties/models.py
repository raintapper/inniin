from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_title
# Create your models here.

User = settings.AUTH_USER_MODEL

class PropertyItemQuerySet(models.query.QuerySet):
	def search(self, query): #PropertyItem.object.all.search(query)
		#empty spaces will be ignored!
		#query = query.strip()
		if query: 
			query = query.strip()
			return self.filter(
				Q(title__icontains=query)|
				Q(location__icontains=query)|
				#from another model-->
				Q(item__itemtype__icontains=query)|
				Q(item__itemdesc__icontains=query)
				).distinct()
		return self

class PropertyItemManager(models.Manager):
	def get_queryset(self):
		return PropertyItemQuerySet(self.model, using=self._db)

	def search(self, query): #PropertyItem.object.search()
		return self.get_queryset().search(query)

class PropertyItem(models.Model):

	owner 		= models.ForeignKey(User) #please check out foreignkey JOINCFE.com
	title		= models.CharField(max_length=120, validators=[validate_title])
	description = models.CharField(max_length=400, null=False, blank=False, default='This is a property description')
	location	= models.CharField(max_length=120, null=True, blank=True)
	category	= models.CharField(max_length=120, null=True, blank=True)
	timestamp	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	slug 		= models.SlugField(unique=True, null=True, blank=True)

	objects = PropertyItemManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('properties:detail', kwargs= {'slug': self.slug})

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.title = instance.title.capitalize()
	if not instance.slug:
			instance.slug = unique_slug_generator(instance)
			
def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
	print("saved!")
	print(instance.timestamp)
	if not instance.slug:
			instance.slug = unique_slug_generator(instance)
			instance.save()

pre_save.connect(rl_pre_save_receiver, sender=PropertyItem)
post_save.connect(rl_post_save_receiver, sender=PropertyItem)