from django import forms

from properties.models import PropertyItem

from .models import Item

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = [
			'propertyitem',
			'itemtype',
			'itemdesc', 		
			'itemnote', 		
			'public', 			
			#image_url (Add Image to be discussed later)
		]

	def __init__(self, user=None, *args, **kwargs):
		print(user)
		print(kwargs)
		super(ItemForm, self).__init__(*args, **kwargs)
		self.fields['propertyitem'].queryset = PropertyItem.objects.filter(owner=user)
		#.exclude(item__isnull=False)


