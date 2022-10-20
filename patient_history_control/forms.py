from django import forms
from .models import HistoryModel


class AddEditHistoryForm(forms.ModelForm):

	"""
	This form is used to add or edit a patient history.

	This form contains a 'type' field and a 'description' field, along with a 'image' field.
	 - type: The type of the history.
	 - description: The description of the history.
	 - image: The image of the history (optional).
	"""
	image = forms.ImageField(required=False, error_messages={'invalid': "Image files only"},
							 widget=forms.FileInput)

	class Meta:
		model = HistoryModel
		fields = ['type', 'description', 'image']
	