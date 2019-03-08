from django import forms
from recipebox.models import Author, Recipe

class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=124)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())

class AuthorAddForm(forms.Form):
    pass

    # user = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE
    # )
    # bio = models.CharField(max_length=124)
