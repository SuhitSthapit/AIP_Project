from django import forms

from .models import LiquorList

from .validators import validate_CanOrBottle ##to validate if user enters can or bottle

class LiquorCreateFrom(forms.Form):
	name = forms.CharField()
	category = forms.CharField(required=False)
	price = forms.FloatField(required=False)
	can_or_bottle = forms.CharField(required=False)

	def clean_name (self):               #####validate error
		name = self.cleaned_data.get("name")
		if name == "Hello":
			raise forms.ValidationError("Not a valid Name!")
		return name


##model form **active one*** 
class LiquorListCreateForm (forms.ModelForm):
	can_or_bottle = forms.CharField(required= False,validators = [validate_CanOrBottle])
	class Meta:
		model = LiquorList
		fields = [
			'name',
			'category',
			'price',
			'can_or_bottle',
			'slug'
		]

	def clean_name (self):               #####validate error
		name = self.cleaned_data.get("name")
		if name == "Hello":
			raise forms.ValidationError("Not a valid Name!")
		return name

	def __init__(self, user=None, *args, **kwargs):
		super(LiquorListCreateForm, self).__init__(*args, **kwargs)
	#	self.fields['name'].queryset =  LiquorList.object.filter(owner = user)