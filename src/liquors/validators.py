from django.core.exceptions import ValidationError


CanOrBottle = ['CAN', 'BOTTLE']

def validate_CanOrBottle (value):
	COB = value.upper()
	if not COB in CanOrBottle:
		raise ValidationError(f"{value} is not correct type of liquor availability")