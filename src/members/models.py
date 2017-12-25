from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from .utils import code_generator

# Create your models here.

User = settings.AUTH_USER_MODEL

class MemberManager(models.Manager):
	def toggle_follow(self, request_user, username_to_toggle):
		member_ = Member.objects.get(user__username__iexact=username_to_toggle)
		user = request_user
		is_following = False
		if user in member_.followers.all():
			member_.followers.remove(user)
		else:
			member_.followers.add(user)
			is_following = True
		return member_, is_following

class Member(models.Model):
	user 			= models.OneToOneField(User) #user.all()
	followers		= models.ManyToManyField(User, related_name='is_following', blank=True) #users.follower.all()
	#following		= models.ManyToManyField(User, related_name='following', blank=True) #users.following.all()
	activation_key	= models.CharField(max_length=120, blank=True, null=True)
	activated		= models.BooleanField(default=False)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)

	objects = MemberManager()

	def __str__(self):
		return self.user.username

	def send_activation_email(self):
		if not self.activated:
			self.activation_key = code_generator()
			self.save()
			sent_mail = False
			return sent_mail
			#send mail

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		member, is_created = Member.objects.get_or_create(user=instance)
		default_user_member = Member.objects.get_or_create(user__id=1)[0] #user__usernam=
		#assign new signups as follower of firstuser (user__id=1), since it is a tuple, use [0]
		default_user_member.followers.add(instance)
		#assign to follow a new signup using firstuser
		member.followers.add(default_user_member.user)
		member.followers.add(2)

post_save.connect(post_save_user_receiver, sender=User)		