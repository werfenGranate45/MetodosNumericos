from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class DegreeForm(forms.Form):
    min_value = 0
    max_value = 360
    message   = "Solo se permite valores entre 0 - 360°"

    degree_field = forms.FloatField(required=True, validators= [
        MinValueValidator(min_value, message=message),
        MaxValueValidator(max_value, message=message)
    ])


