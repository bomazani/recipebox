from django import forms
from recipebox.models import Author, Recipe

class RecipeAddForm(forms.Form):
    title = forms.CharField(label='Recipe Title', max_length=124)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    time_required = forms.IntegerField(label='Cooking Time (in minutes)')
    body = forms.CharField(label='Ingredients/Steps/Serving Suggestions', widget=forms.Textarea)
    author = forms.ModelChoiceField(label='Recipe Author', queryset=Author.objects.all())
    
class AuthorAddForm(forms.Form):
    username = forms.CharField(label="Enter new user's username.", max_length=124)
    first_name = forms.CharField(label="User's First Name", max_length=30)
    last_name = forms.CharField(label="User's Last Name", max_length=120)
    email = forms.EmailField(label="User's Email", )
    bio = forms.CharField(label="Enter new user's bio.", widget=forms.Textarea)

class SignupForm(forms.Form):
    username = forms.CharField(label="Enter new user's username.", max_length=50)
    first_name = forms.CharField(label="User's First Name", max_length=30)
    last_name = forms.CharField(label="User's Last Name", max_length=120)
    email = forms.EmailField(label="User's Email", )
    bio = forms.CharField(label="Enter new user's bio.", widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
