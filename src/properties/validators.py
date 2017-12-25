from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

def validate_email(self):
	email = value
	if ".edu" in email:
		raise ValidationError("We do not accept edu emails")

TITLE = ['Woodlands', 'Marsiling', 'Admiralty', 'Sembawang', 'Yishun']

def validate_title(value):
	cat = value.capitalize()
	# capitalize the first letter of the word
	if not value in TITLE and not cat in TITLE:
		raise ValidationError(f"{value} This is not a valid title, must be woodlands!")

	

