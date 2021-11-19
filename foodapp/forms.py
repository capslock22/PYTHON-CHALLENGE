from django import forms
from django.db.models import fields
from .models import Cuisine, Dish

class CuisineForm(forms.ModelForm):

    class Meta:
        model = Cuisine

        fields = [
            "name",
        ]


class DishForm(forms.ModelForm):

    class Meta:
        model = Dish

        fields = "__all__"