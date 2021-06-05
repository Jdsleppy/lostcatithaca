from django import forms

from lostcats.models import LostCat


class CatLocateForm(forms.Form):
    latitude = forms.FloatField(
        min_value=-180,
        max_value=180,
        widget=forms.HiddenInput,
    )
    longitude = forms.FloatField(
        min_value=-180,
        max_value=180,
        widget=forms.HiddenInput,
    )


class CatCreateForm(forms.ModelForm):
    class Meta:
        model = LostCat
        fields = [
            "title",
            "description",
            "image",
            "latitude",
            "longitude",
        ]
        widgets = {
            "title": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "description": forms.widgets.Textarea(attrs={"class": "form-control"}),
            "image": forms.widgets.ClearableFileInput(attrs={"class": "form-control"}),
            "latitude": forms.HiddenInput(),
            "longitude": forms.HiddenInput(),
        }
