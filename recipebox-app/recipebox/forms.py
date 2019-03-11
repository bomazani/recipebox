from django import forms
from recipebox.models import Author, Recipe

class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=124)
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.DurationField()
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Recipe.objects.all())

class AuthorAddForm(forms.Form):
    user = forms.CharField(label="Enter new user's username.", max_length=124)
    bio = forms.CharField(label="Enter new user's bio.", widget=forms.Textarea)
