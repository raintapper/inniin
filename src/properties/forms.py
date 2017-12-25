from django import forms

from .models import PropertyItem
from .validators import validate_title

class PropertyCreateForm(forms.Form):

	title		= forms.CharField()
	description = forms.CharField(required=True)
	location	= forms.CharField(required=False)

	# remember to add "clean_" to validate the specific field
	

class PropertyItemCreateForm(forms.ModelForm):
	# title 		= forms.CharField(required=False, validators=[validate_title])
	class Meta:
		model = PropertyItem
		fields = [
			'title',
			'description',
			'location',
			'slug',
		]

	def clean_title(self):
		
		title = self.cleaned_data.get("title")
		if title == "hello":
			raise forms.ValidationError("Not a valid title")
		return title

